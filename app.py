from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

## Init Flask APp
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
  ## GEt user message
    user_msg = request.values.get('Body', '').lower()
    ## Init bot response
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    # Applying bot logic
    if 'hello' in user_msg:
        msg.body("Hi there! welcome to whatsapp chatbot! please select SUBJECT to download the material 1.DS 2.MEFA 3.DAA 4.WT 5.PC 6.ABOUT CHATBOT ")
    elif '1' in user_msg:
        msg.body('Download DS Material From Following Link - https://bit.ly/3xbTThS ')
    elif '2' in user_msg:
        msg.body("Download MEFA Material From Following Link - https://bit.ly/39dKuyd ")
    elif '3' in user_msg:
        msg.body("Download DAA Material From Following Link- https://bit.ly/39gaBob ")
    elif '4' in user_msg:
        msg.body('Download WT Material From Following Link-https://bit.ly/3O1YOZn')
    elif '5' in user_msg:
        msg.body('Download PC Material From Following Link - https://bit.ly/3H0gqCw ')
    elif '6' in user_msg:
        msg.body('All source code of this project github link - https://github.com/aadiaditya/chatbot  MADE WITH ❤️ BY SAI ADITYA')
    else:
        msg.body("Sorry, Entered wrong option.Pls choose correct one")
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)