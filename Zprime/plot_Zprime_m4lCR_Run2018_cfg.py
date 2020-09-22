from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2018.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2018.SkimTree_Data_m4l70 import * 
from Zprime.Sequence.RecoSequence import m4lcr_sequence
from Zprime.Config.m4lCR_PlotDefinition import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict import mergeSampleDict

User                    = os.environ['USER']
out_path                = "DataMCDistributions/2020-09-02_m4lCR_Run2018/"
lumi                    = 59.7
nCores                  = 4
outputDir               = "/cmsuf/data/store/user/t2/users/klo/Zprime/UF-NTupleAnalyzer/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + rareBkgSamples + dataSamples
justEndSequence         = False

plots = general_4mu_plots

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = m4lcr_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = outputDir 
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
