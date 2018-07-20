# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

#from DataMC.NanoAOD.Run2016 import *

from RA5.Producer.GenWeightCounter import *
from RA5.Dataset.Run2016 import *

nCores = 8 
outputDir = "/raid/raid7/kshi/SUSY/RA5/sum_weight/"
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
