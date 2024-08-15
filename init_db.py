import asyncpg
import asyncio

from app.config import settings

CREATE_CITIES_TABLE = """
CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    population INTEGER,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    is_capital BOOLEAN,
    UNIQUE (name) 
);
"""


async def init_db():
    conn = await asyncpg.connect(str(settings.DATABASE_URI))
    try:
        await conn.execute(CREATE_CITIES_TABLE)
        print("Cities table created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(init_db())
