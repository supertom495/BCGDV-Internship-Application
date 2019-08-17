import requests
import json


def getKey():
    url = "https://interns.bcgdvsydney.com/api/v1/key"

    response = requests.get(url)
    apiKey = response.json()["key"]

    print(response.status_code)
    return apiKey


def postKey(apiKey):
    url = "https://interns.bcgdvsydney.com/api/v1/submit?apiKey={}".format(apiKey)

    data = json.dumps({
        "name": "Xiyan Tong",
        "email": "xiyan.tong@outlook.com"	
    })

    response = requests.post(url, data=data)

    print(response.status_code) 
    print(response.text)    


if __name__ == "__main__":
    postKey(getKey())