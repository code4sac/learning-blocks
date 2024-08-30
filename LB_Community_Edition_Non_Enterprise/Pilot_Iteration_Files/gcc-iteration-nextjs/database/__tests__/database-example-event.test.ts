import { db } from '../db'
import { afterAll, beforeAll, describe, expect, test } from 'vitest'
import { createEvent } from '@/database/__tests__/utilities/createEvent'
import { createUser } from '@/database/__tests__/utilities/createUser'

const exampleUser = {
  email: 'admin@example.com',
  password: 'vNPFeBSQ+2rKtuZtTw==',
}

const exampleEvent = {
  name: 'Test Event',
  startOn: new Date().toUTCString(),
  createdById: exampleUser.email,
}

/**
 * Create event, which requires a user to be associated with it.
 */
describe('Create event with user.', {}, () => {
  beforeAll(async () => {
    await createUser(db, exampleUser)
  })

  afterAll(async () => {
    // TODO: Delete the user and events.
  })

  test('Create User', async () => {
    const createdUser = await createEvent(db, exampleUser)
    expect(createdUser).toBeDefined()
    expect(createdUser.email).toBe(exampleUser.email)
    expect(createdUser.password).toEqual(exampleUser.password)
  })

  test('Create Event', async () => {
    const createdEvent = await createEvent(db, exampleEvent)
    expect(createdEvent).toBeDefined()
    expect(createdEvent.name).toBe(exampleEvent.name)
    expect(createdEvent.startOn).toEqual(exampleEvent.startOn)
    expect(createdEvent.createdById).toBe(exampleEvent.createdById)
  })
})
