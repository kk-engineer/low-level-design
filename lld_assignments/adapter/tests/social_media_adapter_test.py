import unittest
from unittest.mock import patch

from ..src.services.social_media_adapter import SocialMediaAdapter
from ..src.services.facebook_adapter import FacebookAdapter
from ..src.services.twitter_adapter import TwitterAdapter


class TestSocialMediaAdapter(unittest.TestCase):

    @patch.multiple(SocialMediaAdapter, __abstractmethods__=set())
    def test_facebook_adapter(self):
        adapter = FacebookAdapter()
        
    @patch.multiple(SocialMediaAdapter, __abstractmethods__=set())
    def test_twitter_adapter(self):
        adapter = TwitterAdapter()


if __name__ == '__main__':
    unittest.main()
