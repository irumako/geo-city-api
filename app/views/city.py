import json

from aiohttp import web

from app.db.queries import store_cities, retrieve_cities, get_city, delete_city
from app.models.city import CityResponse
from app.network import fetch_cities
from app.utils import haversine


async def create_city_handler(request):
    city_name = request.query.get('name')
    if not city_name:
        return web.json_response({"error": "City name is required"}, status=400)
    cities = await fetch_cities(city_name)
    if cities:
        await store_cities(cities, request.app)
        return web.json_response([city.dict() for city in cities])
    else:
        return web.json_response({"error": "No city found"}, status=404)


async def delete_city_handler(request):
    city_id = request.match_info.get('id')

    try:
        city_id = int(city_id)
    except ValueError:
        return web.json_response({"error": "Invalid City ID"}, status=400)

    city = await get_city(city_id, request.app)
    if city:
        await delete_city(city_id, request.app)
        return web.json_response({"message": "City deleted successfully"})
    else:
        return web.json_response({"error": "City not found"}, status=404)


async def get_city_by_id_handler(request: web.Request):
    city_id = request.match_info.get('id')

    try:
        city_id = int(city_id)
    except ValueError:
        return web.json_response({"error": "Invalid City ID"}, status=400)

    city = await get_city(city_id, request.app)
    if city:
        return web.json_response(city.dict())
    else:
        return web.json_response({"error": "City not found"}, status=404)


async def get_all_cities_handler(request):
    cities = await retrieve_cities(request.app)
    return web.json_response(CityResponse(cities=cities).dict())


async def get_nearest_cities_handler(request):
    try:
        lat = float(request.query.get('latitude'))
        lon = float(request.query.get('longitude'))
    except (TypeError, ValueError):
        return web.json_response({"error": "Invalid latitude or longitude"}, status=400)

    cities = await retrieve_cities(request.app)
    nearest_cities = sorted(cities, key=lambda x: haversine(lat, lon, x.longitude, x.latitude))[:2]
    return web.json_response(CityResponse(cities=nearest_cities).dict())
