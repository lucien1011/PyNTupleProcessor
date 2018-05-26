from PlotSetting import PlotSetting

class Plot(object):
    def __init__(self,key,rootSetting,funcObj,isCollection=False,selFunc=None,dim=1,plotSetting=None):
        self.key = key
        self.rootSetting = rootSetting
        self.funcObj = funcObj
        self.isCollection = isCollection
        self.selFunc = selFunc
        self.dim = dim
        self.plotSetting = plotSetting if plotSetting else PlotSetting()

    def getWriterSetting(self):
        return [self.key]+self.rootSetting

    def getValues(self,event):
        if not self.isCollection:
            return [self.funcObj(event)]
        else:
            return self.funcObj(event)

    def end(self):
        self.funcObj.end()
