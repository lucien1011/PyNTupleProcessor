from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZdZd.Dataset.Run2017.SkimTree_DarkPhoton_m4l70 import * 
#from HToZdZd.Dataset.Run2016.SkimTree_DarkSUSY_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_DarkPhoton_m4l70_HZdZd import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict import *
from HToZdZd.Config.AnalysisNotePlot import *

out_path                = "DarkPhotonSB/DataMCDistributions/2020-02-29_Run2017/"
User                    = os.environ['USER']
lumi                    = 41.4
nCores                  = 5
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
sigSamples              = [ sigSampleDict[m] for m in [5,10,30,60,] ]
componentList           = bkgSamples + [
                                data2017,
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
        p.selectedSamples = ["ggH","qqZZ",] + [sigSampleDict[m].name for m in [5,30,60]]
    else:
        p.plotSetting.divideByBinWidth = True

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_unblind_sequence
sequence.remove(windowSkimmer)
sequence.add(invertWindowSkimmer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
