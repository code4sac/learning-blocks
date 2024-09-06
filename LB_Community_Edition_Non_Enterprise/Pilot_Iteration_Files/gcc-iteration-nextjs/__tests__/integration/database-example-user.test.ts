import { db } from '@/db'
import { createTestUser } from '@/services/drizzle/utilities/user'
import { afterAll, beforeAll, describe, expect, test } from 'vitest'

const exampleUser = {
  email: 'user7@example.com',
  password: 'vNPFeBSQ+2rKtuZtTw==',
}

/**
 * Test user creation in the database.
 */
test('User email', async () => {
  const createdUser = await createTestUser(exampleUser)
  expect(createdUser).toBeDefined()
  expect(createdUser.user.email).toBe(exampleUser.email)
})
// Todo: Test hashed password by reading it from the database.
// test('User password', async () => {

// })
