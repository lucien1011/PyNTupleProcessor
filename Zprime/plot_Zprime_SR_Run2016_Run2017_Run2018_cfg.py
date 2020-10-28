from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

#from Zprime.Dataset.Run2016.SkimTree_Bkg_m4l70 import *
#from Zprime.Dataset.Run2016.SkimTree_Zprime_m4l70 import *
#from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
#from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Dataset.Run161718.SkimTree_Zprime_m4l70 import *
from Zprime.Sequence.RecoSequence import * 
from Zprime.Config.PlotDefinition import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict_161718 import mergeSampleDict

#User                    = os.environ['USER']
User                    = "kshi"
#out_path                = "SR/DataMCDistributions/2019-06-03_Run2017/"
#out_path                = "DataMCDistributions/Run2016_Run2017/2020-02-24/"
#out_path                = "DataMCDistributions/Run2016_Run2017_Run2018/2020-04-13_4Gev_CR/"
#out_path                = "DataMCDistributions/Run2016_Run2017_Run2018/2020-09-23_4Gev_CR/"
out_path                = "DataMCDistributions/Run2016_Run2017_Run2018/2020-09-23_4Gev_SR/"

#lumi                    = 41.4
nCores                  = 5
outputDir               = system.getStoragePath()+"/Zprime/Zto4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + [sigSampleDict[m] for m in [10,40,70]]
#componentList           = bkgSamples + sigSampleDict.values()
#componentList           = sigSampleDict.values()
componentList           = bkgSamples# + dataSamples# + sigSamples
justEndSequence         = False

plots = general_4mu_plots

for dataset in componentList:
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
