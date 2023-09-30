from .video_codec import VideoCodec
from .video_quality import VideoQuality


class Video:
    def __init__(self, video_url, video_quality):
        self._video_url = video_url
        self._video_quality = video_quality
        self._video_codec = None
        self._bit_rate = None

    # Getter/Setter
    def get_video_quality(self):
        return self._video_quality

    def get_video_codec(self):
        return self._video_codec

    def set_video_codec(self, video_codec):
        self._video_codec = video_codec

    def get_bit_rate(self):
        return self._bit_rate

    def set_bit_rate(self, bit_rate):
        self._bit_rate = bit_rate

    """
    @property
    def video_quality(self):
        return self._video_quality

    @video_quality.setter
    def video_quality(self, value):
        self._video_quality = value

    @property
    def video_codec(self):
        return self._video_codec

    @video_codec.setter
    def video_codec(self, value):
        self._video_codec = value

    @property
    def bit_rate(self):
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, value):
        self._bit_rate = value
    """

