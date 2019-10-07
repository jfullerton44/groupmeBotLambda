import json
import requests
import os


def lambda_handler(event, context):
    
    # api-endpoint 
    URL = "https://api.groupme.com/v3/bots/post"
  
    # location given here 
    messageText = os.environ['message']
    botID = os.environ['bot_id']
      
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {
        'bot_id': botID,
        'text':messageText
    } 
      
    # sending get request and saving the response as response object 
    r = requests.post(url = URL, json = PARAMS) 
    return None
