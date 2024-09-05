import { db } from '../db'
import { afterAll, beforeAll, describe, expect, test } from 'vitest'
import { createEvent } from '@/database/__tests__/utilities/createEvent'

const exampleUser = {
  email: 'user6@example.com',
  password: 'vNPFeBSQ+2rKtuZtTw==',
}

const exampleEvent = {
  name: 'Test Event 8',
  startOn: new Date().toUTCString(),
  createdById: exampleUser.email,
}

/**
 * Create event, which requires a user to be associated with it.
 */
test('Create Event', async () => {
  const createdEvent = await createEvent(db, exampleEvent)
  expect(createdEvent).toBeDefined()
  expect(createdEvent.event.name).toBe(exampleEvent.name)
  expect(createdEvent.event.startOn).toEqual(exampleEvent.startOn)
  expect(createdEvent.event.createdById).toBe(exampleEvent.createdById)
})
