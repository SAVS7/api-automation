import requests

class BaseAPI:


    def get(self, url, params=None):
        return requests.get(url, params=params)

    def post(self, url, payload):
        return requests.post(url, json=payload)

    def put(self, url, payload):
        return requests.put(url, json=payload)

    def delete(self, url):
        return requests.delete(url)
