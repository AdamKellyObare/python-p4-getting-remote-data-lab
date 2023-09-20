import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self)
        return response.content

    def load_json(self):
        response_body = self.generate_response_body()
        return response_json