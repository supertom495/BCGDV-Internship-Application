import requests
import json
import base64


def getKey():
    url = "https://interns.bcgdvsydney.com/api/v1/key"

    response = requests.get(url)
    apiKey = response.json()["key"]

    print(response.status_code)
    return apiKey

def postKey(apiKey):
    url = "https://interns.bcgdvsydney.com/api/v1/submit?apiKey={}".format(apiKey)

    name = base64.b64decode(b'WGl5YW4gVG9uZw==').decode("utf-8")
    email = base64.b64decode(b'eGl5YW4udG9uZ0BvdXRsb29rLmNvbQ==').decode("utf-8")

    data = json.dumps({
        "name": name,
        "email": email	
    })

    response = requests.post(url, data=data)

    print(response.status_code) 
    print(response.text)    

if __name__ == "__main__":
    postKey(getKey())
