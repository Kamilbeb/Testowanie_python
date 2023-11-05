import pytest

from twitter import Twitter


@pytest.fixture(params=[None, 'test.txt'])  # dekorator który globalnie udostępnił nam w kodzie twitter, testy wykonają się podwójnie bez backendu i z backendem
def twitter(request):
    twitter = Twitter(backend=request.param)
    yield twitter  # kiedy poszczególne testy się wykonały wówczas uruchamia się metoda delete
    twitter.delete()


def test_twitter_initialization(twitter):
    assert twitter


def test_tweet_single_message(twitter):
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):  # sprawdzamy wystąpienie wyjątku w momencie gdy tekst jest dłuższy niż 160 znaków
        twitter.tweet(
            'test' * 41)  # tutaj będziemy sprawdzać czy nasz błąd spowoduje wywołanie wyjątku. Pytest da wynik pozytywny bo spodziewaliśmy się tego błędu
    assert twitter.tweets == []  # sprawdzenie że ten tweet nie został dodany do tweets


@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ["first"]),
        ("#first Test message", ["first"]),
        ("#FIRST Test message", ["first"]),
        ("Test message #first", ["first"]),
        ("Test message #first #second", ["first", "second"])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected
