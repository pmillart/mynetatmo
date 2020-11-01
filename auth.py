#This code sample uses requests (HTTP library)
import requests

payload = {'grant_type': 'password',
           'username': "[USER_EMAIL]",
           'password': "[USER_PASSWORD]",
           'client_id':"[YOUR_APP_ID]",
           'client_secret': "[YOUR_CLIENT_SECRET]",
           'scope': '[SCOPE_SPACE_SEPARATED]'}
try:
        response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
        response.raise_for_status()
        access_token=response.json()["access_token"]
        refresh_token=response.json()["refresh_token"]
        scope=response.json()["scope"]
        print("Your access token is:", access_token)
        print("Your refresh token is:", refresh_token)
        print("Your scopes are:", scope)
except requests.exceptions.HTTPError as error:
        print(error.response.status_code, error.response.text)
