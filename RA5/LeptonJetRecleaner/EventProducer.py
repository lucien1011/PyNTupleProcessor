from Core.Module import Module

from RA5.LeptonJetRecleaner.LeptonDict import leptonAlgoDict

import pprint

class LeptonJetProducer(Module):
    def __init__(self,name,algoStr):
        self.name = name
        self.algoStr = algoStr

    def analyze(self,event):
        event.ret = leptonAlgoDict[self.algoStr](event)
        return True
