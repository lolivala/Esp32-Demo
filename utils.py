import ujson

def getConfigSettings():
    
    settings = {}

    with open('config.json') as fp:
        settings = ujson.load(fp)
        #print(str(settings))
        #print(type(settings))
    return settings
 
#c = ConfigHelper()
#c.getConfigSettings()