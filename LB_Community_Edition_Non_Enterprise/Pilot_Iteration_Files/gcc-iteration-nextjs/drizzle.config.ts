import type { Config } from 'drizzle-kit'

export default {
  dialect: 'sqlite',
  schema: './src/service/drizzle/schema.ts',
  out: './src/service/drizzle/migrations',
  driver: 'turso',
  dbCredentials: {
    url: process.env.TURSO_CONNECTION_URL!,
    authToken: process.env.TURSO_AUTH_TOKEN!,
  },
  verbose: true,
  strict: true,
} satisfies Config
