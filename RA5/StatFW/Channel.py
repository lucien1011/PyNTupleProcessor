class Bin(object):
    """
    A class to input informtion for each bin in the data card, i.e. 4mu, 4e and 2e2mu
    """
    def __init__(self,name,signalName="SMS",sysFile="test.txt",inputBinName=""):
        self.name = name
        self.processList = []
        self.signalName = signalName
        self.sysFile = sysFile
        self.inputBinName = inputBinName
       
    def isSignal(self,name):
        return self.signalName in name
