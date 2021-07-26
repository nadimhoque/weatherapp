# Introduction

This is my weather app. I have used open weather map to get the weather and the twilio api to get the weather.

## Instructions

Since I use the the os.environ method, you will need to export the following variables

TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN
OWM_API_KEY

The first two are obviously from Twilio and the last one is from open weather map. 

There is a help page with when you run the weather.py, but you do need to put in the zip code. After exporting the variables above, this is how you can run the script:

python3 weather.py 10001

If all works you should get a sms text from twilio

## Todo's

I do have a bit of work on this because the real way
