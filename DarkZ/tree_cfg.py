from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo

from DarkZ.Dataset.Run2017.Data import * 
from DarkZ.Dataset.Run2017.BkgMC import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
from DarkZ.Skimmer.RecoSkimmer import RecoSkimmer

from Common.TreeProducer import TreeProducer

nCores                  = 8
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180728/"
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + sigSamples + [data2017]
componentList           = [qqToZZ,ggToZZ]
justEndSequence         = True

for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = Sequence()
recoSkimmer             = RecoSkimmer("RecoSkimmer")
recoSkimmer.Z2MassRange = [4.,120.]
treeProducer            = TreeProducer("TreeProducer")

sequence.add(recoSkimmer)
sequence.add(treeProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "SkimTree.root"

endSequence = EndSequence(skipHadd=False)
