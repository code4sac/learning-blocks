import { db } from '@/utility/db'
import { createEvent } from '@/service/drizzle/utilities/createEvent'
import { afterAll, beforeAll, describe, expect, test } from 'vitest'

const exampleUser = {
  email: 'user7@example.com',
  password: 'vNPFeBSQ+2rKtuZtTw==',
}

const exampleEvent = {
  name: 'Test Event 9',
  startOn: new Date().toUTCString(),
  createdById: exampleUser.email,
}

/**
 * Create event, which requires a user to be associated with it.
 */
describe('Create Event', {}, () => {
  beforeAll(async () => {})

  test('Create Event', async () => {
    const createdEvent = await createEvent(db, exampleEvent)
    expect(createdEvent).toBeDefined()
    expect(createdEvent.event.name).toBe(exampleEvent.name)
    expect(createdEvent.event.startOn).toEqual(exampleEvent.startOn)
    expect(createdEvent.event.createdById).toBe(exampleEvent.createdById)
  })
})
