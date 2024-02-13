# Import Flask and ngrok
from flask import Flask, request
from flask_ngrok import run_with_ngrok

# Create a Flask app and run it with ngrok
app = Flask(__name__)
run_with_ngrok(app)

# Define a route for the USSD code
@app.route('/', methods=['POST', 'GET'])
def ussd():
    # Get the session parameters from the request
    session_id = request.values.get('sessionId', None)
    service_code = request.values.get('serviceCode', None)
    phone_number = request.values.get('phoneNumber', None)
    text = request.values.get('text', 'default')
    
    # Split the text input by asterisks
    text_array = text.split('*')
    user_response = text_array[-1]
    
    # Check the user input and generate the response
    if text == '':
        # This is the first request, show the landing page
        response = 'CON Welcome to My USSD Service\n'
        response += 'Please select an option:\n'
        response += '1. Check balance\n'
        response += '2. Send money\n'
        response += '3. Exit\n'
    elif text == '1':
        # The user selected option 1, show the balance
        # You can get the balance from the database using the phone number
        balance = 1000 # Dummy value
        response = f'END Your balance is {balance} Naira\n'
    elif text == '2':
        # The user selected option 2, ask for the recipient number
        response = 'CON Enter the recipient number:\n'
    elif len(text_array) == 2 and text_array[0] == '2':
        # The user entered the recipient number, ask for the amount
        response = 'CON Enter the amount to send:\n'
    elif len(text_array) == 3 and text_array[0] == '2':
        # The user entered the amount, confirm the transaction
        recipient_number = text_array[1]
        amount = text_array[2]
        response = f'CON You are about to send {amount} Naira to {recipient_number}\n'
        response += 'Press 1 to confirm or 2 to cancel:\n'
    elif len(text_array) == 4 and text_array[0] == '2' and text_array[3] == '1':
        # The user confirmed the transaction, process it and show the result
        # You can update the database and send an SMS confirmation using the service API
        response = 'END Transaction successful\n'
    elif len(text_array) == 4 and text_array[0] == '2' and text_array[3] == '2':
        # The user canceled the transaction, show the result
        response = 'END Transaction canceled\n'
    elif text == '3':
        # The user selected option 3, exit the service
        response = 'END Thank you for using My USSD Service\n'
    else:
        # The user input is invalid, show the error message
        response = 'END Invalid input\n'
    
    # Return the response to the mobile network operator
    return response

# Run the app
if __name__ == '__main__':
    app.run()
