# mynetatmo

## Install requirements

- Set new virtual env  
`./python -m samples/venv`
- install requirements  
`pip install -r requirements`

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
