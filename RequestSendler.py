import requests
from decouple import config
from DataMapper import DataMapper
class RequestSendler(object):
    id = config("GUID")
    url = config("URL")
    def SendMessageToServer(self, message):

        data = {"botid": self.id, "message": message}
        postRequest = requests.post(self.url, data=data)
        message = DataMapper.getMessage(json=postRequest.json)
        return message


