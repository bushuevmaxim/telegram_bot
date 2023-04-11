import requests
from decouple import config
from DataMapper import DataMapper
endpoint = config("ENDPOINT_PREDICT")
class RequestSendler(object):
    def SendMessageToServer(message, userID):
        data = {"bot_guid": config("GUID"), "message": message, "client_id": userID}
        postRequest = requests.post(url = config("URL") + endpoint, json=data)
        if postRequest.status_code == 200:
            jsonResponse = postRequest.json()
            message = DataMapper.getMessage(json=jsonResponse)
            return message
        else:
            return "Я вас не понимаю."
        
        
        

    
