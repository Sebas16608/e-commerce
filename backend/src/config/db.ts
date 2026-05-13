import "dotenv/config";
import path from "path";
import { PrismaClient } from "../generated/prisma";
import { PrismaLibSql } from "@prisma/adapter-libsql";

const globalForPrisma = globalThis as unknown as { prisma: PrismaClient | undefined };

const dbPath = process.env.DATABASE_URL?.replace("file:", "") ?? "./dev.db";

const adapter = new PrismaLibSql({ url: `file://${path.resolve(dbPath)}` });

export const prisma = globalForPrisma.prisma ?? new PrismaClient({ adapter });

if (process.env.NODE_ENV !== "production") {
  globalForPrisma.prisma = prisma;
}
