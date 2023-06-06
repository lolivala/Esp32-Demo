import urequests
import ujson
from objects import *

class Webclient:
    host = ""
    port= ""
    jsonRequest =""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
         
    def	postData(self, jsonData, route, headers):
        url = '{}:{}/{}'.format(self.host, self.port, route)
        response = urequests.post(url, headers = headers, data =jsonData)
        print(url)

#document = DeviceMeasurements("Huerto Emmanuelle","Huerto Emmanuelle")
#document.addMeasurent(Measurement("Temperature","100","C", "2023-06-06"))
#document.addMeasurent(Measurement("Humidity","55","%", "2023-06-06"))
#document.addMeasurent(Measurement("Soil Humidity","35","%", "2023-06-06"))

#jsonData = document.getDataInJson()

#apiClient = Webclient("http://192.168.0.124", 5000)
#response = apiClient.postData(jsonData,"measurements",{'content-type': 'application/json'})

#print(response)