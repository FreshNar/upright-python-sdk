import requests 

class Upright:
    def __init__(self, api_key):
        self.base_url = 'https://app.uprightlabs.com/api/'
        self.api_key = api_key 

    def _get_headers(self):
        return {
            "X-Authorization": f"{self.api_key}",
            "Content-Type": "application/json",
        }
    
    def _request(self, method, endpoint, params=None, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
        )
        response.raise_for_status()

        return response
    
    def get(self, endpoint, params=None):
        response = self._request("GET", endpoint, params=params)
        return response.json()
    
    def post(self, endpoint, data=None):
        return self._request("POST", endpoint, data=data)