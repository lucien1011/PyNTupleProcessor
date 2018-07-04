# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from DarkZ.Dataset.Run2017.MC import * 
#from DarkZ.Dataset.Run2017.SkimTree import * 

from DarkZ.Skimmer.Preskimmer import Preskimmer
from DarkZ.Skimmer.OSSFLeptonSkimmer import OSSFLeptonSkimmer

from NanoAOD.Producer.GenWeightCounter import *
from NanoAOD.EndModule.CutflowEndModule import CutflowEndModule

#out_path = "Higgs/DarkZ/SignalEfficiency/EventSelection_v1/Log/20180630/"
out_path = "Higgs/DarkZ/CutflowEfficiency/test/Log/20180703/"

nCores = 1
outputDir = "/raid/raid7/lucien/"+out_path
nEvents = -1
disableProgressBar = True
justEndSequence = True
componentList = [ggH]

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 77.30
    for component in dataset.componentList:
        component.maxEvents = nEvents

preskimmer              = Preskimmer("Preskimmer")
OSSFskimmer             = OSSFLeptonSkimmer("OSSFLeptonSkimmer")
OSSFCounter             = GenWeightCounter("GenWeightCounter",postfix="OSSF")

sequence = Sequence()
sequence.add(preskimmer)
sequence.add(OSSFskimmer)
sequence.add(OSSFCounter)

cutflows = [
        "OSSF",
        ]

cutflowEndModule = CutflowEndModule("/home/lucien/public_html/"+out_path,cutflows=cutflows)

endSequence = EndSequence(skipHadd=justEndSequence)
endSequence.add(cutflowEndModule)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "EventWeight.root"
