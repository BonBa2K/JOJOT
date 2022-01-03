import requests
import json

dd = {
  "device_id": "01",
  "account": "string1",
  "device_name": "string1",
  "language": "string",
  "system_volume": 0,
  "media_volume": 0,
  "user_account": "string"
}

url = "http://127.0.0.1:8000/devicedata/"
url = "http://127.0.0.1:8000/devicedata/01"

#html = requests.post(url, json.dumps(dd))
html = requests.delete(url)

print(html.text)