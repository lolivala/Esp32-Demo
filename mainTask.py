import gc
import time
import dataUtils
from time import sleep
from objects import *
from monitorService import *
from dataAccess import *
from webClient import *

settings = dataUtils.getConfigSettings()
monitor = EnvironmentMonitor()
storage = LocalStorage()
apiClient = Webclient(settings["APIHostName"], settings["APIPort"])
    
def execute():
    try:
        ##sleep(settings["ReadRatio"])
     
        t = time.localtime()
                        
        timestamp = settings["TimeStampFormat"].format(t[0], t[1], t[2], t[3], t[4], t[5])    
                    
        tup = monitor.getTempAndHumidity(timestamp)
                    
        storage.createEntrylog(timestamp,t ,tup, settings)
                    
        document = DeviceMeasurements(settings["DeviceId"], settings["DeviceId"])
        document.addMeasurent(tup.Temperature)
                
        document.addMeasurent(tup.Humidity)
                    
        jsonData = document.getDataInJson()

        response = apiClient.postData(jsonData,"measurements",{'content-type': 'application/json'})
    except OSError as e:
        print('Failed to Exec Main Task.'+ str(e))
    finally:
        gc.collect()
        gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())    

