from abc import ABC, abstractmethod
import datetime
from ..models.social_media_post import SocialMediaPost


class SocialMediaAdapter(ABC):

    @abstractmethod
    def get_posts(self, user_id: int, time_stamp: datetime) -> list[SocialMediaPost]:
        ...

    @abstractmethod
    def post(self, user_id: int, message: str):
        ...
