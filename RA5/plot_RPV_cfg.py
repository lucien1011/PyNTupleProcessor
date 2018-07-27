# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 
from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
from RA5.Skimmer.METSkimmer import METSkimmer
from RA5.Skimmer.LLHtSkimmer import LLHtSkimmer
from RA5.Producer.CategoryProducer import CategoryProducer
from RA5.Producer.NJet40Producer import NJet40Producer
from RA5.Config.MergeSampleDefinition import mergeSampleDict
#from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

#from DataMC.Heppy.Run2016.SampleDefinition import * 
from RA5.Dataset.Run2016 import *

from NanoAOD.Producer.GenWeightCounter import *

if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/Sync2016/2018-07-26/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    out_path = "SigBkgDistribution/2018-07-27/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
lepCats = ["HH","HL","LL"]

nCores = 1
nEvents = -1
disableProgressBar = False
justEndSequence = True
verbose = False
componentList = allMCSamples + allSignalSamples
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = []
for lepCat in lepCats:
    plots.extend(
        [
        Plot("nJet40"+lepCat,      ["TH1D","nJet40"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet40_recal')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nJet40JECUp"+lepCat,  ["TH1D","nJet40JECUp"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet40_jecUp[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nJet40JECDown"+lepCat,  ["TH1D","nJet40JECDown"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet40_jecDown[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nJet25"+lepCat,      ["TH1D","nJet25"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet25[0]')              ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nBJet40"+lepCat,     ["TH1D","nBJet40"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMedium40[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nBJet25"+lepCat,     ["TH1D","nBJet25"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMedium25[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nLepTight"+lepCat,    ["TH1D","nLepTight"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nLepTight[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("nLepLoose"+lepCat,    ["TH1D","nLepLoose"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nLepLoose[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("htJet"+lepCat,       ["TH1D","htJet"+lepCat,"",20,0.,2000.],         LambdaFunc('x: x.htJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("met_pt"+lepCat,      ["TH1D","met_pt"+lepCat,"",10,0., 500.],          LambdaFunc('x: x.met_pt[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("met_phi"+lepCat,     ["TH1D","met_phi"+lepCat,"",10,-5, 5.],          LambdaFunc('x: x.met_phi[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("mht"+lepCat,         ["TH1D","mht"+lepCat,"",10,0., 500.],          LambdaFunc('x: x.mhtJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        
        Plot("LepTightPt1"+lepCat,    ["TH1D","LepTightPt1"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.tightLeps[0].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightEta1"+lepCat,    ["TH1D","LepTightEta1"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.tightLeps[0].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPhi1"+lepCat,    ["TH1D","LepTightPhi1"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.tightLeps[0].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPt2"+lepCat,    ["TH1D","LepTightPt2"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.tightLeps[1].pt')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightEta2"+lepCat,    ["TH1D","LepTightEta2"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.tightLeps[1].eta')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        Plot("LepTightPhi2"+lepCat,    ["TH1D","LepTightPhi2"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.tightLeps[1].phi')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
        ]
        )
plotter                 = Plotter("Plotter",plots)
leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
xsWeighter              = XSWeighter("XSWeighter")
baselineSkimmer         = BaselineSkimmer("BaselineSkimmer")
metSkimmer              = METSkimmer("METSkimmer")
llHtSkimmer             = LLHtSkimmer("LLHtSkimmer")
categoryProducer        = CategoryProducer("CategoryProducer")
nJet40Producer           = NJet40Producer("NJet40Producer")

sequence = Sequence()
#sequence.add(leptonJetProducer)
#sequence.add(baselineSkimmer)
#sequence.add(metSkimmer)
sequence.add(categoryProducer)
sequence.add(llHtSkimmer)
sequence.add(nJet40Producer)
sequence.add(xsWeighter)
sequence.add(plotter)

endSequence = EndSequence(skipHadd=justEndSequence,)
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "MCDistributions.root"
