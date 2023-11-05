import os.path
import re


class Twitter:
    version = '1.0'

    def __init__(self, backend=None):
        self.backend = backend
        self._tweets = []  # atrybut prywatny
        if self.backend and not os.path.exists(self.backend):
            with open(self.backend, 'w'):
                pass

    def delete(self):
        if self.backend:
            os.remove(self.backend)

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            with open(self.backend) as twitter_file:
                self._tweets = [line.rstrip('\n') for line in twitter_file]
        return self._tweets

    def tweet(self, message):
        if len(message) > 160:  # jeżeli wiadomość ma więcej niż 160 znaków to wywołaj błąd
            raise Exception(
                "Message too long")  # Exception podstawowa klasa wyjątków pierwszy parametr to jest komunikat
        self.tweets.append(message)
        if self.backend:
            with open(self.backend, 'w') as twitter_file:
                twitter_file.write("\n".join(self.tweets))

    def find_hashtags(self, message):  # metoda wyszukująca w wiadomości hasztag
        return [m.lower() for m in re.findall("#(\w+)", message)]
