import requests
import json

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params, headers=headers)

        return response.json()

    def post(self, endpoint, data=None, headers=None):
        url = self.base_url + endpoint
        response = requests.post(url, data=data, headers=headers)
        return response.json()




if __name__ == "__main__":
    http = HttpClient
    host = 'https://bwc.ds44.top'
    url = '/shopapi/login/account'
    data = {
    "scene": 2,
    "mobile": 18337173786,
    "terminal":3,
    "code": 19491001
}
    headers = {}
    response = http(host).post(url, data, headers)
    print(response)