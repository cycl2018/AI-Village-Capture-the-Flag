from PIL import Image
import base64
import requests
import json


IMAGE_DIMS = (224, 224)

img = Image.open("/kaggle/input/ai-village-ctf/hotdog/chester.png")
img = img.resize(IMAGE_DIMS)
img_bytes = img.tobytes()
b64_img_bytes = base64.urlsafe_b64encode(img_bytes)

data = {
    "input": b64_img_bytes.decode()
}

score = requests.post("https://hotdog.fly.dev/score", data=json.dumps(data))
print(score.content)

