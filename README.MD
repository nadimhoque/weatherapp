# Introduction

This is my weather app. I have used open weather map to get the weather and the twilio api to get the weather.

## Instructions

Since I use the the os.environ method, you will need to export the following variables

TWILIO_ACCOUNT_SID

TWILIO_AUTH_TOKEN

OWM_API_KEY

The first two are obviously from Twilio and the last one is from open weather map. 

For testing I have created a bash script:

---BEGIN---

```console

#!/bin/bash

export OWM_API_KEY="$API_KEY"
export TWILIO_ACCOUNT_SID="$API_KEY"
export TWILIO_AUTH_TOKEN="$API_KEY"

python3 weather.py $1

```

---END---

If you choose to use the above script then you would probably do the following:

```console

bash $SCRIPT_NAME $ZIP_CODE

```

where $SCRIPT_NAME is the name of the bash script that contains the lines from above and $ZIP_CODE is whatever zip code you want

If it executes correctly then you should get a text message that texts you the weather at your defined $ZIP_CODE

## Todo's

For now I want to use more fucntions in the code. For example I think parsing the arguments should be one function and the sending of the text message via twilio should be another.

Once the script has more functions I may want to deploy this into AWS and have a server on there regularly execute the script.

## Notes

I will keep updating this as needed.
