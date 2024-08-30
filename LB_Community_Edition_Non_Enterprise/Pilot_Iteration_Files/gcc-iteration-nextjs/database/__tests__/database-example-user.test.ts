import { db } from "../db";
import { afterAll, beforeAll, describe, expect, test } from "vitest";
import { createEvent } from "@/database/__tests__/utilities/createEvent";
import { createUser } from "@/database/__tests__/utilities/createUser";

const exampleUser = {
  email: "user6@example.com",
  password: "vNPFeBSQ+2rKtuZtTw==",
};

/**
 * Test user creation in the database.
 */
describe("Create user", {}, () => {
  test("User email", async () => {
    const createdUser = await createUser(db, exampleUser);
    expect(createdUser).toBeDefined();
    expect(createdUser.user.email).toBe(exampleUser.email);
  });
  // Todo: Test hashed password by reading it from the database.
  // test('User password', async () => {

  // })
});
