import asyncpg
from aiohttp import web


async def pg_context(app: web.Application):
    config = app['config']
    app['db_pool'] = await asyncpg.create_pool(
        dsn=str(config.DATABASE_URI),
        min_size=1,
        max_size=10,
    )
    yield
    await app['db_pool'].close()


async def close_db(app: web.Application):
    await app['db_pool'].close()


async def get_db_pool(app: web.Application):
    return app['db_pool']
