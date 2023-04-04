import requests
from decouple import config
from DataMapper import DataMapper
class RequestSendler(object):
    def SendMessageToServer(message):
        data = {"bot_guid": config("GUID"), "message": message}
        postRequest = requests.post(url = config("URL") + "/chat/predict", json=data)
        if postRequest.status_code == 200:
            jsonResponse = postRequest.json()
            message = DataMapper.getMessage(json=jsonResponse)
            return message
        else:
            return "Я вас не понимаю."
        
        
        

    
