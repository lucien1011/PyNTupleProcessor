# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from NanoAOD.Weighter.XSWeighter import XSWeighter
from NanoAOD.Weighter.PUWeighter import PUWeighter
from NanoAOD.Skimmer.JSONSkimmer import JSONSkimmer
from NanoAOD.Skimmer.METFilter import METFilter

from RPV.Producer.PhysObjProducer import PhysObjProducer,JetProducer 
from RPV.Producer.AnalysisProducer import AnalysisProducer 

from RPV.Skimmer.TTbarSkimmer import TTbarSkimmer
#from RPV.Skimmer.ZMuMuSkimmer import ZMuMuSkimmer
from RPV.Skimmer.HLTSkimmer import HLTSkimmer
from RPV.Weighter.Triggereff import Triggereff
from RPV.Weighter.Btageff import Btageff
#from RPV.Weighter.BtagscaleFactor import BtagscaleFactor

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from RPV.Module.Btageff_ratio import Btageff_ratio
from Plotter.Plot import Plot

#from Core.Utils.LambdaFunc import LambdaFunc

import os

useSkimTree = True
if useSkimTree:
    from RPV.SkimTree.NanoAOD.Run2016.TTbarBtageff_MC import allMCSamples
    #from RPV.SkimTree.NanoAOD.Run2016.ZToMuMu_Data import allDataSamples
else:
    from DataMC.NanoAOD.Run2016 import * 

#out_path = "StopToBLep/DataMCDistributions/DataMC_ZToMuMuSelection_v1/2018-06-19/"

nCores = 1 
#outputDir = "/raid/raid7/lucien/SUSY/RPV/"+out_path
outputDir = "./BTag_ZMuMu/"
nEvents = -1
disableProgressBar = False
justEndSequence = True
componentList = allMCSamples
#componentList = allDataSamples + allMCSamples 
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = []

puWeighter              = PUWeighter("PUWeighter",os.environ["BASE_PATH"]+"/DataMC/Pileup/puWeightsRun2016_NTrueInt_FullDataset--Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",doNTrueInt=True,applySystVariation=True)
xsWeighter              = XSWeighter("XSWeighter")
mediumMuonProducer      = PhysObjProducer("MediumMuonProducer","Muon","MediumMuons","Moriond17MediumMuon")
mediumElectronProducer  = PhysObjProducer("MediumElectronProducer","Electron","MediumElectrons","Moriond17MediumElectron")
jetProducer             = JetProducer("JetProducer","Jet",["MediumMuons","MediumElectrons"],"LooseJets","Moriond17LooseJet",0.4)
plotter                 = Plotter("Plotter",plots)
anaProducer             = AnalysisProducer("AnaProducer")
eventSkimmer            = TTbarSkimmer("TTbarSkim")
#eventSkimmer            = ZMuMuSkimmer("ZMuMuSkim")
hltSkimmer              = HLTSkimmer("HLTSkim",cutflow="htCR")
jsonSkimmer             = JSONSkimmer("JSONSkim")
metSkimmer              = METFilter("METSkim")
triggereff              = Triggereff("Triggereff")
btageff                 = Btageff("Btageff")
#btagscalefactor         = BtagscaleFactor("BtagscaleFactor")


sequence = Sequence()
sequence.add(metSkimmer)
sequence.add(jsonSkimmer)
sequence.add(hltSkimmer)
sequence.add(mediumMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(jetProducer)
sequence.add(xsWeighter)
sequence.add(puWeighter)
sequence.add(anaProducer)
sequence.add(eventSkimmer)
sequence.add(triggereff)
sequence.add(btageff)
#sequence.add(btagscalefactor)
sequence.add(plotter)

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/kshi/public_html/test/"
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
endSequence.add(Btageff_ratio(endModuleOutputDir))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "DataMCDistribution.root"
