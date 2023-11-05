import re


class Twitter:
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) > 160:  #jeżeli wiadomość ma więcej niż 160 znaków to wywołaj błąd
            raise Exception("Message too long")   #Exception podstawowa klasa wyjątków pierwszy parametr to jest komunikat
        self.tweets.append(message)

    def find_hashtags(self, message):   #metoda wyszukująca w wiadomości hasztag
        return [m.lower() for m in re.findall("#(\w+)", message)]