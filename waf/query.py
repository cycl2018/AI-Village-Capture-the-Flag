import requests
import json
import base64

input = base64.b64encode(b"This was a test of your emergency systems").decode()
data = json.dumps(
    {"input": input}
)

score = requests.post(
    "https://waf.fly.dev/score", 
    data=data
)

print(score.json())