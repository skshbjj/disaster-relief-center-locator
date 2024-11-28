from flask import Flask, request, jsonify
from flask_cors import CORS
from elasticsearch import Elasticsearch

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Connect to Elasticsearch
es = Elasticsearch(
    hosts=["http://localhost:9200"]
)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', None)
    lat = float(request.args.get('lat', 40.7306))
    lon = float(request.args.get('lon', -73.9352))
    distance = request.args.get('distance', '10km')

    es_query = {
        "query": {
            "bool": {
                "must": [{"match": {"resources": query}}] if query else [],
                "filter": {
                    "geo_distance": {
                        "distance": distance,
                        "location": {"lat": lat, "lon": lon}
                    }
                }
            }
        }
    }

    try:
        result = es.search(index="relief_centers", body=es_query)
        return jsonify(result['hits']['hits'])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    try:
        es.index(index="relief_centers", document=data)
        return jsonify({"message": "Data added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
