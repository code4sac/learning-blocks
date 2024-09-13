import { sqliteTable, text } from 'drizzle-orm/sqlite-core'

import { createdAt, id } from '@/service/drizzle/schema/schemaFields'

export const students = sqliteTable('students', {
  id: id(),
  createdAt: createdAt(),
  email: text('email').unique().notNull(),
  password: text('password').notNull(),
})
