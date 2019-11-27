# WhatsApp Chatbot


## Introduction

This application is a smiple chatbot used in WhatsApp. It is written in python code using REST API and flask and twilio libraries. 

It uses ngrok to allocate a temporary public domain that redirects HTTP requests to a local port.

I was inspired by the blog "Build a whatsapp chatbot with python flask and twilio" by Miguel Grinberg from Twilio.

Link: https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio


## How it works

### Incoming message

When a user sends a message to the WhatsApp chatbot, that message will be captured by the `request.values.get()` and saved in the `incoming_message` variable. 

### Process

The WhatsApp chatbot will analyze the message and find for the keywords.

In this application the keywords are:

1. quote
> I would like a quote

2. joke
> I want to a joke

3. cat
> I want to see a cat

4. calculate and +, -, / or *
> Please calculate 100 + 100

> Please calculate 100 - 100

> Please calculate 100 / 100

> Please calculate 100 * 100

5. name
> What is your name?

6. order
> I want to place an order

> I want 2 boxes of brownies

> I want 2 boxes of biryani

Once the bot detemines the keyword, it will carry out a process and prepare a message. This message will be saved in the `message.body()` for text and `message.media()` for images.

### Outgoing message

Once the message is ready, it will be sent back to the user by the `outgoing_message` variable using the `MessagingResponse()` function. 


## How to run locally

### To join

To use this application, save the number "+1 415 523 8886" and send a message "join congress-north".

It will link the user's number to Twilio and connect to the application to use the WhatsApp chatbot.

### Test cases

```
User: I would like a quote
Bot: Some people are always grumbling because roses have thorns; I am thankful that thorns have roses. (Alphonse Karr)

User: I want to a joke
Bot: As President Roosevelt said: &quot;We have nothing to fear but fear itself. And Chuck Norris.&quot;

User: I want to place an order
Bot: What do you want to order and in what quantity? We are selling brownies and biryani (boxes).

User: I want 2 boxes of brownies
Bot: Order for [2] boxes of brownies confirmed! Thank you.

User: Calculate 10 * 10
Bot: 100
```

## Setup

To setup the applicaiton, follow the twilio link mentioned above.