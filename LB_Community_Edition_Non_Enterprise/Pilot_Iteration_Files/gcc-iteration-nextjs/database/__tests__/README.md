# Get started with the database

Database tests.

> [!IMPORTANT]  
> The database is currently using example data. Once we have a better understanding of the data we will update the database schema and drop the example tables.

## Example

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
