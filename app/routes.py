from aiohttp import web

from .views.city import (
    create_city_handler,
    get_city_by_id_handler,
    delete_city_handler,
    get_all_cities_handler,
    get_nearest_cities_handler,
)


def setup_routes(app: web.Application):
    app.router.add_post('/cities', create_city_handler)
    app.router.add_get('/cities/{id}', get_city_by_id_handler)
    app.router.add_delete('/cities/{id}', delete_city_handler)
    app.router.add_get('/cities', get_all_cities_handler)
    app.router.add_get('/cities/nearest', get_nearest_cities_handler)
