from elasticsearch import Elasticsearch

es = Elasticsearch("http://127.0.0.1:9200")

# Sample data
data = [
    {"name": "Tempe Food Bank", "resources": "food, water", "location": {"lat": 33.4255, "lon": -111.9400}, "timestamp": "2024-11-28T12:00:00Z"},
    {"name": "Phoenix Medical Center", "resources": "medical aid", "location": {"lat": 33.4484, "lon": -112.0740}, "timestamp": "2024-11-28T12:00:00Z"},
    {"name": "Mesa Shelter", "resources": "shelter", "location": {"lat": 33.4152, "lon": -111.8315}, "timestamp": "2024-11-28T12:00:00Z"},
    {"name": "ASU Student Support Center", "resources": "food, medical aid", "location": {"lat": 33.4242, "lon": -111.9281}, "timestamp": "2024-11-28T12:00:00Z"},
    {"name": "Tempe Community Center", "resources": "food, water, shelter", "location": {"lat": 33.4223, "lon": -111.9327}, "timestamp": "2024-11-28T12:00:00Z"}
]

# Bulk insert
for entry in data:
    es.index(index="relief_centers", document=entry)
