
# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

from Example.Dataset.Data_Sept18_v1 import *
from Example.Dataset.MC_Sept18_v1 import *

from Example.Module.JetProducer import JetProducer
from Example.Module.LeptonProducer import LeptonProducer
from Example.Module.TightLeptonSkimmer import TightLeptonSkimmer
from Example.Module.VariableProducer import VariableProducer

out_path                = "./testPlot/"
outputDir               = out_path
endModuleOutputDir      = out_path 

nCores                  = 4
nEvents                 = -1
disableProgressBar      = False
justEndSequence         = False
verbose                 = False

componentList           = dataComponentDict.values() + [DYJetsToLL_M10to50_LO,DYJetsToLL_M50_LO_ext,]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots                   = [
     
                    ]
plotter                 = Plotter("Plotter",plots)
leptonProducer          = LeptonProducer("LeptonProducer")
jetProducer             = JetProducer("JetProducer")
variableProducer        = VariableProducer("VariableProducer")
skimmer                 = TightLeptonSkimmer("TightLepSkimmer")

sequence                = Sequence()
sequence.add(leptonProducer)
sequence.add(jetProducer)
sequence.add(skimmer)
sequence.add(variableProducer)
sequence.add(plotter)

endSequence             = EndSequence(skipHadd=False,)
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistributions.root"
