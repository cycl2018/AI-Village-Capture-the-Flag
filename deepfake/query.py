import base64
import requests
import json

with open("sample.mp4", "rb") as f:
    data = f.read()

b64_data = base64.urlsafe_b64encode(data).decode()

in_data = json.dumps({"input": b64_data})

score = requests.post("https://deepfake.fly.dev/score", data=in_data)

print(score.json())