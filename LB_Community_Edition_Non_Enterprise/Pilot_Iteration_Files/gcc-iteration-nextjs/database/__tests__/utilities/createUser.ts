import { LibSQLDatabase } from "drizzle-orm/libsql";

export async function createUser(db: LibSQLDatabase<typeof import("../../schema")>, userData) {
    const createdUser = await db.insert(events).values(userData)

    return createdUser
}