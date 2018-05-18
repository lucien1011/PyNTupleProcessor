# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from DataMC.NanoAOD.Run2016 import *

from RA5.Producer.GenWeightCounter import *

nCores = 8 
outputDir = "/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/"
nEvents = -1
disableProgressBar = False
justEndSequence = True
componentList = [
    TToLeptons_sch,
    T_tch,
    T_tWch,
    TBar_tWch,
    ]

sequence = Sequence()
eventWeightCount = GenWeightCounter("GenWeightCounter")
sequence.add(eventWeightCount)

endSequence = EndSequence()

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "EventWeight.root"
