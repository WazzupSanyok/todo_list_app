from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME COLUMN "mail" TO "email";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME COLUMN "email" TO "mail";"""
