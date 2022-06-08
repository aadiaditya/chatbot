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
    if 'hi' in user_msg:
        msg.body("Hi there! welcome to whatsapp chatbot! please select SUBJECT to download the material \n 1.DS \n 2.MEFA \n 3.DAA \n 4.WT \n 5.PC \n 6.ABOUT CHATBOT")
    elif '1' in user_msg:
        msg.body('Download DS Material From Following Link - https://bit.ly/3xbTThS . Thank you for using this bot.All the best for exams')
    elif '2' in user_msg:
        msg.body("Download MEFA Material From Following Link - https://bit.ly/39dKuyd Thank you for using this bot.All the best for exams")
    elif '3' in user_msg:
        msg.body("Download DAA Material From Following Link- https://bit.ly/39gaBob Thank you for using this bot.All the best for exams")
    elif '4' in user_msg:
        msg.body('Download WT Material From Following Link-https://bit.ly/3O1YOZn Thank you for using this bot.All the best for exams')
    elif '5' in user_msg:
        msg.body('Download PC Material From Following Link - https://bit.ly/3H0gqCw  Thank you for using this bot.All the best for exams')
    elif '6' in user_msg:
        msg.body('All source code of this project github link - https://github.com/aadiaditya/chatbot  MADE WITH ❤️ BY SAI ADITYA')
    else:
        msg.body("Sorry, Entered wrong option.Pls choose correct one")
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)