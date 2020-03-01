from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import *
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer
#from DarkZ.Config.PlotDefinition import *
from DarkZ.Config.AnalysisNotePlot import *
#from DarkZ.Config.AnalysisNotePlot_MassWindowBinning import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from DarkZ.Config.MergeSampleDict_RunII import mergeSampleDict

import os,ROOT

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-05-24_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-06-12_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-08-21_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-09-09_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-09-10_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-12-02_RunII/"
out_path                = "DarkPhotonSR/DataMCDistributions/2020-02-28_RunII/"
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + sigSamples + ppZZdSamples
#componentList           = bkgSamples + [sample2016.HZZd_M15,sample2016.HZZd_M30] + [sample_ppZZd.ppZZd4l_M15,sample_ppZZd.ppZZd4l_M30]
componentList           = bkgSamples + dataSamples + sigSamples
justEndSequence         = True

plots = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots + general_mu_plots + general_el_plots

for sample in ["HZZd_M"+str(m) for m in [5,20,30]]:
    if sample not in mergeSampleDict:
        mergeSampleDict[sample] = []
    mergeSampleDict[sample].append(sample+"_Run2016")
    mergeSampleDict[sample].append(sample+"_Run2017")
    mergeSampleDict[sample].append(sample+"_Run2018")

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

for dataset in componentList:
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
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
