from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.SkimTree_SMHiggs import * 
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton import * 
#from DarkZ.Dataset.Run2017.SignalMC import * 

from DarkZ.Sequence.RecoSequence import * 

from DarkZ.StatTools.MassWindow import MassWindow
from DarkZ.StatTools.YieldProducer import YieldProducer
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "MCDistributions/MC_BaselineSelection_v1/2018-07-09/"
#out_path = "StatInput/DarkPhotonSelection_v1/2018-08-20/"
#out_path = "StatInput/DarkPhotonSelection_ATLAS-BrHToZZd100_v1/2018-08-20/"
#out_path = "StatInput/DarkPhotonSelection_m4l118To130/2018-08-31/"
out_path = "StatInput/DarkPhotonSelection_m4l118To130_Nominal/2018-09-21/"
#out_path = "StatInput/DarkPhotonSelection_m4l118To130_UniformIso/2018-09-21/"
#out_path = "StatInput/DarkPhotonSelection_m4l105To140/2018-08-31/"

mergeSampleDict = {
        "ggH":  ["ggH"],
        "VBF":  ["VBF"],
        "WH":   ["WHPlus","WHminus",],
        "ZH":   ["ZH",],
        "qqZZ": ["qqZZTo4L",],
        "ggZZ": [
            "ggZZTo2e2mu",
            "ggZZTo2e2tau",
            "ggZZTo2mu2tau",
            "ggZZTo4e",
            "ggZZTo4mu",
            "ggZZTo4tau",
            ],
        "ZPlusX": ["ZPlusX"],
        }

mass_window_list = [
        MassWindow(4,0.02),
        MassWindow(7,0.02),
        MassWindow(10,0.02),
        MassWindow(15,0.02),
        MassWindow(20,0.02),
        MassWindow(25,0.02),
        MassWindow(30,0.02),
        ]

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSamples + [data2016]
justEndSequence         = False
skipGitDetail           = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 77.30
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = darkphoton_signal_sequence
#variableProducer        = VariableProducer("VariableProducer")
yieldProducer           = YieldProducer("YieldProducer",mass_window_list)

#sequence.add(variableProducer)
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

#endSequence = EndSequence(skipHadd=justEndSequence)
endSequence = EndSequence(skipHadd=False)
