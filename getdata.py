import requests
import os
import json
import uuid
from azure.cosmos import  CosmosClient, Container, Database, PartitionKey
from azure.cosmos.errors import HTTPFailure
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
from azure.cosmos.partition_key import PartitionKey

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
    #print("Your access token is:", access_token)
    #print("Your refresh token is:", refresh_token)
    #print("Your scopes are:", scope)
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

params = { 'access_token': access_token }

try:
    response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
    #print(data)
    data2= json.dumps(data)
    #print(data2)
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, auth = {
    'masterKey': key
})

database_name = 'NetatmoDatabase'
container_name = 'mesures'

try:
    database = client.create_database(database_name)
except HTTPFailure as ae:
    if e.status_code != 409:
        raise
    database = client.get_database_client(database_name)

database_client = client.get_database_client(database_name)

try:
    container_client = database_client.create_container(id=container_name, partition_key=PartitionKey(path="/user/mail"))
except HTTPFailure as e:
    if e.status_code != 409:
        raise
    container_client = database_client.get_container_client(container_name)

container_client = database_client.get_container_client(container_name)

container_client.upsert_item(data)
#print(sample)

#container_client.upsert_item(sample)
#container.create_item(data2)
