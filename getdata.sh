#set -x 

export CLIENT_ID=$(az keyvault secret show --name NETATMOCLIENTID --vault-name pmtkeyvault --query value -o tsv)
export CLIENT_SECRET=$(az keyvault secret show --name NETATMOCLIENTSECRET --vault-name pmtkeyvault --query value -o tsv)
export NETATMO_USERNAME=$(az keyvault secret show --name NETATMOUSERNAME --vault-name pmtkeyvault --query value -o tsv)
export NETATMO_PWD=$(az keyvault secret show --name NETATMOPWD --vault-name pmtkeyvault --query value -o tsv)
export NETATMO_DEVICE_ID=$(az keyvault secret show --name NETATMODEVICEID --vault-name pmtkeyvault --query value -o tsv)

export NETATMO_API=https://api.netatmo.com/oauth2/token

[ -z $NETATMO_AUTH ] && export NETATMO_AUTH=$(curl -d "grant_type=password&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&username=$NETATMO_USERNAME&password=$NETATMO_PWD&scope=read_station" https://api.netatmo.net/oauth2/token)
export NETATMO_ACCESS_TOKEN=$(echo $NETATMO_AUTH | jq -r '.access_token')
export NETATMO_REFRESH_TOKEN=$(echo $NETATMO_AUTH | jq -r '.refresh_token')

curl -s -d "access_token=$NETATMO_ACCESS_TOKEN&device_id=$NETATMO_DEVICE_ID" https://api.netatmo.com/api/getstationsdata
