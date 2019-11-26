from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import waitress


def create_app():
    """
    Creates the server app.
    """
    app = Flask("WhatsApp Chatbot")

    # the application defines a /bot endpoint that listens to POST requests.
    @app.route('/bot', methods=['POST'])
    def bot():
        """
        The body of the function bot() is going to analyze the message sent by the user and provide the appropriate response.
        """
        # First obtain a message from the user. 
        # Message comes via POST request in which Key is the "Body" and values is the "message".
        # {"Body": "can you send me a famous quote?"}
        # Converted the text to lowercase, so that all words can appear in a same case variations.
        incoming_msg = request.values.get('Body', '').lower()

        # Create a response that includes text and media components
        resp = MessagingResponse()
        msg = resp.message()
        
        responded = False
        if 'quote' in incoming_msg:
            # return a quote
            r = requests.get('https://api.quotable.io/random')
            if r.status_code == 200:
                data = r.json() # "values" : "{"content": "Some quote"} {"author": "author name"}"
                quote = f'{data["content"]} ({data["author"]})'
            else:
                quote = 'I could not retrieve a quote at this time, sorry.'
            msg.body(quote)
            responded = True
        if 'cat' in incoming_msg:
            # return a cat pic
            msg.media('https://cataas.com/cat')
            responded = True
        if 'joke' in incoming_msg:
            r = requests.get('http://api.icndb.com/jokes/random')
            if r.status_code == 200:
                data = r.json()
                value = data["value"]
                joke = value["joke"]
            else:
                joke = 'I could not retrieve a joke at this time, sorry.'
            msg.body(joke)
            responded = True
        if 'name' in incoming_msg:
            name = 'My name is Stephen and I am a BOT.'
            msg.body(name)
            responded = True
        if 'calculate' in incoming_msg:
            num = [int(num) for num in incoming_msg.split() if num.isdigit()]
            num1 = num[0]
            num2 = num[1]
            if "+" in incoming_msg:
                result = num1 + num2
            elif "-" in incoming_msg:
                result = num1 - num2
            elif "*" in incoming_msg:
                result = num1 * num2
            elif "/" in incoming_msg:
                result = num1 / num2
            msg.body(str(result))
            responded = True
        if not responded:
            # return a generic response here
            msg.body('I only share quotes, jokes, cat images, calculate(using +, -, / and *) and say my name, sorry!')
        return str(resp)
    return app


def main():
    """
    Create the app.
    """
    app = create_app()
    waitress.serve(app, host='0.0.0.0', port=8080)


main()