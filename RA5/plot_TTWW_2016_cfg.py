# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Config.MergeSampleDefinition import mergeSampleDict
#from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from RA5.Sequence.RecoSequence import sr_sequence

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

#from DataMC.Heppy.Run2016.SampleDefinition import * 
from RA5.Dataset.Run2016.Oct18_v1_TTWW import sigComponentDict
from RA5.Dataset.Run2016.Sept18_v1_skim import *

if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/Sync2016/2018-09-13_HLTEmulation/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    out_path = "SigBkgDistribution/2018-10-17/"
    outputDir = "/raid/raid7/lucien/FirstLook/TTWW/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
lepCats = ["HH","HL","LL"]

nCores = 4
nEvents = -1
disableProgressBar = False
justEndSequence = False
verbose = False
#componentList = allMCSamples + [Data_Run2016B,] 
componentList = [c for c in componentDict.values() if not (("WJets" in c.name and "HT" in c.name) or ("DYJets" in c.name and "HT" in c.name)) ] + sigComponentDict.values()
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
        #dataset.lumi = 5.93
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = []
for lepCat in lepCats:
    plots.extend(
        [
        Plot("nJet40"+lepCat,      ["TH1D","nJet40"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA540[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        #Plot("nJet40JECUp"+lepCat,  ["TH1D","nJet40JECUp"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA540_jecUp[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        #Plot("nJet40JECDown"+lepCat,  ["TH1D","nJet40JECDown"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA540_jecDown[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nJet25"+lepCat,      ["TH1D","nJet25"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA525[0]')              ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nBJet40"+lepCat,     ["TH1D","nBJet40"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMediumRA540[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nBJet25"+lepCat,     ["TH1D","nBJet25"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMediumRA525[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nLepTight"+lepCat,    ["TH1D","nLepTight"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: len(x.tightLeps)')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("htJet"+lepCat,       ["TH1D","htJet"+lepCat,"",12,0.,1200.],         LambdaFunc('x: x.htJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("met_pt"+lepCat,      ["TH1D","met_pt"+lepCat,"",10,0., 500.],          LambdaFunc('x: x.met_pt[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("met_phi"+lepCat,     ["TH1D","met_phi"+lepCat,"",10,-5, 5.],          LambdaFunc('x: x.met_phi[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("mht"+lepCat,         ["TH1D","mht"+lepCat,"",10,0., 500.],          LambdaFunc('x: x.mhtJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("mtmin"+lepCat,         ["TH1D","mtmin"+lepCat,"",20,0., 200.],          LambdaFunc('x: x.mtmin')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        
        Plot("LepTightPt1"+lepCat,    ["TH1D","LepTightPt1"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.tightLeps[0].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightEta1"+lepCat,    ["TH1D","LepTightEta1"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.tightLeps[0].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPhi1"+lepCat,    ["TH1D","LepTightPhi1"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.tightLeps[0].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPt2"+lepCat,    ["TH1D","LepTightPt2"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.tightLeps[1].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightEta2"+lepCat,    ["TH1D","LepTightEta2"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.tightLeps[1].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPhi2"+lepCat,    ["TH1D","LepTightPhi2"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.tightLeps[1].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        ]
        )
plotter                 = Plotter("Plotter",plots)

sequence = sr_sequence
sequence.add(plotter)

endSequence = EndSequence(skipHadd=False,)
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "DataMCDistributions.root"
