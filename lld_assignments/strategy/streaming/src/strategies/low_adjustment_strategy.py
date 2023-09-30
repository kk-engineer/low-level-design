from .quality_adjustment_strategy import QualityAdjustmentStrategy
from ..models.video_quality import VideoQuality
from ..models.video_codec import VideoCodec
from ..models.video import Video


class LowVideoAdjustmentStrategy(QualityAdjustmentStrategy):

    def supports_type(self) -> VideoQuality:
        return VideoQuality.LOW

    def adjust(self, video: Video) -> Video:
        video.set_video_codec(VideoCodec.H264)
        video.set_bit_rate(500)
        return video
