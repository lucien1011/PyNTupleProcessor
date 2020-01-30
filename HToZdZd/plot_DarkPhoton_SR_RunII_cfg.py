from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZdZd.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict_RunII import *
from HToZdZd.Config.AnalysisNotePlot import *

import os,ROOT

#out_path                = "DarkPhotonSR/DataMCDistributions/2019-05-24_RunII_MC_RatioCut0p05/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-08-19_RunII_MC_RatioCut0p05/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-08-23_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-12-19_RunII/"
out_path                = "DarkPhotonSR/DataMCDistributions/2020-01-20_RunII/"
User                    = os.environ['USER']
nCores                  = 3
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + dataSamples + sigSamples
#sigSamples              = [ sigSampleDict[m] for m in [5,10,30,60,] ]
sigSamples              = []
componentList           = bkgSamples + dataSamples + sigSamples
justEndSequence         = False

plots = general_plots 

for sig in sigSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_width_dict[sig.name] = 4

for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

for p in plots:
    if p.dim == 2: 
        p.plotSetting.leg_pos = [0.39,0.70,0.59,0.92]
        p.plotSetting.x_axis_title = "m_{Z1}"
        p.plotSetting.y_axis_title = "m_{Z2}"
        p.plotSetting.minimum = 0.
        p.plotSetting.marker_size = 0.7
        p.plotSetting.marker_style_dict = {
                "Higgs": 21,
                "qqZZ": 22,
                "ggZZ": 23,
                "Data": 34,
                }
        p.plotSetting.marker_color_dict = {
                "qqZZ": ROOT.kOrange,
                "ggZZ": ROOT.kGreen,
                "Data": ROOT.kBlack
                }
        p.plotSetting.marker_size_dict = {
                "ggZZ": 0.4,
                "Data": 1.0,
                }
        p.plotSetting.scatter_density = "1.0"
        p.selectedSamples = ["Higgs","qqZZ","ggZZ","Data",]
        p.plotSetting.cms_lumi = True
        p.plotSetting.tdr_style = True
        p.plotSetting.SetNColumns = 4

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_unblind_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence,haddDataSamples=True,)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
