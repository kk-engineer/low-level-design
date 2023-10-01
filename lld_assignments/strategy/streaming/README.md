                                                                                                                                                # Strategy Pattern for Video Streaming Quality Adjustment

## Problem Statement
You are developing a video streaming platform that offers different streaming qualities, such as low, standard, and high definition. The platform should dynamically adjust the streaming quality based on the user's network conditions to ensure smooth playback. Additionally, more quality adjustment algorithms may be added in the future. Your task is to implement this dynamic quality adjustment system using the Strategy pattern.

## Assignment
Your assignment is to implement the Strategy pattern to create strategies for adjusting video streaming quality. The existing code provides a starting point, but you need to complete the implementation.

### Task 1: Implement Strategy Interface
1. Use the existing `QualityAdjustmentStrategy` interface, which defines the `supportsType` method that returns the `VideoQuality` supported by the strategy.
2. Add a new method `adjust` to the `QualityAdjustmentStrategy` interface that accepts a `Video` object and returns a modified `Video` object with adjusted quality settings.

### Task 2: Implement Concrete Strategies
1. Create three concrete strategy classes, each corresponding to a different video quality (LOW, MEDIUM, HIGH). Implement the `supportsType` method to return the supported quality.
2. Implement the `adjust` method for each concrete strategy to adjust the `Video` object's quality settings based on the quality level. Copy the implementation code from the original `VideoStreamingManager` class.

### Task 3: Update `VideoStreamingManager`
1. Modify the `VideoStreamingManager` class to accept a `QualityAdjustmentStrategy` object in the constructor.
2. Implement the `streamVideo` method in the `VideoStreamingManager` class to use the provided strategy to adjust the video's quality settings.

## Testing Instructions
1. Ensure that you have implemented the Strategy pattern correctly by passing the provided test cases in the `TestVideoStreamManager` class.
2. The test cases validate that there are three concrete strategies, that the `QualityAdjustmentStrategy` interface has the required methods, and that the `VideoStreamingManager` class is correctly updated to use the strategy for quality adjustment.
3. Make sure that the `adjust` method in each strategy class correctly adjusts the video's quality settings based on the supported quality.

`Important`: Use PyCharm IDE to run the test cases, else you may get the following error when you run the tests - `ImportError: attempted relative import with no known parent package`

Remember to refactor the existing code to use the Strategy pattern and ensure that your tests pass successfully. Good luck with your assignment!