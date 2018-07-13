# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from DarkZ.Dataset.Run2017.SkimTree import * 

from DarkZ.Skimmer.AnalysisSkimmer import AnalysisSkimmer

from NanoAOD.Producer.GenWeightCounter import *
from NanoAOD.EndModule.EfficiencyEndModule import EfficiencyEndModule

out_path = "Higgs/DarkZ/SignalEfficiency/EventSelection_v1/Log/20180630/"

nCores = 8
outputDir = "/raid/raid7/lucien/"+out_path
nEvents = -1
disableProgressBar = False
justEndSequence = True
componentList = sigSamples

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 77.30
    for component in dataset.componentList:
        component.maxEvents = nEvents

anaSkimmer              = AnalysisSkimmer("AnalysisSkimmer")
genWeightCounter        = GenWeightCounter("GenWeightCounter")

sequence = Sequence()
sequence.add(anaSkimmer)
sequence.add(genWeightCounter)

efficiencyEndModule = EfficiencyEndModule("/home/lucien/public_html/"+out_path)

endSequence = EndSequence(skipHadd=justEndSequence)
endSequence.add(efficiencyEndModule)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "EventWeight.root"
