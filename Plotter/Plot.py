from PlotSetting import PlotSetting

class Plot(object):
    def __init__(self,key,rootSetting,funcObj,isCollection=False,selFunc=None,dim=1,plotSetting=None,getEventWeight=None,customHistDict=None):
        self.key = key
        self.rootSetting = rootSetting
        self.funcObj = funcObj
        self.isCollection = isCollection
        self.selFunc = selFunc
        self.dim = dim
        self.plotSetting = plotSetting if plotSetting else PlotSetting()
        if self.isCollection and self.dim == 2:
            raise RuntimeError,"Can't do collection and dim2 at the same time"
        self.getEventWeight = getEventWeight
        self.customHistDict = {} if not customHistDict else customHistDict

    def getWriterSetting(self):
        return [self.key]+self.rootSetting

    def getValues(self,event):
        if not self.isCollection and not self.dim == 2:
            return [self.funcObj(event)]
        else:
            return self.funcObj(event)

    def end(self):
        self.funcObj.end()
        if self.selFunc:
            self.selFunc.end()
        if self.getEventWeight:
            self.getEventWeight.end()
