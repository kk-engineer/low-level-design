import unittest
from unittest.mock import patch

from adapter.social_media.src.services.social_media_adapter import SocialMediaAdapter
from adapter.social_media.src.services.facebook_adapter import FacebookAdapter
from adapter.social_media.src.services.twitter_adapter import TwitterAdapter


class TestSocialMediaAdapter(unittest.TestCase):

    @patch.multiple(SocialMediaAdapter, __abstractmethods__=set())
    def test_facebook_adapter(self):
        adapter = FacebookAdapter()
        user_id, time_stamp = 1, 123456789
        posts = adapter.get_posts(user_id, time_stamp)
        self.assertEqual(posts[0].text, "FB Post")
        self.assertEqual(posts[0].id, "1")
        self.assertEqual(posts[0].user_id, 1)

    @patch.multiple(SocialMediaAdapter, __abstractmethods__=set())
    def test_twitter_adapter(self):
        adapter = TwitterAdapter()
        user_id, time_stamp = 1, 123456789
        posts = adapter.get_posts(user_id, time_stamp)
        self.assertEqual(posts[0].text, "Second Tweet")
        self.assertEqual(posts[0].id, "2")
        self.assertEqual(posts[0].user_id, 2)


if __name__ == '__main__':
    unittest.main()
