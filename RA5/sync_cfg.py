# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Sequence.RecoSequence import sr_sequence

from RA5.Producer.YieldCounter import YieldCounter
from RA5.Config.MergeSampleDefinition import mergeSampleDict

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
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/Sync2016/2018-07-23/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    out_path = "Sync2016/2018-08-23/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
lepCats = ["HH","HL","LL"]

nCores = 1
nEvents = -1
disableProgressBar = False
justEndSequence = True
verbose = False
componentList = allMCSamples
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

#plots = []
#for lepCat in lepCats:
#    plots.extend(
#        [
#        Plot("nJet40"+lepCat,      ["TH1D","nJet40"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet40_recal')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("nJet40JECUp"+lepCat,  ["TH1D","nJet40JECUp"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet40_jecUp[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("nJet40JECDown"+lepCat,  ["TH1D","nJet40JECDown"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet40_jecDown[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("nJet25"+lepCat,      ["TH1D","nJet25"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJet25[0]')              ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("nBJet40"+lepCat,     ["TH1D","nBJet40"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMedium40[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("nBJet25"+lepCat,     ["TH1D","nBJet25"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMedium25[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("nLepTight"+lepCat,    ["TH1D","nLepTight"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nLepTight[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("nLepLoose"+lepCat,    ["TH1D","nLepLoose"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nLepLoose[0]')        ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("htJet"+lepCat,       ["TH1D","htJet"+lepCat,"",10,0.,1000.],         LambdaFunc('x: x.htJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("met_pt"+lepCat,      ["TH1D","met_pt"+lepCat,"",10,0., 500.],          LambdaFunc('x: x.met_pt[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("met_phi"+lepCat,     ["TH1D","met_phi"+lepCat,"",10,-5, 5.],          LambdaFunc('x: x.met_phi[0]')           ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        Plot("mht"+lepCat,         ["TH1D","mht"+lepCat,"",10,0., 500.],          LambdaFunc('x: x.mhtJet40[0]')            ,selFunc=LambdaFunc('x: x.cat.lepCat == \"%s\"'%lepCat)),
#        ]
#        )
#plotter                 = Plotter("Plotter",plots)
yieldCounter            = YieldCounter("YieldCounter")

sequence = sr_sequence 
sequence.add(yieldCounter)
#sequence.add(plotter)

#endSequence = EndSequence(skipHadd=False,)
#endSequence.add(PlotEndModule(endModuleOutputDir,plots))

endSequence = EndSequence(haddAllSamples=True)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SyncFile.root"