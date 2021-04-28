import datetime
import json
import requests
from urllib.parse import urljoin
from .exceptions import AuthenticationFailed


class OAuth:
    token = None
    __valid_token_minutes = 59
    __token_expire_in = None
    __refresh_token = None
    __server_address = ""
    __authorize_uri = "/auth"
    __refresh_authorize_uri = "/auth/refresh"

    def __init__(self, server_address):
        self.__server_address = server_address

    def __get_authorize_url(self):
        return urljoin(self.__server_address, self.__authorize_uri)

    def __get_refresh_authorize_url(self):
        return urljoin(self.__server_address, self.__refresh_authorize_uri)

    def __build_headers(self):
        return {
            "Content-Type": "application/json"
        }

    def __define_the_expires_in_token_manually(self):
        self.__token_expire_in = datetime.datetime.utcnow() + datetime.timedelta(minutes=self.__valid_token_minutes)

    def authentication(self, username, password):
        payload = json.dumps({
            'username': username,
            'password': password
        })

        result = requests.post(
            self.__get_authorize_url(),
            headers=self.__build_headers(),
            data=payload
        )

        if 200 <= result.status_code <= 299:
            body = json.loads(result.content)

            self.token = body.get("access")
            self.__refresh_token = body.get("refresh")
            if self.token:
                self.__define_the_expires_in_token_manually()
            return self.token
        else:
            raise AuthenticationFailed()

    def refresh_token(self):
        raise NotImplementedError
