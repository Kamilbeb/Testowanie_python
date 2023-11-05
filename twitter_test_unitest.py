import unittest

from twitter import Twitter


class TwitterTest(unittest.TestCase):
    def setUp(self):  # metoda wykonywana przed każdym testem
        self.twitter = Twitter()

    def test_initialization(self):  # będziemy sprawdzali czy nasza klasa się tworzy
        self.assertTrue(self.twitter)  # sprawdzamy czy nasz twitter jest True

    def test_tweet_single(self):
        # When
        self.twitter.tweet('Test message')
        # Then
        self.assertEqual(self.twitter.tweets, ['Test message'])


if __name__ == '__main__':  # żeby zapobiec przy importowaniu wykonania tej funkcji
    unittest.main()  # wywołanie testów
