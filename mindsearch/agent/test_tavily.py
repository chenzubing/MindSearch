import requests

endpoint = 'https://api.tavily.com/search'
data = {
       'api_key': 'Your Tavily API Key',
       'query': 'knee osteoarthritis rehabilitation methods',
       'search_depth': 'advanced',
       'max_results': 6
    }
response = requests.post(endpoint, json=data)
print(response.status_code)
print(response.text)