from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Elastic Cloud credentials
ELASTIC_CLOUD_URL = "https://f70a99e805574c3394cbe207273ffd79.us-west1.gcp.cloud.es.io:443"
ELASTIC_USERNAME = "elastic"
ELASTIC_PASSWORD = "0JOOysCWnyUU1KkM8zp0bysV"

# Connect to Elasticsearch
es = Elasticsearch(
    ELASTIC_CLOUD_URL,
    basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),
    verify_certs=True
)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    distance = request.args.get("distance", "10km")
    
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

if __name__ == "__main__":
    app.run(debug=True)
