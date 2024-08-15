import logging
from typing import List

from aiohttp import web

from app.db.connection import get_db_pool
from app.models.city import City


async def delete_city(city_id: int, app: web.Application):
    pool = await get_db_pool(app)
    try:
        async with pool.acquire() as connection:
            async with connection.transaction():
                query = "DELETE FROM cities WHERE id = $1"
                await connection.execute(query, city_id)

    except Exception as e:
        logging.error(f"Error deleting city with ID {city_id}: {e}")


async def get_city(city_id: int, app: web.Application) -> City | None:
    pool = await get_db_pool(app)
    try:
        async with pool.acquire() as connection:
            async with connection.transaction():
                query = "SELECT name, country, population, latitude, longitude, is_capital FROM cities WHERE id = $1"
                row = await connection.fetchrow(query, city_id)

                return City(**row) if row else None
    except Exception as e:
        logging.error(f"Error retrieving city with ID {city_id}: {e}")
        return None


async def retrieve_cities(app: web.Application) -> List[City]:
    pool = await get_db_pool(app)
    try:
        async with pool.acquire() as connection:
            async with connection.transaction():
                query = "SELECT name, country, population, latitude, longitude, is_capital FROM cities"
                rows = await connection.fetch(query)
                cities = [City(**row) for row in rows]
        return cities
    except Exception as e:
        logging.error(f"Error retrieving cities: {e}")
        return []


async def store_cities(cities: List[City], app: web.Application):
    pool = await get_db_pool(app)
    async with pool.acquire() as connection:
        async with connection.transaction():
            for city in cities:
                try:
                    await connection.execute("""
                    INSERT INTO cities (name, country, population, latitude, longitude, is_capital)
                    VALUES ($1, $2, $3, $4, $5, $6)
                    ON CONFLICT (name) DO NOTHING
                    """, city.name, city.country, city.population, city.latitude, city.longitude, city.is_capital)
                except Exception as e:
                    logging.error(f"Error storing city {city.name}: {e}")
                    continue
