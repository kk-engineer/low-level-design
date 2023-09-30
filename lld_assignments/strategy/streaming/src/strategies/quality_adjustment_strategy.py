from abc import ABC, abstractmethod
from ..models.video_quality import VideoQuality
from ..models.video import Video


class QualityAdjustmentStrategy(ABC):

    @abstractmethod
    def supports_type(self) -> VideoQuality:
        ...

    @abstractmethod
    def adjust(self, video: Video) -> Video:
        ...
