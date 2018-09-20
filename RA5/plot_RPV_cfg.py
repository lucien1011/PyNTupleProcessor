# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Config.MergeSampleDefinition import mergeSampleDict
#from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from RA5.Sequence.RecoSequence import rpv_sequence

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

#from RA5.Dataset.Run2016.Sept18_v1 import *
from RA5.Dataset.Run2016.Sept18_v1_Data import *
from RA5.Dataset.Run2016.Sept18_v1_skim import *

#if where == "hpg":
    #out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/RPV/DataMCDistributions/2018-09-12_HLTEmulation/"
    #outputDir = out_path
    #endModuleOutputDir = out_path 
#elif where == "ihepa":
    #out_path = "RPV/DataMCDistribution/2018-09-19_OnlyMET0To50/"
    #out_path = "RPV/DataMCDistribution/2018-09-19/"
    #outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    #endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path

#out_path = ""
outputDir = "./testPlot/"
endModuleOutputDir = "/home/kshi/public_html/RA5/tightleptons/"
lepCats = ["HH","HL","LL"]

nCores = 5
nEvents = -1
disableProgressBar = False
justEndSequence = False
verbose = False
#componentList = allMCSamples + allSignalSamples + [Data_Run2016B,]
#componentList = allMCSamples + [Data_Run2016B,]
#componentList = componentDict.values()
componentList = skimComponentDict.values() + dataComponentDict.values()
for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 35.9
        dataset.lumi = 5.93
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
        #Plot("nLepLoose"+lepCat,    ["TH1D","nLepLoose"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nLepLoose[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("htJet"+lepCat,       ["TH1D","htJet"+lepCat,"",20,0.,1000.],         LambdaFunc('x: x.htJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("met_pt"+lepCat,      ["TH1D","met_pt"+lepCat,"",25,0., 250.],          LambdaFunc('x: x.met_pt[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("met_phi"+lepCat,     ["TH1D","met_phi"+lepCat,"",10,-5, 5.],          LambdaFunc('x: x.met_phi[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("mht"+lepCat,         ["TH1D","mht"+lepCat,"",10,0., 500.],          LambdaFunc('x: x.mhtJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("mtmin"+lepCat,         ["TH1D","mtmin"+lepCat,"",20,0., 200.],          LambdaFunc('x: x.mtmin')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        
        Plot("LepTightPt1"+lepCat,    ["TH1D","LepTightPt1"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.tightLeps[0].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightEta1"+lepCat,    ["TH1D","LepTightEta1"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.tightLeps[0].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPhi1"+lepCat,    ["TH1D","LepTightPhi1"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.tightLeps[0].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPt2"+lepCat,    ["TH1D","LepTightPt2"+lepCat,"",20,0.,200.],      LambdaFunc('x: x.tightLeps[1].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightEta2"+lepCat,    ["TH1D","LepTightEta2"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.tightLeps[1].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPhi2"+lepCat,    ["TH1D","LepTightPhi2"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.tightLeps[1].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),


        Plot("JetPt1"+lepCat,    ["TH1D","JetPt1"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.selJets[0].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("JetEta1"+lepCat,    ["TH1D","JetEta1"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.selJets[0].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),

        Plot("JetPhi1"+lepCat,    ["TH1D","JetPhi1"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.selJets[0].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("JetPt2"+lepCat,    ["TH1D","JetPt2"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.selJets[1].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("JetEta2"+lepCat,    ["TH1D","JetEta2"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.selJets[1].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),

        Plot("JetPhi2"+lepCat,    ["TH1D","JetPhi2"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.selJets[1].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        ]
        )
plotter                 = Plotter("Plotter",plots)

sequence = rpv_sequence
sequence.add(plotter)

endSequence = EndSequence(skipHadd=False,)
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "DataMCDistributions.root"
