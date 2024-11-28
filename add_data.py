from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    "https://f70a99e805574c3394cbe207273ffd79.us-west1.gcp.cloud.es.io:443",
    basic_auth=("elastic", "0JOOysCWnyUU1KkM8zp0bysV"),
)

# Mock data for Tempe relief centers
data = [
    {
        "name": "Tempe Food Bank",
        "resources": "food, water",
        "location": {"lat": 33.4255, "lon": -111.9400},
        "address": "123 Main St, Tempe, AZ 85281",
        "contact": "(480) 555-1234",
    },
    {
        "name": "Tempe Medical Aid Center",
        "resources": "medical aid, first aid kits",
        "location": {"lat": 33.4246, "lon": -111.9327},
        "address": "456 College Ave, Tempe, AZ 85281",
        "contact": "(480) 555-5678",
    },
    {
        "name": "Tempe Shelter",
        "resources": "shelter, blankets",
        "location": {"lat": 33.4263, "lon": -111.9434},
        "address": "789 Rural Rd, Tempe, AZ 85281",
        "contact": "(480) 555-9012",
    },
]

# Index data
for idx, center in enumerate(data):
    es.index(index="relief_centers", id=idx + 1, document=center)

print("Data added!")
