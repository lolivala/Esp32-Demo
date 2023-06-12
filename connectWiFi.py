import dataUtils
import network

def connect():
    
    print("Step 1")
    settings = dataUtils.getConfigSettings()
    ssid = settings["ssid"]
    password = settings["ssidPassword"]
    
    print("Step 2")
    station = network.WLAN(network.STA_IF)
 
    print("Step 3")
    station.active(True)
    station.connect(ssid, password)
    
    print("Step 4")
    while station.isconnected() == False:
      pass

    print("Connection successful")
    print(station.ifconfig())