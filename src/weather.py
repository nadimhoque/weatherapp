#!/usr/bin/python3

import os
import requests
import sys
from twilio.rest import Client

from argparse import ArgumentParser

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid,auth_token)

parser = ArgumentParser(description='Get the current weather based off of zipcode')
parser.add_argument('zip', help='zip/postal code is required to get weather')
parser.add_argument('--country', default ='us', help='country in where the zip/postal code is from. The default is US')

args = parser.parse_args()

owm_api_key = os.getenv("OWM_API_KEY")

if not owm_api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={owm_api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

temp = round((res.json()['main']['temp']-273.15) * (9/5) +32)

message = client.messages \
        .create(
                body=f"The tempearture at {args.zip} is {temp}",
                from_='+13236724859',
                to='+14805186235'
        )

print(message.sid)


