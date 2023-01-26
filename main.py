import requests
import os
import datetime as dt

USERNAME = "lordshadow"
TOKEN = os.environ.get("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"

data = input("How many minutes did you code today? ")

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_param = {
    "id": "graph1",
    "name": "Python Course",
    "unit": "Hour",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Calcutta"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = dt.datetime.now()
DATE = today.strftime("%Y%m%d")

pixel_param = {
    "date": DATE,
    "quantity": data,
    "unit": "Mins",
    "color": "sora"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_param, headers=headers)
# print(response.text)

response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1", json=pixel_param, headers=headers)
print(response.text)

# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1", json=pixel_param, headers=headers)
# print(response.text)

# response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{DATE}", headers=headers)
# print(response.text)