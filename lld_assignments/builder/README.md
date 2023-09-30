# Builder Pattern Implementation for Building Queries

## Problem Statement

You are tasked with developing a database management system that involves creating and executing SQL queries. Queries can vary in complexity, involving different SELECT clauses, JOIN operations, WHERE conditions, and more. The current approach of constructing queries using concatenated strings has proven to be error-prone, difficult to read, and challenging to modify. You should implement the Builder pattern to create instances of query objects with various configurations, resulting in more maintainable and flexible code.

## Assignment

Your task is to implement the Builder pattern to construct query objects with different configurations. The Builder pattern facilitates the step-by-step construction of complex objects while keeping the creation process separate from the main object.

## Implementing the Builder Pattern

1. **Review the original class**: You have been provided with a class named `Query`. This class represents SQL queries with different components. Your task is to implement the Builder pattern to create instances of a class with the same properties.

2. **Create the builder class**: Develop a new class called `QueryBuilder` that will implement the Builder pattern for creating query instances. A starter class has been given for you to begin with. Don't forget to annotate the class with the `@WithBuilder` annotation. The actual name of the class doesn't matter, as long as it is annotated.
3. **Test your implementation**: Test cases have been provided for you to verify the correctness of your implementation. Execute the test cases to ensure the accuracy of your code.

## Instructions
1. Clone this repository to your local machine.
2. Create a new class annotated with the `@WithBuilder` annotation.
3. Implement the builder pattern within your `QueryBuilder` class.
4. Run the provided test cases in the `QueryBuilderTest` class to validate the correctness of your implementation.
