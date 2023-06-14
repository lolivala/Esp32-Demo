#import webrepl
#webrepl.start()
import gc
import esp
import connectWiFi
import micropython
  
try:
  import usocket as socket
except:
  import socket

#micropython.alloc_emergency_exception_buf(100)

esp.osdebug(None)
gc.collect()
gc.enable()
#gc.disable()

connectWiFi.connect()