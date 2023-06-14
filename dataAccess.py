from machine import Pin, SoftSPI
from sdcard import SDCard
import os
import gc

#Pin assignment
#  MISO -> GPIO 13
#  MOSI -> GPIO 12
#  SCK  -> GPIO 14
#  CSD  -> GPIO 27
class LocalStorage:
    
    spisd = SoftSPI(-1,
                    miso=Pin(13),
                    mosi=Pin(12),
                    sck=Pin(14))
    
    sd = SDCard(spisd,Pin(27))
    
    vfs = None
    
    def __init__(self):
        try:
            #print('Root directory: {}'.format(os.listdir()))
            self.vfs = os.VfsFat(self.sd)
            os.mount(self.vfs,'/sd')
            #print('Root directory: {}'.format(os.listdir()))
            os.chdir('sd')
            #print('SD Card containst: {}'.format(os.listdir()))
        except OSError as e:
            print('Error on Data Access: '+ str(e.args[0]))
        finally:
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())


    def createEntrylog(self, timestamp, t, tup, settings):
        try:
            directoryName = settings["DirectoryNameFormat"].format(t[0], t[1], t[2])
            fileName = settings["FileNameFormat"].format(t[0], t[1], t[2], t[3])
            
            
            newRow = '{},{:3.1f}C,{:3.1f}%'.format(timestamp,
                                        tup.Temperature.measurementvalue,
                                        tup.Humidity.measurementvalue)
            
            dirList = os.listdir()
            #print('dirList=',dirlist)
            print(newRow)
            
            if directoryName not in dirList:
                os.mkdir(directoryName)
                        
            os.chdir(directoryName)
            
            #print('{}: {}'.format(directorName,os.listdir()))
            fileList = os.listdir()
            
            if fileName not in fileList:
                f = open(fileName, 'w')
                f.write(newRow)
                f.close()
            else:
                f = open(fileName, 'a')
                f.write('\n'+ newRow)
                f.close()
            
            os.chdir('..')
        except OSError as e:
            print('Error on Data Access: '+ str(e.args[0]))
        finally:
            gc.collect()
            gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())