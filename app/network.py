import logging
from typing import List

import aiohttp
from pydantic import ValidationError

from app.config import settings
from app.models.city import City


async def fetch_cities(city_name: str) -> List[City]:
    url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
    headers = {
        "X-Api-Key": settings.API_TOKEN
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                try:
                    cities = [City(**city_data) for city_data in data]
                    return cities
                except ValidationError as e:
                    logging.error(f"Validation error: {e}")
                    return []
            else:
                logging.warning(f"Failed to fetch cities: HTTP {response.status}")
                return []
