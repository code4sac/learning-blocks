import { randomUUID } from 'node:crypto'

import { sql } from 'drizzle-orm'
import { integer, text } from 'drizzle-orm/sqlite-core'

export const id = () =>
  text('id')
    .primaryKey()
    .$default(() => randomUUID())

export const createdAt = () =>
  text('created_at')
    .default(sql`CURRENT_TIMESTAMP`)
    .notNull()

export const date = (name: string) => text(name)

export const boolean = (field: string) => integer(field, { mode: 'boolean' })
