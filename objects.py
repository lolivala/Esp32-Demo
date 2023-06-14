import gc
import ujson

class Device:
    nodeId = ""
    name = ""
    location =""
    ipAddress = ""
    
class Sensor:
    sensorId = ""
    sensorName = ""
    sensorType = ""  
    manufacturer = ""
    port = ""
    readRate= ""

class Measurement:
    measurementId = ""
    measurementName = ""
    measurementvalue = ""
    unitOfMeasure = ""
    dateTime = ""

    def __init__(self, measurementName, measurementvalue, unitOfMeasure, dateTime):
        self.measurementName = measurementName
        self.measurementvalue = measurementvalue
        self.unitOfMeasure = unitOfMeasure
        self.dateTime = dateTime

class DeviceMeasurements:
    deviceId = ""
    sensorId = ""
    measurements = []
    
    def __init__(self, deviceId, sensorId):
        self.sensorId = sensorId
        self.deviceId = deviceId
        self.measurements = []
        
    def addMeasurent(self, measurement):
        self.measurements.append(measurement)

    def getDataInJson(self):
        mainDict = {}
        arrayMes = []
        try:
            mainDict["DeviceId"] = self.deviceId 
            mainDict["SensorId"] = self.sensorId
            
            for m in self.measurements:
                dict = {}
                dict["MeasurementName"] = m.measurementName
                dict["Measurementvalue"] = m.measurementvalue
                dict["UnitOfMeasure"] = m.unitOfMeasure
                dict["DateTime"] = m.dateTime
                arrayMes.append(dict)
            
            mainDict["Measurements"] = arrayMes
            
            #return ujson.dumps(mainDict)
        except OSError as e:
            print('Error on objets: '+ str(e.args[0]))
        finally:
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())
            return ujson.dumps(mainDict)


#document = DeviceMeasurements("sdafsfsdaf","retrewrrtr")
#document.addMeasurent(Measurement("Temperature","100","C", "2023-06-06"))
#document.addMeasurent(Measurement("Humidity","55","%", "2023-06-06"))
#document.addMeasurent(Measurement("Soil Humidity","35","%", "2023-06-06"))

#print(document.getDataInJson())

