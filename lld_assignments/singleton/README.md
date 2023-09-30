# Logger

## Problem Statement

You are tasked with developing a logging module for a complex software application. The logging module needs to maintain a single log file throughout the application's execution to avoid file access conflicts and ensure consistency. To prevent multiple instances of the logging module and ensure thread-safe access to the log file, you need to implement the Singleton design pattern along with the logging functionality.

## Assignment

Your task is to implement the `Logger` interface that follows the Singleton design pattern to manage logging operations and maintain a single log file.
### Part 1: Implementing Singleton and Logger

1. **Implement the Singleton design pattern**: Create a class that implements the `Logger` interface. Implement the Singleton design pattern within this class to ensure that only one instance of the logger can exist within the program.

2. **Implement the `getInstance()` and `resetInstance()` methods**: Implement the `getInstance()` method in the `LoggerSolution` class. This method should return the singleton instance of the logger class. Also, implement the `resetInstance()` method to reset the singleton instance to `null`.

### Part 2: Logging Operations

The logger module is responsible for recording log messages of different levels in a single log file. Think of it as a central place where various parts of your software can write messages for debugging or monitoring purposes.

You have to implement the following methods:
- `void setLogFile(String filePath)`: This method sets the log file path. The logger will write log messages to this file. Look at using the `java.io.PrintWriter` and `java.io.FileWriter` classes to write to the log file. You can initialise them in this method.
- `void log(LogLevel level, String message)`: This method is responsible for logging a message with a specified log level. The log message should include a timestamp, log level, and the provided message. Throw an `IllegalStateException` if the logger is not initialised using the `setLogFile()` method.
- `String getLogFile()`: This method returns the current log file path.
- `void flush()`: This method flushes any buffered log entries to the log file. Find the appropriate method to use from the `java.io.PrintWriter` class.
- `void close()`: This method closes the logger and releases any resources. Find the appropriate method to use from the `java.io.PrintWriter` class.

### Instructions

1. Clone this repository to your local machine.
2. Implement the `Logger` interface and the required methods as specified above.
3. Ensure that your implementation follows the Singleton design pattern and provides proper logging functionality.
4. Run the provided test cases in the `LoggerTest` class to verify the correctness of your implementation.
