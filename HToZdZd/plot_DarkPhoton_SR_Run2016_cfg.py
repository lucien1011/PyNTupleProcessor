from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
#from HToZdZd.Dataset.Run2016.SkimTree_DarkSUSY_m4l70 import * 
from HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_HZdZd import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict import *
from HToZdZd.Config.AnalysisNotePlot import *

#out_path                = "DarkPhotonSR/DataMCDistributions/2019-02-15_MC_RatioCut0p05/" # Lucien's new dir
#out_path                = "DarkPhotonSR/DataMCDistributions/20190228_MassRatioCuts/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-03-31_Run2017_MC_RatioCut0p05/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-08-23_Run2016/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-09-06_Run2016/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-12-09_Run2016/"
out_path                = "DarkPhotonSR/DataMCDistributions/2019-12-11_Run2016/"
User                    = os.environ['USER']
lumi                    = 35.9
nCores                  = 5
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
sigSamples              = [ sigSampleDict[m] for m in [5,10,30,60,] ]
componentList           = bkgSamples + [
                                data2016,
                                ] + sigSamples
justEndSequence         = False

plots = general_plots 

for sig in sigSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_width_dict[sig.name] = 4

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

for p in plots:
    if p.dim == 2: 
        p.plotSetting.leg_pos = [0.14,0.65,0.34,0.87]
        p.plotSetting.x_axis_title = "m_{Z1}"
        p.plotSetting.y_axis_title = "m_{Z2}"
        p.plotSetting.minimum = 0.
        p.selectedSamples = ["Higgs","qqZZ",] + [sigSampleDict[m].name for m in [5,30,60]]

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_unblind_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
