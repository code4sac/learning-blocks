import { relations } from 'drizzle-orm'
import { integer, sqliteTable, text, unique } from 'drizzle-orm/sqlite-core'
import {
  boolean,
  createdAt,
  date,
  id,
} from '@/services/drizzle/schema/schemaFields'

export const students = sqliteTable('students', {
  id: id(),
  createdAt: createdAt(),
  email: text('email').unique().notNull(),
  password: text('password').notNull(),
})
