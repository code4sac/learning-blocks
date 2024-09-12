import { sqliteTursoDb } from '@/service/drizzle/sqliteTursoDb'

// Load the SQLite database client that is connected to the Turso database.
export const db = sqliteTursoDb
