import requests
import json
from urllib.parse import urljoin
from .oauth import OAuth
from .exceptions import FatalError


class Client:
    __uri_sum = '/sum'
    server_address = None
    access_token = None
    __oauth = None

    def __init__(self, server_address):
        self.server_address = server_address
        self.__oauth = OAuth(server_address)

    def __build_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

    def __get_endpoint_sum_url(self):
        return urljoin(self.server_address, self.__uri_sum)

    def endpoint_authentication(self, username, password):
        self.access_token = self.__oauth.authentication(username, password)
        return self.access_token

    def endpoint_sum(self, payload):
        result = requests.post(
            self.__get_endpoint_sum_url(),
            headers=self.__build_headers(),
            data=json.dumps(payload)
        )
        if 200 <= result.status_code <= 299:
            body = json.loads(result.content)

            return body["SHA256_hash_of_the_sum"]
        else:
            raise FatalError()
