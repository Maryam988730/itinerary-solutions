# app/api.py
from flask import Blueprint, request, jsonify, render_template

api = Blueprint('api', __name__, url_prefix='/api') 

# Temporary in-memory itineraries
itineraries = [
    {"id": 1, "user": "Alex", "country": "Japan", "city": "Tokyo",
     "theme": "Culture", "stops": ["Shibuya", "Asakusa", "Ueno Park"]},
    {"id": 2, "user": "Maya", "country": "Japan", "city": "Kyoto",
     "theme": "Food", "stops": ["Gion", "Nishiki Market", "Fushimi Inari"]}
]

@api.route('/')
def home():
    return render_template('home.html')

@api.route('/api/itineraries', methods=['GET'])
def get_itineraries():
    return jsonify(itineraries)

@api.route('/api/itineraries', methods=['POST'])
def create_itinerary():
    data = request.get_json()
    new_itinerary = {
        "id": len(itineraries) + 1,
        "user": data.get("user", "Anonymous"),
        "country": data["country"],
        "city": data["city"],
        "theme": data.get("theme", "General"),
        "stops": data.get("stops", [])
    }
    itineraries.append(new_itinerary)
    return jsonify(new_itinerary), 201

@api.route('/api/collide/<int:id1>/<int:id2>', methods=['GET'])
def collide_itineraries(id1, id2):
    t1 = next((t for t in itineraries if t["id"] == id1), None)
    t2 = next((t for t in itineraries if t["id"] == id2), None)
    if not t1 or not t2:
        return jsonify({"error": "One or both itineraries not found"}), 404
    merged_stops = sorted(list(set(t1["stops"] + t2["stops"])))
    return jsonify({
        "itinerary_1": t1,
        "itinerary_2": t2,
        "merged_stops": merged_stops
    })
