class Plot(object):
    def __init__(self,key,rootSetting,funcObj,isCollection=False,selFunc=None):
        self.key = key
        self.rootSetting = rootSetting
        self.funcObj = funcObj
        self.isCollection = isCollection
        self.selFunc = selFunc

    def getWriterSetting(self):
        return [self.key]+self.rootSetting

    def getValues(self,event):
        if not self.isCollection:
            return [self.funcObj(event)]
        else:
            return self.funcObj(event)
