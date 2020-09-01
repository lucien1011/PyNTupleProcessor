from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZaToLLGG.Dataset.Run2017.Bkg_NanoAODv1_ihepa import * 
from HToZaToLLGG.Dataset.Run2017.ALP_PrivateSample_ihepa import * 
#from HToZaToLLGG.Dataset.Run2017.Bkg_NanoAODv1_hpg import * 
#from HToZaToLLGG.Dataset.Run2017.ALP_PrivateSample_hpg import * 
from HToZaToLLGG.Sequence.RecoSequence import * 
from HToZaToLLGG.Config.KinematicPlot import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

import ROOT,os

User                    = os.environ['USER']
#out_path                = "SignalRegion/2020-01-30_Run2017/"
#out_path                = "SignalRegion/2020-02-03_Run2017/"
out_path                = "SignalRegion/2020-02-04_Run2017/"
lumi                    = 41.4
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/HToZaToLLGG/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [ZGGToLLGG,ALP_HToZa_M15,ALP_HToZa_M30,]
justEndSequence         = False

plots = lepton_plots + photon_plots + general_plots

for p in plots:
    p.plotSetting.line_color_dict[ALP_HToZa_M15.name] = ROOT.kRed
    p.plotSetting.line_color_dict[ALP_HToZa_M30.name] = ROOT.kBlue

#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = sr_resolved_sequence 
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/HToZaToLLGG/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
