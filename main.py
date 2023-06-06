import time
from time import sleep
from objects import *
from monitorService import *
from dataAccess import *
from webClient import *
import utils

try:
    settings = utils.getConfigSettings()
    
    monitor = EnvironmentMonitor()
    storage = LocalStorage()
    apiClient = Webclient(settings["HostName"], settings["Port"])

    while True:
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
          
except OSError as e:
    print('Failed to read sensor.')
