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
    // Connect to the database before running the tests
    await db.connect();
  });

  afterAll(async () => {
    // Disconnect from the database after running the tests
    await db.disconnect();
  });

  beforeEach(async () => {
    // Clear the database before each test
    await events.deleteMany({});
    await attendees.deleteMany({});
    await rsvps.deleteMany({});
  });

  test("Create Event", async () => {
    const eventData = {
      title: "Test Event",
      date: new Date(),
      location: "Test Location",
    };

    const createdEvent = await events.create(eventData);

    expect(createdEvent).toBeDefined();
    expect(createdEvent.title).toBe(eventData.title);
    expect(createdEvent.date).toEqual(eventData.date);
    expect(createdEvent.location).toBe(eventData.location);
  });

  test("Get All Events", async () => {
    const eventData = [
      {
        title: "Event 1",
        date: new Date(),
        location: "Location 1",
      },
      {
        title: "Event 2",
        date: new Date(),
        location: "Location 2",
      },
    ];

    await events.create(eventData[0]);
    await events.create(eventData[1]);

    const allEvents = await events.getAll();

    expect(allEvents).toHaveLength(2);
    expect(allEvents[0].title).toBe(eventData[0].title);
    expect(allEvents[1].title).toBe(eventData[1].title);
  });

  // Add more tests here...
});
```
