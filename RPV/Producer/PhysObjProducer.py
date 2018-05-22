import ROOT

from Core.Collection import Collection
from Core.Module import Module

from RPV.Config.PhysObjDefinition import *

from Core.Utils.XCleaning import cleanJetsAndLeptons

class PhysObjProducer(Module):
    def __init__(self,name,inCollName,outCollName,selection):
        self.name = name
        self.inCollName = inCollName
        self.outCollName = outCollName
        self.selection = selection
    
    def begin(self):
        pass

    def analyze(self, event):
        phyObjs = Collection(event, self.inCollName)
        selObjs = [phyObj for phyObj in phyObjs if phyObjDefDict[self.selection](phyObj)]
        setattr(event,self.outCollName,selObjs)
        return True

class JetProducer(Module):
    def __init__(self,name,inCollName,inOtherCollNames,outCollName,selection,deltaR):
        self.name = name
        self.inCollName = inCollName
        self.inOtherCollNames = inOtherCollNames
        self.outCollName = outCollName
        self.selection = selection
        self.deltaR = deltaR

    def analyze(self,event):
        jets = Collection(event,self.inCollName)
        selectedJets = [j for j in jets if phyObjDefDict[self.selection](j)]
        for inOtherCollName in self.inOtherCollNames:
            selectedJets,_ = cleanJetsAndLeptons(selectedJets,getattr(event,inOtherCollName),self.deltaR)
        setattr(event,self.outCollName,selectedJets)
        return True
