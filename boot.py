# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import gc
import esp
import connectWiFi
  
try:
  import usocket as socket
except:
  import socket

connectWiFi.connect()

esp.osdebug(None)
gc.collect()