from lagent.actions import BaseAction
from lagent.schema import ActionReturn, ActionStatusCode
import requests
from typing import List
import logging
import json

class TavilySearch(BaseAction):
    def __init__(self, api_key: str, topk: int = 3, **kwargs):
        super().__init__()
        self.api_key = api_key
        self.topk = topk
        self.proxy = kwargs.get('proxy')
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def search(self, query: str) -> dict:
        self.logger.debug(f"TavilySearch.search called with query: {query}")
        endpoint = 'https://api.tavily.com/search'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'api_key': self.api_key,
            'query': query,
            'search_depth': 'advanced',
            'max_results': self.topk * 2
        }
        try:
            self.logger.debug(f"Sending POST request to {endpoint}")
            self.logger.debug(f"Request data: {json.dumps(data)}")
            response = requests.post(endpoint, json=data, headers=headers, proxies=self.proxy)
            self.logger.debug(f"Response status code: {response.status_code}")
            self.logger.debug(f"Response content: {response.text}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error in TavilySearch.search: {e}")
            return {'error': str(e)}

    def run(self, query: str) -> ActionReturn:
        try:
            results = self.search(query)
            self.logger.debug(f"Raw search results: {results}")
            if isinstance(results, dict) and 'error' in results:
                error_return = ActionReturn(
                    result=[{'type': 'text', 'content': str(results['error'])}],
                    state=ActionStatusCode.API_ERROR
                )
                self.logger.debug(f"Returning error: {error_return}")
                return error_return
            
            if not isinstance(results, dict) or 'results' not in results:
                error_return = ActionReturn(
                    result=[{'type': 'text', 'content': f"Unexpected response format: {results}"}],
                    state=ActionStatusCode.API_ERROR
                )
                self.logger.debug(f"Returning error due to unexpected format: {error_return}")
                return error_return
            
            processed_results = self.process_results(results)
            success_return = ActionReturn(
                result=[{'type': 'text', 'content': json.dumps(processed_results)}],
                state=ActionStatusCode.SUCCESS
            )
            self.logger.debug(f"Returning success: {success_return}")
            return success_return
        except Exception as e:
            self.logger.error(f"Error in TavilySearch.run: {e}")
            exception_return = ActionReturn(
                result=[{'type': 'text', 'content': str(e)}],
                state=ActionStatusCode.API_ERROR
            )
            self.logger.debug(f"Returning exception: {exception_return}")
            return exception_return

    def process_results(self, results: dict) -> dict:
        processed = {}
        for idx, result in enumerate(results.get('results', [])):
            processed[str(idx)] = {
                'title': result['title'],
                'url': result['url'],
                'content': result['content']
            }
        return processed

    @classmethod
    def get_api_description(cls):
        return {
            'name': 'TavilySearch',
            'description': 'A search engine that provides web search results.',
            'parameters': [
                {
                    'name': 'query',
                    'type': 'STRING',
                    'description': 'The search query'
                }
            ],
            'required': ['query']
        }