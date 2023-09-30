from .social_media_adapter import SocialMediaAdapter
import datetime
from ..models.social_media_post import SocialMediaPost
from ..models.facebook_post import FacebookPost
from ..external.facebook_api import FacebookApi


class FacebookAdapter(SocialMediaAdapter):

    def __init__(self):
        self._facebook_api = FacebookApi()

    @staticmethod
    def to_social_media_post(post: FacebookPost) -> SocialMediaPost:
        return SocialMediaPost(post.id, post.status, post.user_id, post.time_stamp)

    def get_posts(self, user_id: int, time_stamp: datetime) -> list[SocialMediaPost]:
        fb_posts = self._facebook_api.fetch_facebook_posts(user_id, time_stamp)
        sm_posts = [FacebookAdapter.to_social_media_post(post) for post in fb_posts]
        return sm_posts

    def post(self, user_id: int, message: str):
        self._facebook_api.post_facebook_status(user_id, message)
