import time
import utils
from time import sleep
from objects import *
from monitorService import *
from dataAccess import *
from webClient import *

try:
    settings = utils.getConfigSettings()
    
    monitor = EnvironmentMonitor()
    storage = LocalStorage()
    apiClient = Webclient(settings["HostName"], settings["Port"])

    while True:
        document = None
        jsonData = ""
        sleep(5)
        t = time.localtime()
        
        timestamp = settings["TimeStampFormat"].format(t[0], t[1], t[2], t[3], t[4], t[5])
        directoryname =settings["DirectoryNameFormat"].format(t[0], t[1], t[2])
        filename = settings["FileNameFormat"].format(t[0], t[1], t[2], t[3])    
             
        tup = monitor.getTempAndHumidity(timestamp)
        
        newRow = '{},{:3.1f}C,{:3.1f}%'.format(timestamp,
                                               tup.Temperature.measurementvalue,
                                               tup.Humidity.measurementvalue)
        
        storage.createEntrylog(newRow,directoryname,filename)
        
        document = DeviceMeasurements(settings["DeviceId"],settings["SensorId"])
        document.addMeasurent(tup.Temperature)
        document.addMeasurent(tup.Humidity)
        
        jsonData = document.getDataInJson()

        response = apiClient.postData(jsonData,"measurements",{'content-type': 'application/json'})
          
except OSError as e:
    print('Failed to read sensor.')
