from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2018.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2018.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 
from Zprime.Config.PlotDefinition import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict import mergeSampleDict

User                    = os.environ['USER']
#out_path                = "SR/DataMCDistributions/2019-06-03_Run2017/"
#out_path                = "DataMCDistributions/Run2017/test/"
#out_path                = "DataMCDistributions/Run2018/2020-04-13_4Gev_CR/"
#out_path                = "DataMCDistributions/Run2018/2020-09-23_4Gev_CR/"
#out_path                = "DataMCDistributions/Run2018/2020-09-23_4Gev_SR/"
#out_path                = "DataMCDistributions/Run2018/2020-09-23_4Gev_mZ1_mZ2_fullrange/"
#out_path                = "DataMCDistributions/Run2018/2020-10-05_4Gev_signalcount_mZ2/"
#out_path                = "DataMCDistributions/Run2018/2020-10-05_4Gev_signalcount_mZ1_mZ2/"
out_path                = "DataMCDistributions/Run2018/2020-10-14_4Gev_signalcount_mZ2/"

lumi                    = 59.7
nCores                  = 5
outputDir               = system.getStoragePath()+"/Zprime/Zto4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + [sigSampleDict[m] for m in [10,40,70]]
#componentList           = bkgSamples + sigSampleDict.values()
#componentList           = sigSampleDict.values()
componentList           = sigSamples# + bkgSamples# + dataSamples 
justEndSequence         = False

plots = general_4mu_plots

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = signal_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Zprime/Zto4l/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
