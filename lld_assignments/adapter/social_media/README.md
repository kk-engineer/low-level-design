                                                                                                                                                                                                                                         # Adapter Pattern for Social Media Aggregator

## Problem Statement
You are working on a social media aggregator app that pulls in posts from various social platforms. Each platform provides data in different structures through distinct APIs. Your task is to unify the data format within the app and ensure that integrating new social platforms remains hassle-free. To achieve this, you want to implement the Adapter pattern, allowing you to create adapter classes for different social media platform APIs. These adapters will convert platform-specific APIs into a common format that your application can use.

## Assignment
Your goal is to implement the Adapter pattern to create adapter classes for different social media platform APIs. These adapters should conform to a common interface, making it easy to integrate new platforms in the future. Your task is to abstract away the differences in APIs and data formats and provide a unified interface for your application to work with.

## Implementing the Adapter Pattern

1. **Review the existing APIs**: Study the APIs and data formats of the social media platforms you need to integrate. Understand the differences in their APIs and how they interact with their respective systems.

2. **Implement the adapter interface**: You have been provided with a `SocialMediaAdapter` interface. Your task is to implement this interface in different adapter classes, each corresponding to a different social media platform. The adapters should adapt the provider-specific APIs into a format that matches the `SocialMediaAdapter` interface.

3. **Use composition**: Create adapter classes that internally use instances of the actual social media platform APIs. You should not modify the platform APIs directly. Instead, create methods in the adapter classes that map to the platform APIs and perform the necessary transformations.

4. **Test your implementation**: Run the provided test cases in the `SocialMediaAdapterTest` class to ensure that your adapter classes work correctly. These test cases will check if your adapters have the required methods and if they interact with the platform APIs properly.

## Instructions
1. Clone this repository to your local machine.
2. Implement the Adapter pattern by creating adapter classes that implement the `SocialMediaAdapter` interface and adapt the APIs of different social media platforms.
3. Run the provided test cases in the `TestSocialMediaAdapter` class to verify the correctness of your adapter pattern implementation. Make sure your adapters have the expected methods and interact with the platform APIs as required.

`Important`: Use PyCharm IDE to run the test cases, else you may get the following error when you run the tests - `ImportError: attempted relative import with no known parent package`