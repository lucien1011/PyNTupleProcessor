# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from DataMC.NanoAOD.Run2016 import * 

from RPV.Producer.PhysObjProducer import PhysObjProducer,JetProducer 
from RPV.Producer.TreeProducer import TreeProducer
from RPV.Producer.AnalysisProducer import AnalysisProducer 
from RPV.Skimmer.ZMuMuSkimmer import ZMuMuSkimmer

nCores = 4 
#outputDir = "/raid/raid7/lucien/SUSY/RPV/SkimTree/ZMuMu/2018-06-19/BkgMC_ZMuMuSelection_v1/"
outputDir = "/raid/raid7/kshi/SUSY/RPV/SkimTree/mc/ZToMuMu/"
nEvents = -1
disableProgressBar = False
justEndSequence = False 
componentList = allMCSamples 
for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

mediumMuonProducer      = PhysObjProducer("MediumMuonProducer","Muon","MediumMuons","Moriond17MediumMuon")
mediumElectronProducer  = PhysObjProducer("MediumElectronProducer","Electron","MediumElectrons","Moriond17MediumElectron")
jetProducer             = JetProducer("JetProducer","Jet",["MediumMuons","MediumElectrons"],"LooseJets","Moriond17LooseJet",0.4)
eventSkimmer            = ZMuMuSkimmer("ZMuMuSkim")
treeProducer            = TreeProducer("TreeProducer")

sequence = Sequence()
sequence.add(mediumMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(jetProducer)
sequence.add(eventSkimmer)
sequence.add(treeProducer)

endSequence = EndSequence()

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SkimTree.root"
