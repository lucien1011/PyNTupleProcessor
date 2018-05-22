# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

useSkimTree = True
if useSkimTree:
    from RPV.SkimTree.NanoAOD.Run2016.MC import *
else:
    from DataMC.NanoAOD.Run2016 import * 

from NanoAOD.Producer.GenWeightCounter import *

nCores = 8 
outputDir = "/raid/raid7/lucien/SUSY/RPV/SumGenWeight/NanoAOD_BaselineSelection_v1/"
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
