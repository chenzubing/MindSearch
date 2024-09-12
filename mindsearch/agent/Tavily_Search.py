# from lagent.actions import BaseSearch
from lagent.schema import ActionReturn, ActionStatusCode
import requests
from typing import List
from cachetools import TTLCache, cached
from lagent.actions import BaseAction, tool_api
from lagent.actions.parser import BaseParser, JsonParser

class BaseSearch:

    def __init__(self, topk: int = 3, black_list: List[str] = None):
        self.topk = topk
        self.black_list = black_list

    def _filter_results(self, results: List[tuple]) -> dict:
        filtered_results = {}
        count = 0
        for url, snippet, title in results:
            if all(domain not in url
                   for domain in self.black_list) and not url.endswith('.pdf'):
                filtered_results[count] = {
                    'url': url,
                    'summ': json.dumps(snippet, ensure_ascii=False)[1:-1],
                    'title': title
                }
                count += 1
                if count >= self.topk:
                    break
        return filtered_results

class TavilySearch(BaseSearch):

    def __init__(self,
                 api_key: str,
                 topk: int = 3,
                 black_list: List[str] = [
                     'enoN',
                     'youtube.com',
                     'bilibili.com',
                     'researchgate.net',
                 ],
                 **kwargs):
        self.api_key = api_key
        self.proxy = kwargs.get('proxy')
        super().__init__(topk, black_list)

    @cached(cache=TTLCache(maxsize=100, ttl=600))
    def search(self, query: str, max_retry: int = 3) -> dict:
        for attempt in range(max_retry):
            try:
                response = self._call_tavily_api(query)
                return self._parse_response(response)
            except Exception as e:
                logging.exception(str(e))
                warnings.warn(
                    f'重试 {attempt + 1}/{max_retry} 由于错误: {e}')
                time.sleep(random.randint(2, 5))
        raise Exception('多次重试后仍无法从Tavily搜索获取结果。')

    def _call_tavily_api(self, query: str) -> dict:
        endpoint = 'https://api.tavily.com/search'
        params = {
            'api_key': self.api_key,
            'query': query,
            'search_depth': 'advanced',
            'max_results': self.topk * 2
        }
        response = requests.get(endpoint, params=params, proxies=self.proxy)
        response.raise_for_status()
        return response.json()

    def _parse_response(self, response: dict) -> dict:
        raw_results = []
        for result in response.get('results', []):
            raw_results.append((
                result.get('url', ''),
                result.get('content', ''),
                result.get('title', '')
            ))
        return self._filter_results(raw_results)

    @tool_api
    def run(self, query: str) -> ActionReturn:
        """使用Tavily搜索引擎进行搜索。

        Args:
            query (str): 搜索查询

        Returns:
            ActionReturn: 搜索结果
        """
        try:
            results = self.search(query)
            return ActionReturn(
                content=str(results),
                state=ActionStatusCode.SUCCESS
            )
        except Exception as e:
            return ActionReturn(
                content=str(e),
                state=ActionStatusCode.API_ERROR
            )