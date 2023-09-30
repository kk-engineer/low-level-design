from .quality_adjustment_strategy import QualityAdjustmentStrategy
from ..models.video_quality import VideoQuality
from ..models.video_codec import VideoCodec
from ..models.video import Video


class MediumVideoAdjustmentStrategy(QualityAdjustmentStrategy):

    def supports_type(self) -> VideoQuality:
        return VideoQuality.MEDIUM

    def adjust(self, video: Video) -> Video:
        video.set_video_codec(VideoCodec.H265)
        video.set_bit_rate(1000)
        return video
