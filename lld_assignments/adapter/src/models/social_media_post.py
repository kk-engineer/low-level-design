from dataclasses import dataclass
import datetime


@dataclass
class SocialMediaPost:
    id: str
    text: str
    user_id: int
    time_stamp: datetime
