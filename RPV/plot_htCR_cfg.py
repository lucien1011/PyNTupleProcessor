# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from NanoAOD.Weighter.XSWeighter import XSWeighter
from NanoAOD.Weighter.PUWeighter import PUWeighter
from NanoAOD.Skimmer.JSONSkimmer import JSONSkimmer

from RPV.Producer.PhysObjProducer import PhysObjProducer,JetProducer 
from RPV.Producer.AnalysisProducer import AnalysisProducer 

from RPV.Skimmer.EventSkimmer import EventSkimmer
from RPV.Skimmer.HLTSkimmer import HLTSkimmer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc

import os

useSkimTree = True
if useSkimTree:
    from RPV.SkimTree.NanoAOD.Run2016.MC import allMCSamples
    from RPV.SkimTree.NanoAOD.Run2016.Data import allDataSamples
else:
    from DataMC.NanoAOD.Run2016 import * 

out_path = "StopToBLep/DataMCDistributions/DataMC_htCRSelection_v1/2018-06-18/"

nCores = 8 
outputDir = "/raid/raid7/lucien/SUSY/RPV/"+out_path
nEvents = -1
disableProgressBar = True
justEndSequence = False
componentList = allDataSamples + allMCSamples 
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 5.93
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = [
        Plot("nJet40",      ["TH1D","nJet40","",10,-0.5,9.5],       LambdaFunc('x: x.nJet40')),
        Plot("nBJet25",     ["TH1D","nBJet25","",10,-0.5,9.5],      LambdaFunc('x: len([j for j in x.LooseJets if j.btagCSVV2 > 0.8484])')),
        Plot("nLep40",      ["TH1D","nLep40","",10,-0.5,9.5],       LambdaFunc('x: x.nLep40')),
        Plot("met",         ["TH1D","met","",10,0., 500.],          LambdaFunc('x: x.MET_pt[0]')),
        Plot("ht40",        ["TH1D","ht40","",10,0.,1000.],         LambdaFunc('x: x.ht40')),
        Plot("mll",         ["TH1D","mll","",10,0.,500.],           LambdaFunc('x: x.mll if x.mll else -1.')),
        Plot("jetPt1",      ["TH1D","jetPt1","",10,0., 500.],       LambdaFunc('x: x.jets[0].pt if len(x.jets) > 0 else -1')),
        Plot("jetEta1",     ["TH1D","jetEta1","",10,-3.,3.],        LambdaFunc('x: x.jets[0].eta if len(x.jets) > 0 else -1')),
        Plot("jetPhi1",     ["TH1D","jetPhi1","",10,-4.,4.],        LambdaFunc('x: x.jets[0].phi if len(x.jets) > 0 else -1')),
        Plot("jetmuEF1",    ["TH1D","jetmuEF1","",20,0.,1.],        LambdaFunc('x: x.jets[0].muEF if len(x.jets) > 0 else -1')),
        Plot("jetchEF1",    ["TH1D","jetchEF1","",20,0.,1.],        LambdaFunc('x: x.jets[0].chEmEF+x.jets[0].chHEF if len(x.jets) > 0 else -1')),
        Plot("jetchEmEF1",  ["TH1D","jetchEmEF1","",20,0.,1.],      LambdaFunc('x: x.jets[0].chEmEF if len(x.jets) > 0 else -1')),
        Plot("jetchHEF1",   ["TH1D","jetchHEF1","",20,0.,1.],       LambdaFunc('x: x.jets[0].chHEF if len(x.jets) > 0 else -1')),
        Plot("jetPt2",      ["TH1D","jetPt2","",10,0., 500.],       LambdaFunc('x: x.jets[1].pt if len(x.jets) > 1 else -1')),
        Plot("muonPt1",     ["TH1D","muonPt1","",10,0., 500.],      LambdaFunc('x: x.muons[0].pt if len(x.muons) > 0 else -1')),
        Plot("muonPt2",     ["TH1D","muonPt2","",10,0., 500.],      LambdaFunc('x: x.muons[1].pt if len(x.muons) > 1 else -1')),
        Plot("elePt1",      ["TH1D","elePt1","",10,0., 500.],       LambdaFunc('x: x.eles[0].pt if len(x.eles) > 0 else -1')),
        Plot("elePt2",      ["TH1D","elePt2","",10,0., 500.],       LambdaFunc('x: x.eles[1].pt if len(x.eles) > 1 else -1')),
        Plot("nGoodPV",     ["TH1D","nGoodPV","",30,0.0,60.0],      LambdaFunc('x: x.PV_npvsGood[0]')),
        ]
puWeighter              = PUWeighter("PUWeighter",os.environ["BASE_PATH"]+"/DataMC/Pileup/puWeightsRun2016_NTrueInt_FullDataset--Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",doNTrueInt=True,applySystVariation=True)
xsWeighter              = XSWeighter("XSWeighter")
mediumMuonProducer      = PhysObjProducer("MediumMuonProducer","Muon","MediumMuons","Moriond17MediumMuon")
mediumElectronProducer  = PhysObjProducer("MediumElectronProducer","Electron","MediumElectrons","Moriond17MediumElectron")
jetProducer             = JetProducer("JetProducer","Jet",["MediumMuons","MediumElectrons"],"LooseJets","Moriond17LooseJet",0.4)
plotter                 = Plotter("Plotter",plots)
anaProducer             = AnalysisProducer("AnaProducer")
eventSkimmer            = EventSkimmer("StopToBLepSkim",cutflow="htCR")
hltSkimmer              = HLTSkimmer("HLTSkim",cutflow="htCR")
jsonSkimmer             = JSONSkimmer("JSONSkim")

sequence = Sequence()
sequence.add(jsonSkimmer)
sequence.add(hltSkimmer)
sequence.add(mediumMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(jetProducer)
sequence.add(xsWeighter)
sequence.add(puWeighter)
sequence.add(anaProducer)
sequence.add(eventSkimmer)
sequence.add(plotter)

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/SUSY/RPV/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "DataMCDistribution.root"
