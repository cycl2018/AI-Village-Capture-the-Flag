import requests
import json


data = json.dumps(
    {
        "line1": 10,
        "line2": 11
    }
)

score = requests.post(
    "https://token.fly.dev/score", 
    data=data
)

print(score.json())