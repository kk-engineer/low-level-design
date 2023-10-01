                                                                                                                                        # Observer Pattern for Stock Trading Platform

## Problem Statement
You are developing a stock trading platform where users need to be notified whenever the price of a particular stock crosses a certain threshold. These notifications should be sent through various channels such as email, SMS, and mobile app notifications. To achieve this, you want to implement the Observer pattern, allowing users to subscribe to stock price updates and receive notifications through multiple channels.

## Assignment
Your task is to implement the Observer pattern to create a flexible notification system for the stock trading platform. The `StockTradingManager` class handles stock price updates, and various observer classes (e.g., `EmailService`, `SmsService`, `AppService`) need to be notified when the stock price crosses the threshold.

## Implementing the Observer Pattern

1. **Review the original class**: Study the `StockTradingManager` class and its dependencies. Understand how it currently handles stock price updates and notifications.

2. **Implement the publisher abstract class**: You have been provided with a `Publisher` abstract class. Your task is to implement the methods required by this class in the `StockTradingManager` class. Remember that the `Publisher` class is a contract that defines the methods that a class can use to notify observers. Implement the `ObserverRegistry` in the `Publisher` class.

3. **Implement the observer interface**: Design an interface named `Observer` with a method that accepts the stock name and current price as arguments. Observer classes (such as `EmailService`, `SmsService`, `AppService`) will implement this interface to receive notifications.

4. **Modify the publisher**: Refactor the `StockTradingManager` class as required. **Do not modify the constructor** as it used by the tests.

5. **Modify the observers**: Refactor the observer classes to implement the `Observer` interface. Update their existing methods to match the new interface method signature.

6. **Test your implementation**: Run the provided test cases in the `StockTradingManagerTest` class to ensure that your observer pattern implementation is correct. These test cases will check if observers are being notified correctly and if the StockTradingManager behaves as expected.

## Instructions
1. Clone this repository to your local machine.
2. Implement the Observer pattern by completing the `Publisher` and `Observer` interface and modifying the observer classes (`EmailService`, `SmsService`, `AppService`) and the `StockTradingManager` class.
3. Run the provided test cases in the `TestStockTradingManager` class to verify the correctness of your observer pattern implementation.

`Important`: Use PyCharm IDE to run the test cases, else you may get the following error when you run the tests -
`ImportError: attempted relative import with no known parent package`