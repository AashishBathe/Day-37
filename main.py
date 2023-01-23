import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": os.environ.get("TOKEN"),
    "username": "lordshadow",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

response = requests.post(url=pixela_endpoint, json=user_parameters)
print(response.text)