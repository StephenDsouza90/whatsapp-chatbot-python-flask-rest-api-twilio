import requests
import waitress
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


def create_app():
    """
    Create server.
    """

    app = Flask("WhatsApp Chatbot")
    
    @app.route('/bot', methods=['POST'])
    def chatbot():
        incoming_message = request.values.get("Body").lower()

        outgoing_message = MessagingResponse()
        message = outgoing_message.message()

        responded = False

        if 'quote' in incoming_message:
            qoute_returned = requests.get('https://api.quotable.io/random')
            if qoute_returned.status_code == 200:
                data = qoute_returned.json()
                quote = f'{data["content"]} ({data["author"]})'
            else:
                quote = "Quote not available at the moment. Please send a message again."
            message.body(quote)
            responded = True

        if 'cat' in incoming_message:
            message.media('https://cataas.com/cat')
            responded = True

        if 'joke' in incoming_message:
            joke_returned = requests.get('http://api.icndb.com/jokes/random')
            if joke_returned.status_code == 200:
                data = joke_returned.json()
                value = data["value"]
                joke = value["joke"]
            else:
                joke = 'Joke not available at the moment. Please send a message again.'
            message.body(joke)
            responded = True

        if 'name' in incoming_message:
            name = 'My name is Stephen and I am a BOT. What is your name?'
            message.body(name)
            responded = True
        
        if 'calculate' in incoming_message:
            num = [int(num) for num in incoming_message.split() if num.isdigit()]
            num1 = num[0]
            num2 = num[1]
            if "+" in incoming_message:
                result = num1 + num2
            elif "-" in incoming_message:
                result = num1 - num2
            elif "*" in incoming_message:
                result = num1 * num2
            elif "/" in incoming_message:
                result = num1 / num2
            message.body(str(result))
            responded = True

        if 'order' in incoming_message:
            order = 'What do you want to order and in what quantity? We are selling brownies and biryani (boxes).'
            message.body(order)
            responded = True
        
        if 'brownies' in incoming_message:
            quantity = [int(q) for q in incoming_message.split() if q.isdigit()]
            order = "Order for {} boxes of brownies confirmed! Thank you.".format(quantity)
            message.body(order)
            responded = True

        if 'biryani' in incoming_message:
            quantity = [int(q) for q in incoming_message.split() if q.isdigit()]
            order = "Order for {} boxes of biryani confirmed! Thank you.".format(quantity)
            message.body(order)
            responded = True

        if not responded:
            message.body('Please use keywords "quote", "joke", "cat", "calculate and +, -, / or *", "name", "order"')

        return str(outgoing_message)
    return app


def main():
    """
    Run server.
    """
    app = create_app()
    waitress.serve(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()