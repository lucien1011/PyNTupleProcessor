from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2018.SkimTree_DarkPhoton_m4l70 import * 
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_ppZZd4l import * 
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer
#from DarkZ.Config.PlotDefinition import *
from DarkZ.Config.AnalysisNotePlot import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.MergeSampleDict import mergeSampleDict

import ROOT,os

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-04-02_Run2018/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-05-07_Run2018/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-07-09_Run2018/"
#out_path                = "DarkPhotonSR/ShapeTemplate/2019-07-29_Run2018/"
out_path                = "DarkPhotonSR/ShapeTemplate/2019-08-23_Run2018/"
lumi                    = 59.7
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + [data2018] #+ [HZZd_M4,HZZd_M15,HZZd_M30,] 
componentList           = bkgSamples + [HZZd_M15,HZZd_M30,ppZZd4l_M15,ppZZd4l_M30,] + [data2018,] 
justEndSequence         = False

plots = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

for sig in sigSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_width_dict[sig.name] = 4
        p.plotSetting.line_color_dict[sig.name] = ROOT.kRed
for sig in ppZZdSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 9
        p.plotSetting.line_width_dict[sig.name] = 4
        p.plotSetting.line_color_dict[sig.name] = ROOT.kOrange

#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
variableProducer        = VariableProducer("VariableProducer")

sequence                = darkphoton_signal_sequence
#sequence                = higgs_m4lNarrowWindow_sequence
sequence.add(variableProducer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))
