import sys

sys.path.insert(0, "./")

import requests

ride = {"PULocationID": 10, "DOLocationID": 50, "trip_distance": 40}

url = "http://localhost:9696/predict"
response = requests.post(url, json=ride).json()
print(response)
