import json
import os.path
import re
from urllib.parse import urljoin

import requests as requests

USERS_API = "https://api.github.com/users/"


class Twitter:
    version = '1.0'

    def __init__(self, backend=None, username=None):
        self.backend = backend
        self._tweets = []  # atrybut prywatny
        self.username = username

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            backend_text = self.backend.read()
            if backend_text:
                self._tweets = json.loads(backend_text)
        return self._tweets

    @property
    def tweet_massages(self):
        return [tweet['message'] for tweet in self.tweets]

    def get_user_avatar(self):
        if not self.username:
            return None

        url = urljoin(USERS_API, self.username)
        resp = requests.get(url)
        return resp.json()['avatar_url']
    def tweet(self, message):
        if len(message) > 160:  # jeżeli wiadomość ma więcej niż 160 znaków to wywołaj błąd
            raise Exception(
                "Message too long")  # Exception podstawowa klasa wyjątków pierwszy parametr to jest komunikat
        self.tweets.append({'message': message,
                            'avatar': self.get_user_avatar(),
                            'hashtags': self.find_hashtags(message)
                            })
        if self.backend:
            self.backend.write(json.dumps(self.tweets))

    def find_hashtags(self, message):  # metoda wyszukująca w wiadomości hasztag
        return [m.lower() for m in re.findall("#(\w+)", message)]
