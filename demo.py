import urequests
import ujson

root =  {}
root["MeasurementID"] = "adfsghdafg-asdgfadfsgs-adfgadfgad"

lista  = []

dict = {}
dict["SensorType"] = "Temperature"
dict["UnitOfMeasure"] = "C"
dict["SensorName"] = "DHT11"

lista.append(dict)

dict2 = {}
dict2["SensorType"] = "Humidity"
dict2["UnitOfMeasure"] = "%"
dict2["SensorName"] = "DYKX"

lista.append(dict2)

root["Body"] = repr(lista)
 
encoded = ujson.dumps(dict)

print(dict)

jsonReq =ujson.dumps(root)

response = urequests.post("http://192.168.0.124:5000/measurements",
                         headers = {'content-type': 'application/json'},
                         data =jsonReq)

#print(response.text)
#print(response.json())