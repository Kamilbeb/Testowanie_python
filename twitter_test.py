import pytest

from twitter import Twitter


@pytest.fixture  # autouse=Truebędzie wykonana przed każdym testem bez względu czy test będzie tego potrzebował
def backend(tmpdir):
    temp_file = tmpdir.join('test.txt')
    temp_file.write('')
    return temp_file


@pytest.fixture(params=['List', 'backend'],
                name='twitter')  # dekorator który globalnie udostępnił nam w kodzie twitter, testy wykonają się podwójnie bez backendu i z backendem
def fixture_twitter(backend, request):
    if request.param == 'List':
        twitter = Twitter()
    elif request.param == 'backend':
        twitter = Twitter(backend=backend)
    return twitter


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

def test_initialize_two_twitter_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    twitter1.tweet('Test 1')
    twitter1.tweet('Test 2')

    assert twitter2.tweets == ['Test 1', 'Test 2']
@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ["first"]),
        ("#first Test message", ["first"]),
        ("#FIRST Test message", ["first"]),
        ("Test message #first", ["first"]),
        ("Test message #first #second", ["first", "second"])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected
