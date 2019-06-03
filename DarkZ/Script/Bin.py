class Bin(object):
    def __init__(self,
            histName,
            width=None,
            yieldFunc=None,
            latexName=None,
            ):
        self.histName = histName
        self.width = width
        self.yieldFunc = yieldFunc
        self.latexName = latexName

    def getWindowWidth(self,centre):
        return centre*(1.-self.width),centre*(1.+self.width)

