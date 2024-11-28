from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Elastic Cloud credentials
ELASTIC_CLOUD_URL = "https://f70a99e805574c3394cbe207273ffd79.us-west1.gcp.cloud.es.io:443"
ELASTIC_USERNAME = "elastic"
ELASTIC_PASSWORD = "0JOOysCWnyUU1KkM8zp0bysV"

# Connect to Elasticsearch
try:
    es = Elasticsearch(
        ELASTIC_CLOUD_URL,
        basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),
        verify_certs=True
    )
    # Test connection
    if not es.ping():
        raise ValueError("Connection to Elasticsearch failed.")
except Exception as e:
    raise SystemExit(f"Failed to connect to Elasticsearch: {e}")

# Root route to confirm backend is running
@app.route("/", methods=["GET"])
def index():
    return "Backend is live!"

# Search route
@app.route("/search", methods=["GET"])
def search():
    try:
        query = request.args.get("q", "")
        lat = request.args.get("lat", type=float)
        lon = request.args.get("lon", type=float)
        distance = request.args.get("distance", "10km")
        
        if lat is None or lon is None:
            return jsonify({"error": "Missing 'lat' or 'lon' in the request"}), 400

        body = {
            "query": {
                "geo_distance": {
                    "distance": distance,
                    "location": {
                        "lat": lat,
                        "lon": lon
                    }
                }
            }
        }

        if query:
            body["query"] = {
                "bool": {
                    "must": [
                        {"match": {"resources": query}},
                        body["query"]
                    ]
                }
            }

        response = es.search(index="relief_centers", body=body)
        return jsonify(response["hits"]["hits"])
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
