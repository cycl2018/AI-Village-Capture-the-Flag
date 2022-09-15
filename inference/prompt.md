# Inference (id: inference)

### Scenario
Model model on the wall, who is the fairest of them all? 

?gnidaer llits uoy era yhW .uoy htiw skcans thguorb ev'dluohs uoY .skcans rof pots t'noD .won oG .tsaf oG .niW .galf eht teG .ledom eht esreveR

### Objective
Retrieve the images that spell the flag.

### Query
```python
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
```