import ROOT

from Core.NanoAODResult.Collection import Collection
from Core.Module import Module

from RPV.Config.PhysObjDefinition import *

from Utils.XCleaning import cleanJetsAndLeptons

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

mediumMuonProducer      = PhysObjProducer("MediumMuonProducer","Muon","MediumMuons","Moriond17MediumMuon")
looseMuonProducer       = PhysObjProducer("LooseMuonProducer","Muon","LooseMuons","Moriond17LooseMuon")
mediumElectronProducer  = PhysObjProducer("MediumElectronProducer","Electron","MediumElectrons","Moriond17MediumElectron")
looseElectronProducer   = PhysObjProducer("LooseElectronProducer","Electron","LooseElectrons","Moriond17LooseElectron")
jetProducer             = JetProducer("JetProducer","Jet",["MediumMuons","LooseMuons","MediumElectrons","LooseElectrons"],"LooseJets","Moriond17LooseJet",0.4)
