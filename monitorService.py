import dht
from machine import Pin, SoftSPI
from objects import *
from collections import namedtuple

class EnvironmentMonitor:
    sensor = dht.DHT11(Pin(2))

    def getTempAndHumidity(self, timestamp):
        self.sensor.measure()
        temp = self.sensor.temperature()
        humi = self.sensor.humidity()
        
        tempMeasurement = Measurement("Temperature",temp,"C",timestamp)
        humiMeasurement = Measurement("Humidity",humi,"%",timestamp)
        
        MyTuple = namedtuple("MyTuple",("Temperature", "Humidity"))
        t1 = MyTuple(tempMeasurement,humiMeasurement)
        
        return t1