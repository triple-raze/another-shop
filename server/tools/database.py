import asyncpg
from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()

async def execsql(query: str, args: tuple = (), as_list=False, first=False,):
    
    pool = await asyncpg.create_pool(
        database = getenv('ENV_POSTGRES_DB'),
        user = getenv('ENV_POSTGRES_USER'),
        password = getenv('ENV_POSTGRES_PASSWORD'),
        port = getenv('ENV_POSTGRES_PORT')
    )

    async with pool.acquire() as conn:
        result = await conn.fetch(query, *args)
        
        if as_list:
            result = [list(item.values()) for item in result]
        else:
            result = [dict(row) for row in result]

    await pool.close()

    if not result:
        if as_list: return []
        if not as_list: return {}

    if first:
        result = result[0]

    return result
