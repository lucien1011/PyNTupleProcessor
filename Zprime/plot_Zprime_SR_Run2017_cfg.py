from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 
from Zprime.Config.PlotDefinition import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict import mergeSampleDict

User                    = os.environ['USER']
out_path                = "SR/DataMCDistributions/2019-05-07_Run2017/"
lumi                    = 41.4
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [zpToMuMu_M15] 
justEndSequence         = True

plots = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

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
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/Zprime/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
