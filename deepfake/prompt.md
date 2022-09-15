# DeepFake (id: deepfake)

### Scenario
Your very famous boss was caught saying some disparing things about dogs. Naturally, the dog lobby is not happy. To make matters worse, they paid someone to make a deepfake that was caught by a SuperSecretDeepFakeDefenseSystem.  

### Objective
Fix the `sample.mp4` to bypass the SuperSecretDeepFakeDefenseSystem and get your boss out of the media.

### Query
```python
import base64
import requests
import json

with open("sample.mp4", "rb") as f:
    data = f.read()

b64_data = base64.urlsafe_b64encode(data).decode()
in_data = json.dumps({"input": b64_data})

score = requests.post("https://deepfake.fly.dev/score", data=in_data)

print(score.json())
```