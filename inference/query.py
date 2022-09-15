import numpy as np
import requests
import json

x = np.random.uniform(0, 1, (1, 32, 32, 1))

data = {"input": x.tolist()}

response = requests.post(
    "http://inference.fly.dev/score",
    data = json.dumps(data)
)
print(response.json())