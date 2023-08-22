import requests
import datetime as dt

USER_TOKEN = "ineedtohidethisinanenvendpoint15032003"
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "rynlkl"


user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": USER_TOKEN,
}

graph_params = {
    "id": "codegrph1503",
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "float",
    "color": "sora",
    "timezone": "GB",
}

graph_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_creation_endpoint,json=graph_params,headers=headers)
# print(response.text)

date_today = str(dt.datetime.today().date())
date = "".join(date_today.split("-"))

pixel_params = {
    "date": date,
    "quantity": str(1.0),
}
pixel_creation_endpoint = f"{graph_creation_endpoint}/{graph_params['id']}"
response = requests.post(url=pixel_creation_endpoint,json=pixel_params,headers=headers)

update_endpoint = f""
