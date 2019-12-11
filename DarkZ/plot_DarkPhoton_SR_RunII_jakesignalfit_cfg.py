from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

#from DarkZ.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import sigSamples
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_HZZdInterpolation import sigSamples
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer
from DarkZ.Config.PlotDefinition import *
#from DarkZ.Config.AnalysisNotePlot import *
#from DarkZ.Config.AnalysisNotePlot_MassWindowBinning import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from DarkZ.Config.MergeSampleDict_RunII import mergeSampleDict

import os,ROOT
from shutil import copyfile

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-05-24_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-06-12_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-08-21_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-09-09_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-09-10_RunII/"
out_path                = "DarkPhotonSR/DataMCDistributions/HToZZd_Run2016_mXtoll_gausfit_nocutbelow4GeV/"
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path  # Usually /raid/raid7/
php_output_dir          = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path 
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + sigSamples + ppZZdSamples
#componentList           = bkgSamples + [sample2016.HZZd_M15,sample2016.HZZd_M30] + [sample_ppZZd.ppZZd4l_M15,sample_ppZZd.ppZZd4l_M30]
#componentList           = bkgSamples + dataSamples
componentList           = sigSamples
justEndSequence         = False

php_input_dir = "/home/rosedj1/"
#if not os.path.exists(outputDir):
#    os.makedirs(outputDir)
if not os.path.exists(php_output_dir):
    os.makedirs(php_output_dir)
copyfile(php_input_dir+"index.php",php_output_dir+"index.php")

plots = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

for sig in sigSamples:
    count = 0
    for p in plots:
#        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_style_dict[sig.name] = 1
        p.plotSetting.line_width_dict[sig.name] = 4
        p.plotSetting.line_color_dict[sig.name] = 0 + count
#        p.plotSetting.line_color_dict[sig.name] = ROOT.kRed
        count += 1
#for sig in ppZZdSamples:
#    for p in plots:
#        p.plotSetting.line_style_dict[sig.name] = 9
#        p.plotSetting.line_width_dict[sig.name] = 4
#        p.plotSetting.line_color_dict[sig.name] = ROOT.kOrange

for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
variableProducer        = VariableProducer("VariableProducer")

sequence                = darkphoton_nomX2cut_signal_sequence
#sequence                = darkphoton_signal_sequence
#sequence                = higgs_m4lNarrowWindow_sequence
sequence.add(variableProducer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
