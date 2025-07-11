import asyncpg
from dotenv import load_dotenv
from os import getenv

load_dotenv()

async def execsql(query: str, args: tuple, first=False):
    
    pool = await asyncpg.create_pool(
        database = getenv('ENV_POSTGRES_DB'),
        user = getenv('ENV_POSTGRES_USER'),
        password = getenv('ENV_POSTGRES_PASSWORD'),
        port = getenv('ENV_POSTGRES_PORT')
    )

    async with pool.acquire() as conn:
        result = await conn.fetch(query, *args)
        result = [dict(row) for row in result]

    await pool.close()

    if first:
        result = result[0]

    return result
