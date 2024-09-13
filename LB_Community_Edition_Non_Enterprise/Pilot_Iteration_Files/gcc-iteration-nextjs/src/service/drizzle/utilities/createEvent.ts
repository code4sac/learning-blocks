import { LibSQLDatabase } from 'drizzle-orm/libsql'

import { events } from '@/service/drizzle/schema'

export async function createEvent(
  db: LibSQLDatabase<typeof import('../schema')>,
  eventData,
) {
  let rows = await db
    .insert(events)
    .values({
      name: eventData.name,
      startOn: eventData.startOn,
      createdById: eventData.createdById,
      status: 'draft',
    })
    .returning({
      id: events.id,
      name: events.name,
      startOn: events.startOn,
      createdById: events.createdById,
    })

  let event = rows[0]

  return { event }
}
