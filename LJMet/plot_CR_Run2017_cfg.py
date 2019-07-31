from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Plotter.Plotter import Plotter
from Plotter.PlotSetting import PlotSetting
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from LJMet.Sequence.RecoSequence import *

#from LJMet.Dataset.LJMet_step1_tptp2017 import *
from LJMet.Dataset.FWLJMet_step1_tptp2017 import *

from LJMet.Config.MergeSampleDict import mergeSampleDict
from LJMet.Config.Plot_Run2017 import plots

import os

User                    = os.environ["USER"]
#out_path                = "CR/DataMCDistributions/2019-05-29_Run2017/"
out_path                = "CR/DataMCDistributions/2019-07-25_Run2017/"
lumi                    = 41.298
nCores                  = 5
outputDir               = out_path #system.getStoragePath()+"/"+User+"/LJMet/B2G/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples
justEndSequence         = True
eventSelection          = LambdaFunc("x: x.minDR_leadAK8otherAK8[0] > 3.")

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots += [
        Plot("AK4HT_0b0H",        ["TH1D","AK4HT_0b0H","",25,500.0,3000.0],	LambdaFunc('x: x.AK4HT[0]'),plotSetting=PlotSetting(x_axis_title="AK4 H_{T}"), selFunc=LambdaFunc("x: x.NJetsH1btagged[0] == 0 and x.NJetsH2btagged[0] == 0 and x.NJetsCSV_JetSubCalc[0] == 0")),
        Plot("AK4HT_1b0H",        ["TH1D","AK4HT_1b0H","",25,500.0,3000.0],	LambdaFunc('x: x.AK4HT[0]'),plotSetting=PlotSetting(x_axis_title="AK4 H_{T}"), selFunc=LambdaFunc("x: x.NJetsH1btagged[0] == 0 and x.NJetsH2btagged[0] == 0 and x.NJetsCSV_JetSubCalc[0] > 0")),
        Plot("AK4HT_1b1H",        ["TH1D","AK4HT_1b1H","",25,500.0,3000.0],	LambdaFunc('x: x.AK4HT[0]'),plotSetting=PlotSetting(x_axis_title="AK4 H_{T}"), selFunc=LambdaFunc("x: (x.NJetsH1btagged[0] >= 0 or x.NJetsH2btagged[0] > 0) and x.NJetsCSV_JetSubCalc[0] > 0")),
        ]

plotter                 = Plotter("Plotter",plots)

sequence = cr_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=False,)
endModuleOutputDir = out_path #system.getPublicHtmlPath()+"/LJMet/B2G/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots, skipSF=True))
