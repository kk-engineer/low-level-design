from ..models.video import Video
from ..strategies.quality_adjustment_strategy import QualityAdjustmentStrategy


class VideoStreamingManager:

    def __init__(self, video: Video, quality_adjustment_strategy: QualityAdjustmentStrategy):
        self._video = video
        self._quality_adjustment_strategy = quality_adjustment_strategy

    def stream_video(self):
        return self._quality_adjustment_strategy.adjust(self._video)

