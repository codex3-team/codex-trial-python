from flask import Blueprint
from cars.views import CarsApi
from utils.utils import register_api

cars_bp = Blueprint('cars_bp', __name__,)

register_api(cars_bp, CarsApi, 'cars_api', '/', pk='car_id')