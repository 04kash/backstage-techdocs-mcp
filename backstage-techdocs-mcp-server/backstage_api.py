import requests
from urllib.parse import urljoin

class BackstageApiWrapper:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url
        print("Creating Backstage wrapper with", {"token": token, "baseUrl": base_url})

    def _http_request(self, path: str):
        url = urljoin(self.base_url, path)
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Backstage API returned HTTP {response.status_code}: {response.text}")

    def get_techdocs_search_results(self, query: str):
        return self._http_request(f'api/search/query?term={query}&types[0]=techdocs')