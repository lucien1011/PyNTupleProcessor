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
from RA5.Dataset.Run2016.Oct18_v1_SMS import sigComponentList_plot

if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/RPV/DataMCDistributions/2018-09-12_HLTEmulation/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    out_path = "SignalRegion/YieldPlot/2018-10-16/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path

nCores = 5
nEvents = -1
disableProgressBar = False
justEndSequence = False
verbose = False
componentList = skimComponentDict.values() + dataComponentDict.values()
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = [
        
        Plot("rpv_HH_sr",["TH1D","rpv_sr","",16,52.5,68.5],LambdaFunc('x: x.SRCategory'),selFunc=LambdaFunc('x: x.leptonCategory == \"HH\" and x.met_pt[0] < 50.')),
        Plot("baseline_HH_sr",["TH1D","baseline_sr","",52,0.5,52.5],LambdaFunc('x: x.SRCategory'),selFunc=LambdaFunc('x: x.leptonCategory == \"HH\" and x.met_pt[0] > 50.')),
        ]
plotter                 = Plotter("Plotter",plots)

sequence = rpv_sequence
sequence.add(plotter)

endSequence = EndSequence(skipHadd=justEndSequence,)
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "YieldPlot.root"
