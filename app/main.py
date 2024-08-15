import logging

from aiohttp import web

from app.config import settings
from app.db.connection import pg_context
from app.routes import setup_routes


async def create_app():
    app = web.Application()

    config = settings
    app['config'] = config

    app.cleanup_ctx.append(pg_context)

    setup_routes(app)

    return app


def main():
    logging.basicConfig(level=settings.LOGGING_LEVEL)

    app = create_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
