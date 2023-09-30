from .quality_adjustment_strategy import QualityAdjustmentStrategy
from ..models.video_quality import VideoQuality
from ..models.video_codec import VideoCodec
from ..models.video import Video


class HighVideoAdjustmentStrategy(QualityAdjustmentStrategy):

    def supports_type(self) -> VideoQuality:
        return VideoQuality.HIGH

    def adjust(self, video: Video) -> Video:
        video.set_video_codec(VideoCodec.VP9)
        video.set_bit_rate(2000)
        return video
