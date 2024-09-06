# Tests

## **tests** Folder

The `__tests__` folder is a convention used in Next.js projects to organize test files. This folder typically contains
unit tests, integration tests, and end-to-end (E2E) tests. By following this convention, you can keep your test files
separate from your application code, making the project structure cleaner and more maintainable.

### Types of Tests

- **Unit Tests**: Test individual components or functions in isolation.
- **Integration Tests**: Test the interaction between multiple components or modules.
- **End-to-End (E2E) Tests**: Test the entire application flow from start to finish.

### Benefits

- **Organized Structure**: Keeps test files separate from application code.
- **Maintainability**: Easier to manage and locate test files.
- **Consistency**: Follows common conventions, making it easier for new developers to understand the project structure.

## Unit Testing Pattern

Unit testing involves testing individual components or functions in isolation to ensure they work as expected. This type
of testing is essential for verifying the correctness of the smallest parts of your application.

### Benefits

- **Early Bug Detection**: Identifies issues at an early stage in the development cycle.
- **Simplifies Debugging**: Easier to pinpoint the source of a problem.
- **Improves Code Quality**: Encourages writing modular and maintainable code.
- **Facilitates Refactoring**: Provides confidence when making changes to the codebase.

### Unit Testing with Next.js Components

When unit testing Next.js components, you typically use a testing library like Jest along with a utility like React
Testing Library to render components and make assertions.

## Integration Testing Pattern

Integration testing involves testing the interaction between multiple components or modules to ensure they work together
as expected. This type of testing helps identify issues that may arise when different parts of the application are
combined.

### Benefits

- **Detects Interface Issues**: Ensures that components or modules interact correctly.
- **Improves Reliability**: Validates the integration points, reducing the risk of bugs.
- **Early Detection**: Identifies issues early in the development cycle, making them easier to fix.

## End-to-End (E2E) Testing Pattern

End-to-End (E2E) testing involves testing the entire application flow from start to finish. This type of testing ensures
that all integrated components of an application work together as expected. E2E tests simulate real user scenarios,
providing confidence that the system meets business requirements and user expectations.

### Benefits

- **Comprehensive Coverage**: Validates the entire application workflow.
- **User-Centric**: Simulates real user interactions.
- **Early Detection**: Identifies integration issues early in the development cycle.

### Tools

Common tools for E2E testing include:

- **Cypress**
- **Selenium**
- **Playwright**

## Get started with the database

Database tests.

> [!IMPORTANT]  
> The database is currently using example data. Once we have a better understanding of the data we will update the database schema and drop the example tables.

### Example

```typescript
import { db } from "@/database/db";
import { events, attendees, rsvps } from "@/database/schema";
import {
  afterAll,
  beforeAll,
  beforeEach,
  describe,
  expect,
  test,
} from "vitest";

describe("Database Tests", () => {
  beforeAll(async () => {
  });

  afterAll(async () => {
  });

  beforeEach(async () => {
  });

  test("Example test", async () => {
  });
```
