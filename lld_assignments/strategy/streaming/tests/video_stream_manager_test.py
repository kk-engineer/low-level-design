import unittest
from unittest.mock import patch

from ..src.models.video_quality import VideoQuality
from ..src.models.video_codec import VideoCodec
from ..src.models.video import Video
from ..src.strategies.quality_adjustment_strategy import QualityAdjustmentStrategy
from ..src.strategies.low_adjustment_strategy import LowVideoAdjustmentStrategy
from ..src.strategies.medium_adjustment_strategy import MediumVideoAdjustmentStrategy
from ..src.strategies.high_adjustment_strategy import HighVideoAdjustmentStrategy
from ..src.services.video_streaming_manager import VideoStreamingManager


class TestVideoStreamManager(unittest.TestCase):

    @patch.multiple(QualityAdjustmentStrategy, __abstractmethods__=set())
    def test_low_streaming_strategy(self):
        strategy = LowVideoAdjustmentStrategy()
        video_url = "scaler.com/video_low"
        video_quality = strategy.supports_type()
        video = Video(video_url, video_quality)
        manager = VideoStreamingManager(video, strategy)
        adjusted_video = manager.stream_video()

        self.assertEqual(adjusted_video.get_video_quality(), VideoQuality.LOW, "If the strategy pattern is "
                                                                               "implemented correctly, "
                                                                               "the video quality should be LOW.")

        self.assertEqual(adjusted_video.get_video_codec(), VideoCodec.H264, "If the strategy pattern is implemented "
                                                                            "correctly, the codec should be H264 for "
                                                                            "low quality videos.")

        self.assertEqual(adjusted_video.get_bit_rate(), 500, "If the strategy pattern is implemented correctly, "
                                                             "the bit rate should be 500 for high quality videos.")

    @patch.multiple(QualityAdjustmentStrategy, __abstractmethods__=set())
    def test_medium_streaming_strategy(self):
        strategy = MediumVideoAdjustmentStrategy()
        video_url = "scaler.com/video_medium"
        video_quality = strategy.supports_type()
        video = Video(video_url, video_quality)
        manager = VideoStreamingManager(video, strategy)
        adjusted_video = manager.stream_video()

        self.assertEqual(adjusted_video.get_video_quality(), VideoQuality.MEDIUM, "If the strategy pattern is "
                                                                                  "implemented correctly, "
                                                                                  "the video quality should be MEDIUM.")

        self.assertEqual(adjusted_video.get_video_codec(), VideoCodec.H265, "If the strategy pattern is implemented "
                                                                           "correctly, the codec should be H265 for "
                                                                           "medium quality videos.")

        self.assertEqual(adjusted_video.get_bit_rate(), 1000, "If the strategy pattern is implemented correctly, "
                                                              "the bit rate should be 1000 for high quality videos.")

    @patch.multiple(QualityAdjustmentStrategy, __abstractmethods__=set())
    def test_high_streaming_strategy(self):
        strategy = HighVideoAdjustmentStrategy()
        video_url = "scaler.com/video_high"
        video_quality = strategy.supports_type()
        video = Video(video_url, video_quality)
        manager = VideoStreamingManager(video, strategy)
        adjusted_video = manager.stream_video()

        self.assertEqual(adjusted_video.get_video_quality(), VideoQuality.HIGH, "If the strategy pattern is "
                                                                                "implemented correctly, "
                                                                                "the video quality should be HIGH.")

        self.assertEqual(adjusted_video.get_video_codec(), VideoCodec.VP9, "If the strategy pattern is implemented "
                                                                           "correctly, the codec should be VP9 for "
                                                                           "high quality videos.")

        self.assertEqual(adjusted_video.get_bit_rate(), 2000, "If the strategy pattern is implemented correctly, "
                                                              "the bit rate should be 2000 for high quality videos.")


if __name__ == '__main__':
    unittest.main()
