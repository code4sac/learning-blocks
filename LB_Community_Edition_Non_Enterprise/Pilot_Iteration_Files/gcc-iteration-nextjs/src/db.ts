import { loadEnvConfig } from '@next/env'
import { drizzle } from 'drizzle-orm/libsql'
import { createClient } from '@libsql/client'
import * as schema from '@/services/drizzle/schema'

// Set the environment variables that are used by the Drizzle client.
// Use @next/env instead of dotenv package.
// TODO (Feature): Use development environment variables by default.
const projectDir = process.cwd()
loadEnvConfig(projectDir)

const client = createClient({
  url: process.env.TURSO_CONNECTION_URL!,
  authToken: process.env.TURSO_AUTH_TOKEN!,
})

export const db = drizzle(client, { schema })
