from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Plotter.Plotter import Plotter
from Plotter.PlotSetting import PlotSetting
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from LJMet.Sequence.RecoSequence import *

#from LJMet.Dataset.LJMet_step1_tptp2017 import *
#from LJMet.Dataset.FWLJMet_step1_tptp2017 import *
from LJMet.Dataset.FWLJMET102X_1lep2017Dnn_071519_step1 import *

from LJMet.Config.MergeSampleDict import mergeSampleDict
from LJMet.Config.Plot_Run2017 import plots

import os

User                    = os.environ["USER"]
#out_path                = "CR/DataMCDistributions/2019-05-29_Run2017/"
#out_path                = "CR/DataMCDistributions/2019-07-25_Run2017/"
out_path                = "CR/DataMCDistributions/2019-07-31_Run2017_SyncPreSelection/"
lumi                    = 41.298
nCores                  = 6
outputDir               = out_path #system.getStoragePath()+"/"+User+"/LJMet/B2G/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [b for b in bkgSamples] + dataSamples
justEndSequence         = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence = cr_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=False,)
endModuleOutputDir = out_path #system.getPublicHtmlPath()+"/LJMet/B2G/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots, skipSF=False))
