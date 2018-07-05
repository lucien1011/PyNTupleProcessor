# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

useSkimTree = False
if useSkimTree:
    from RPV.SkimTree.NanoAOD.Run2016.MC import *
else:
    from DataMC.NanoAOD.Run2016 import * 

from NanoAOD.Producer.GenWeightCounter import *

nCores = 8
#outputDir = "/raid/raid7/lucien/SUSY/RPV/SumGenWeight/NanoAOD_InclusiveSelection_v2/"
outputDir = "/raid/raid7/kshi/SUSY/RPV/sum_weight/"
nEvents = -1
disableProgressBar = False
justEndSequence = False
componentList = allMCSamples

sequence = Sequence()
eventWeightCount = GenWeightCounter("GenWeightCounter")
sequence.add(eventWeightCount)

endSequence = EndSequence()

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "EventWeight.root"
