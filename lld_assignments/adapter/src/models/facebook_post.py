from dataclasses import dataclass
import datetime


@dataclass
class FacebookPost:
    id: str
    status: str
    user_id: int
    time_stamp: datetime
