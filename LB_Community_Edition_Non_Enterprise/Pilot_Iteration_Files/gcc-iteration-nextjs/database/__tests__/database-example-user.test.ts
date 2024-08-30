import { db } from '../db'
import { afterAll, beforeAll, describe, expect, test } from 'vitest'
import { createEvent } from '@/database/__tests__/utilities/createEvent'
import { createUser } from '@/database/__tests__/utilities/createUser'

const exampleUser = {
    email: "user@example.com",
    password: "vNPFeBSQ+2rKtuZtTw==",
}

/**
 * Create user.
 */
test('Create User', async () => {
    const createdUser = await createUser(db, exampleUser)
    expect(createdUser).toBeDefined()
    expect(createdUser.email).toBe(exampleUser.email)
    expect(createdUser.password).toEqual(exampleUser.password)
})