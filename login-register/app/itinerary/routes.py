from flask import render_template
from . import itinerary

@itinerary.route('/itinerary_create')
def itinerary_create():
    times = ["Morning", "Afternoon", "Evening"]  # example data
    return render_template('itinerary_create.html', times=times)
