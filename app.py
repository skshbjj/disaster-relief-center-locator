from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["*"])

# Initialize Elasticsearch client
# Replace "http://localhost:9200" with your Elasticsearch URL if different
es = Elasticsearch(hosts=["http://localhost:9200"])

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/search", methods=["GET"])
def search():
    """
    Endpoint to search relief centers based on query parameters.
    Query Parameters:
        q: Resource to search for (e.g., "food")
        lat: Latitude of the location
        lon: Longitude of the location
        distance: Search radius (e.g., "10km")
    """
    query = request.args.get("q", "")
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    distance = request.args.get("distance", "10km")

    if not lat or not lon:
        return jsonify({"error": "Latitude and Longitude are required!"}), 400

    try:
        # Elasticsearch geo-distance query
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"resources": query}}
                    ],
                    "filter": {
                        "geo_distance": {
                            "distance": distance,
                            "location": {
                                "lat": lat,
                                "lon": lon
                            }
                        }
                    }
                }
            }
        }

        response = es.search(index="relief_centers", body=body)
        hits = response["hits"]["hits"]

        # Format the response
        results = [{"_source": hit["_source"], "_score": hit["_score"]} for hit in hits]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Export Flask app for Vercel
if __name__ == "__main__":
    app.run()
