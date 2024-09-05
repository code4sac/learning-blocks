import { db } from '../db'
import { afterAll, beforeAll, describe, expect, test } from 'vitest'
import { createTestUser } from '@/database/__tests__/utilities/createUser'

const exampleUser = {
  email: 'user6@example.com',
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
