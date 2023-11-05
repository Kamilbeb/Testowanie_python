import pytest

from twitter import Twitter

def test_twitter_initialization():
    twitter = Twitter()
    assert twitter

def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']

def test_tweet_long_message():
    twitter = Twitter()
    with pytest.raises(Exception):       #sprawdzamy wystąpienie wyjątku w momencie gdy tekst jest dłuższy niż 160 znaków
        twitter.tweet('test'*41)    #tutaj będziemy sprawdzać czy nasz błąd spowoduje wywołanie wyjątku. Pytest da wynik pozytywny bo spodziewaliśmy się tego błędu
    assert twitter.tweets == [] #sprawdzenie że ten tweet nie został dodany do tweets

