class Systematic(object):
    def __init__(self,name,process,correlation=None,factor=1.,systNamePrefix=""):
        self.name = name
        self.process = process
        self.correlation = correlation
        self.systNamePrefix = systNamePrefix
        self.factor= factor
        self.skipDC= False
        self.forceSymmetric = False
        self.forceNormalization = False

class lnNSystematic(Systematic):
    def __init__(self,name,process,magnitudeFunc=None,correlation=None,factor=1.,systNamePrefix=""):
        super(lnNSystematic,self).__init__(name,process,correlation=correlation,factor=factor,systNamePrefix=systNamePrefix)
        self.systType = "lnN"
        self.name = name
        self.process = process
        self.magnitudeFunc = magnitudeFunc
        self.correlation = correlation
    
    def getSystName(self):
        return self.name

class ShapeSystematic(Systematic):
    def __init__(self,name,process,correlation="",factior=1.,systNamePrefix=""):
        super(ShapeSystematic,self).__init__(name,process,correlation=correlation,factor=factor,systNamePrefix=systNamePrefix)
        self.systType = "shape"

    def getSystName(self):
        return self.name

class RateParameter(Systematic):
    def __init__(self,name,process,formulaStr,parameterStr,correlation=None):
        self.name = name
        self.process = process
        self.formulaStr = formulaStr
        self.parameterStr = parameterStr
        self.correlation = correlationi
