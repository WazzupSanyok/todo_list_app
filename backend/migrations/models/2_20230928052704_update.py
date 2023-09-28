from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX "uid_user_usernam_9987ab" ON "user" ("username");
        CREATE UNIQUE INDEX "uid_user_email_1b4f1c" ON "user" ("email");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_user_email_1b4f1c";
        DROP INDEX "idx_user_usernam_9987ab";"""
