
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("data.json")
firebase_admin.initialize_app(cred)
db = firestore.client()




@app.route('/')
def home():
    return render_template('home.html')

# Get all itineraries


@app.route('/api/itineraries', methods=['GET'])
def get_itineraries():
    return jsonify(itineraries)

# Create new itinerary


@app.route('/api/itineraries', methods=['POST'])
def create_itinerary():
    data = request.get_json()
    new_itinerary = {
        "user": data.get("user", "Anonymous"),
        "country": data["country"],
        "city": data["city"],
        "theme": data.get("theme", "General"),
        "stops": data.get("stops", [])
    }
    doc_ref = db.collection('itineraries').add(new_itinerary)
    new_itinerary["id"] = doc_ref[1].id  # add Firestore doc ID
    return jsonify(new_itinerary), 201

@app.route('/api/collide/<id1>/<id2>', methods=['GET'])
def collide_itineraries(id1, id2):
    t1 = db.collection('itineraries').document(id1).get()
    t2 = db.collection('itineraries').document(id2).get()

    if not t1.exists or not t2.exists:
        return jsonify({"error": "One or both itineraries not found"}), 404

    t1_data = t1.to_dict()
    t2_data = t2.to_dict()

    merged_stops = sorted(list(set(t1_data["stops"] + t2_data["stops"])))
    return jsonify({
        "itinerary_1": t1_data,
        "itinerary_2": t2_data,
        "merged_stops": merged_stops
    })


if __name__ == '__main__':
    app.run(debug=True)