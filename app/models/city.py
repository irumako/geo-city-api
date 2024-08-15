from pydantic import BaseModel
from typing import List


class City(BaseModel):
    name: str
    country: str
    population: int
    latitude: float
    longitude: float
    is_capital: bool


class CityResponse(BaseModel):
    cities: List[City]
