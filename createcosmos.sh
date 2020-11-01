
#https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/cosmos/azure-cosmos#getting-started

export RES_GROUP=netatmo
export ACCT_NAME=cosmosnetatmo

az group create --name $RES_GROUP --location westeurope
az cosmosdb create --resource-group $RES_GROUP --name $ACCT_NAME

export ACCOUNT_URI=$(az cosmosdb show --resource-group $RES_GROUP --name $ACCT_NAME --query documentEndpoint --output tsv)
export ACCOUNT_KEY=$(az cosmosdb list-keys --resource-group $RES_GROUP --name $ACCT_NAME --query primaryMasterKey --output tsv)


