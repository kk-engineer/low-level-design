from dataclasses import dataclass


@dataclass
class TwitterTweet:
    id: str
    tweet: str
    user_id: int
