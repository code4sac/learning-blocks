# Utilities and Shared Libraries

> [!WARNING]  
> Utilities folder needs to be cleaned up.

The utilities folder is a place for general-purpose typescript code that is used throughout the application. It includes
backend and frontend code.

- Wrappers for third-party libraries. Uses facade pattern.

## Facade Pattern

The Facade Pattern provides a simplified interface to a complex subsystem. It hides the complexities of the system and
provides an easy-to-use interface for the client. This pattern is particularly useful when working with third-party
libraries, as it allows you to create a unified API that is easier to work with and maintain.

## Utility Pattern

The Utility Pattern involves creating reusable functions or classes that perform common tasks. These utilities are
designed to be stateless and independent, making them easy to test and maintain. They help in reducing code duplication
and improving code organization.
