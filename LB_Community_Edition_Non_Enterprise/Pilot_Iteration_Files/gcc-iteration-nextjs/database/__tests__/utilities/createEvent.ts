import { events } from "@/database/schema";
import { LibSQLDatabase } from "drizzle-orm/libsql";
import { integer, sqliteTable, text, unique } from 'drizzle-orm/sqlite-core'

export async function createEvent(db: LibSQLDatabase<typeof import("../../schema")>) {
    const createdEvent = await db.insert(events).values({
        name: "Example Event",
        startOn: new Date().toUTCString(),
        createdById: text('createdById').notNull(),
        description: text('description'),

        streetNumber: integer('streetNumber'),
        street: text('street'),
        zip: integer('zip'),
        bldg: text('bldg'),

        isPrivate: boolean('isPrivate').default(false).notNull(),
        status: text('status', {
            enum: ['draft', 'live', 'started', 'ended', 'canceled'],
        })
            .default('draft')
            .notNull(),
    })

    return createdEvent
}