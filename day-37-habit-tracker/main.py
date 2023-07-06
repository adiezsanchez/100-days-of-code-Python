import requests
from datetime import datetime


USERNAME = "YOUR_USERNAME"
TOKEN = "TOKEN"
GRAPH_ID = "GRAPH_ID"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsofService":"yes",
    "notMinor":"yes"
}

# TODO.1 Create username, only needs to be done once
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# TODO.2 Create a graph definition
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_parameters = {
#     "id":"pythoncoding1",
#     "name":"100_Days_of_coding_Python",
#     "unit":"minutes",
#     "type":"int",
#     "color":"ajisai"
# }
# header = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint,  json=graph_parameters, headers=header)
# print(response.text)

loop = True

while loop:
    coding_today = input ("Do you want to input today's minutes of coding? Type Y/N: ")
    if coding_today == "Y":
        today = datetime.now()
        date_to_modify = today.strftime('%Y%m%d')
    else:
        date_to_modify = input ("Which date do you want to input your data for? YYYYMMDD: ")
    minutes_of_coding = int(input("How many minutes of coding do you want to input?: "))

    # TODO.3 Post today's value into a pixel
    #
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_params = {
        "date": date_to_modify,
        "quantity": f"{minutes_of_coding}"
    }
    header = {"X-USER-TOKEN": TOKEN}
    print(pixel_params)
    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
    print(response.text)

    ask_continue = input("Do you want to input more dates? Type Y/N: ")
    if ask_continue == "N":
        loop = False


# TODO.4 Update and delete pixels with PUT and DELETE methods
# Update

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221024"
# pixel_params = {"quantity":"60"}
# header = {"X-USER-TOKEN": TOKEN}
# response = requests.put(url=update_endpoint, json=pixel_params, headers=header)
# print(response.text)

# Delete

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221024"
# header = {"X-USER-TOKEN": TOKEN}
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)

