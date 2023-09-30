from .social_media_adapter import SocialMediaAdapter
import datetime
from ..models.social_media_post import SocialMediaPost
from ..models.twitter_tweet import TwitterTweet
from ..external.twitter_api import TwitterApi


class TwitterAdapter(SocialMediaAdapter):
    def __init__(self):
        self._twitter_api = TwitterApi()

    @staticmethod
    def to_social_media_post(tweet: TwitterTweet) -> SocialMediaPost:
        return SocialMediaPost(tweet.id, tweet.tweet, tweet.user_id, None)

    def get_posts(self, user_id: int, time_stamp: datetime) -> list[SocialMediaPost]:
        tweets = self._twitter_api.get_tweets(user_id)
        sm_posts = [TwitterAdapter.to_social_media_post(tweet) for tweet in tweets]

    def post(self, user_id: int, message: str):
        self._twitter_api.tweet(user_id, message)
