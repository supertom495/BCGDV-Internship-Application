import requests
import json

Url = "https://interns.bcgdvsydney.com/api/v1/key"
# header = {}
# data = {}

response = requests.get(Url).json()
# data = json.loads(s=response)
apiKey = response["key"]
print(apiKey)

postUrl = "https://interns.bcgdvsydney.com/api/v1/submit?apiKey=" + apiKey

print(postUrl)

# response = requests.post(Url, data=data, headers=header).text
# print(response)