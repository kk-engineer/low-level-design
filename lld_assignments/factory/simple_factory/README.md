# Simple Factory Pattern for Notification System

## Problem Statement

You are designing a notification system. Depending on the type of notification (e.g., email, SMS, push notification), different notification routines are required. You need a way to create notifications without explicitly specifying their classes, ensuring the system is open for future notification types.

## Assignment

Your task is to implement the Simple Factory pattern to create notifications in the notification system. The Simple Factory pattern provides a way to create objects without exposing the instantiation logic, allowing for easy addition of new notification types.

### Task 1 - Creating a Common Parent Class - Product Hierarchy

To streamline the creation of notifications, implement the common parent class named `Notification`. This class should include attributes and methods that are common to all notifications. The method `notificationType` has already been abstracted out for you as an example. You will need to implement the `Notification` class as a common parent class for all notifications.

### Task 2 - Implementing the Simple Factory

Implement a `NotificationFactory` class that follows the Simple Factory pattern. This class should have a method to create notifications based on the `NotificationType`. The factory class should be capable of creating different types of notifications based on the `NotificationType`. Also remember that to create a notification, you need to pass the recipient, message and sender as parameters as well.

### Instructions

1. Implement the `Notification` class as a common parent class for all notifications. Include attributes and methods that are common to all notifications.

2. Implement the `NotificationFactory` class that implements the Simple Factory pattern. Add a method to create notifications based on `NotificationType` and other parameters.

3. Run the provided test cases in the `NotificationTest` class to verify the correctness of your implementation. The tests will check if all notifications have a common parent class and if the factory class can correctly create notifications based on the notification type, recipient, and message.