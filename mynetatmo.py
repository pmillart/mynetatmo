#This code sample uses requests (HTTP library)
import requests
import os 
import json
import uuid
from azure.storage.blob import BlobServiceClient

netatmousername = os.environ['NETATMO_USERNAME']
netatmopasswd = os.environ['NETATMO_PWD']
netatmoclientid = os.environ['CLIENT_ID']
netatmosecret = os.environ['CLIENT_SECRET']

payload = {'grant_type': "password",
           'username': netatmousername,
           'password': netatmopasswd,
           'client_id':netatmoclientid,
           'client_secret': netatmosecret,
           'scope': 'read_station'}
try:
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token=response.json()["access_token"]
    refresh_token=response.json()["refresh_token"]
    scope=response.json()["scope"]
    params = { 'access_token': access_token }
    #print("Your access token is:", access_token)
    #print("Your refresh token is:", refresh_token)
    #print("Your scopes are:", scope)
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

try:
    response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
    #print(data)
    data2= json.dumps(data)
    print(data2)
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

try:
    id = uuid.uuid4()
    filename =  str(id) + ".json"
    print(filename)
    f = open("samples/" + filename, "w")
    f.write(data2)
    f.close()
    print("File saved local")
    
    sas_url = "BlobEndpoint=https://wesynapseadls.blob.core.windows.net/;QueueEndpoint=https://wesynapseadls.queue.core.windows.net/;FileEndpoint=https://wesynapseadls.file.core.windows.net/;TableEndpoint=https://wesynapseadls.table.core.windows.net/;SharedAccessSignature=sv=2019-10-10&ss=b&srt=sco&sp=rwdlacx&se=2021-07-09T17:43:22Z&st=2020-07-09T09:43:22Z&spr=https&sig=rHKApAft%2BNDAGoY7mn5WFXV5HQqmqoE%2BYGhqIIGx9Xc%3D"
    blob_service_client = BlobServiceClient.from_connection_string(sas_url)
    container_client = blob_service_client.get_container_client("wesynapsefs")
    blob_client = container_client.get_blob_client("netatmo/"+filename)
    print("save the data")
    with open("samples/" + filename, "rb") as data:
        blob_client.upload_blob(data)
except StorageErrorException:
    print("ERROR")
