from ..models.twitter_tweet import TwitterTweet
from .api_utils import ApiUtils


class TwitterApi:

    def get_tweets(self, user_id: int) -> list[TwitterTweet]:
        # Implementation to fetch Twitter tweets
        ApiUtils.log_twitter_get_posts()
        tweet = TwitterTweet("1", "First Tweet", 1)
        return [tweet]

    def tweet(self, user_id: int, text: str):
        # Implementation to send a tweet on Twitter
        ApiUtils.log_twitter_post_status()
