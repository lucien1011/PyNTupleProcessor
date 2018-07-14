# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Common.TreeProducer import TreeProducer

from Config.BranchToAdd import branchesToAdd

from Core.Utils.LambdaFunc import LambdaFunc

import os,array

from DataMC.Heppy.Run2016.HaddMC import * 
from DataMC.Heppy.Run2016.SampleDefinition import * 

out_path = "./HeppyValidation/2018-07-13/"

nCores = 2
#outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
outputDir = out_path
nEvents = 10
disableProgressBar = False
justEndSequence = False
componentList = componentList[4:6]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

branchesToKeep = [
        "met_pt",
        ]

leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
xsWeighter              = XSWeighter("XSWeighter")
treeProducer            = TreeProducer("TreeProducer",listOfBranchesToKeep=branchesToKeep,branchesToAdd=branchesToAdd)

sequence = Sequence()
sequence.add(leptonJetProducer)
sequence.add(xsWeighter)
sequence.add(treeProducer)

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = out_path

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "MCDistributions.root"
