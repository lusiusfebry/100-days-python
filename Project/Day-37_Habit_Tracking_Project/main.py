import requests
from datetime import datetime

USERNAME = "febrypthontest2"
TOKEN = "Dlsu2000"
GRAPH_ID = "graph2"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# Create user
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

#create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora",
}
#
headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
#
#
# Posting pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# # today = datetime.now(year=2023,month=2,day=25)
# today = datetime(year=2023,month=1,day=26)
today = datetime.now()
# # print (today.strftime("%Y%m%d"))
#
pixel_creation_parameter = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("how many KM ??"),
}
#
pixel_response = requests.post(url=pixel_creation_endpoint,json=pixel_creation_parameter,headers=headers)
print(pixel_response.text)

# update pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "4.5",
}

# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

# delete pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)
