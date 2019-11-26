"""
https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio
"""

"""
Join
>> WhatsApp message to +1 415 523 8886 with code "join congress-north"

Sandbox Configuration
>> https://www.twilio.com/console/sms/whatsapp/sandbox

sample
>> https://493a56cb.ngrok.io + /bot
>> https://493a56cb.ngrok.io/bot

SAVE
"""

"""
Open a second terminal window and run "ngrok http 8080" to allocate a temporary public domain 
that redirects HTTP requests to our local port 5000. 

Note the lines beginning with “Forwarding”. 
These show the public URL that ngrok uses to redirect requests into our service. 
What we need to do now is tell Twilio to use this URL to send incoming message notifications.

Go back to the Twilio Console, click on Programmable SMS, then on WhatsApp, and finally on Sandbox. 
>> https://www.twilio.com/console/sms/whatsapp/sandbox

Copy the https:// URL from the ngrok output and then paste it on the “When a message comes in” field. 
Since our chatbot is exposed under the /bot URL, append that at the end of the root ngrok URL. 
Make sure the request method is set to HTTP Post. 
Don’t forget to click the red Save button at the bottom of the page to record these changes.
"""