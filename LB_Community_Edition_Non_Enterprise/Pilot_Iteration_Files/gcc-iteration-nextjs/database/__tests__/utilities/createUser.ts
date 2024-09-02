import { LibSQLDatabase } from "drizzle-orm/libsql";
import { eq } from "drizzle-orm";
import { users } from "@/database/schema";
import bcrypt from "bcrypt";
import { db } from "@/database/db";
import jwt from "jsonwebtoken";

const SECRET = "use_an_ENV_variable";

export const createTokenForUser = (userId: string) => {
  const token = jwt.sign({ id: userId }, SECRET);
  return token;
};

async function createTestUser({
  email,
  password,
}: {
  email: string;
  password: string;
}) {
  const hashedPW = await hashPW(password);
  const rows = await db
    .insert(users)
    .values({ email, password: hashedPW })
    .returning({
      id: users.id,
      email: users.email,
      createdAt: users.createdAt,
      password: users.password,
    });

  const user = rows[0];
  const token = createTokenForUser(user.id);

  return { user, token };
}

function hashPW(password: string) {
  return bcrypt.hash(password, 10);
}

export async function createUser(
  db: LibSQLDatabase<typeof import("../../schema")>,
  userData
) {
  const createdUser = await createTestUser(userData);

  return createdUser;
}
