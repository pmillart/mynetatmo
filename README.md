# mynetatmo

## Install requirements

- Set new virtual env  
`./python -m samples/venv`
- install requirements  
`pip install -r requirements`
- You can check using:  
`pip list`

## get Variables from azure key vault
- CLIENT_ID provided by Netatmo
- CLIENT_SECRET
- NETATMO_USERNAME
- NETATMO_PWD
- NETATMO_DEVICE_ID

## Step 1:  Try to get data from Netatmo using curl

Secret are stored in azure keyvault  
Just run the followinf script

`./getdata.sh`

## Step 2: using Python



- source environnement  
`source samples/venv/bin/activate` 
```
. ./env.sh
python mynetatmo.py
```
