import asyncpg
from dotenv import load_dotenv
from os import getenv

load_dotenv()

async def execsql(query: str):
    pool = await asyncpg.create_pool(
        database = getenv('ENV_POSTGRES_DB'),
        user = getenv('ENV_POSTGRES_USER'),
        password = getenv('ENV_POSTGRES_PASSWORD'),
        port = getenv('ENV_POSTGRES_PORT')
    )

    async with pool.acquire() as conn:
        result = await conn.fetch(query)
    
    await pool.close()

    return result
