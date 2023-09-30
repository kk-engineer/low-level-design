from ..models.facebook_post import FacebookPost
from .api_utils import ApiUtils
import datetime


class FacebookApi:

    def fetch_facebook_posts(self, user_id: int, time_stamp: datetime) -> list[FacebookPost]:
        # Implementation to fetch Facebook posts
        ApiUtils.log_facebook_get_posts()
        fb_post = FacebookPost("1", "Hello World", 1, 123456789)
        return [fb_post]

    def post_facebook_status(self, user_id: int, status: str):
        # Implementation to post a status on Facebook
        ApiUtils.log_facebook_post_status()