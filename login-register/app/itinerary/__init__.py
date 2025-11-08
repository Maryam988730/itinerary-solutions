from flask import Blueprint

itinerary = Blueprint('itinerary', __name__)

from . import routes