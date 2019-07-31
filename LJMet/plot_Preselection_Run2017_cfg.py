from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from LJMet.Sequence.RecoSequence import *

#from LJMet.Dataset.FWLJMet_step1_tptp2017 import *
from LJMet.Dataset.FWLJMET102X_1lep2017Dnn_071519_step1 import *

from LJMet.Config.MergeSampleDict import mergeSampleDict
from LJMet.Config.Plot_Run2017 import plots

import os

User                    = os.environ["USER"]
#out_path                = "Preselection/DataMCDistributions/2019-03-31_Run2017_test/"
#out_path                = "Preselection/DataMCDistributions/2019-07-24_Run2017_noPileUpWeight/"
out_path                = "Preselection/DataMCDistributions/2019-07-31_Run2017_SyncPreSelection/"
lumi                    = 41.298
nCores                  = 6
#outputDir               = system.getStoragePath()+"/"+User+"/LJMet/B2G/"+out_path
outputDir               = out_path
nEvents                 = -1
disableProgressBar      = False
#sigSamples              = [sigDict["TT_M1200_BW-BW"]]
sigSamples              = []
componentList           = bkgSamples + dataSamples #[b for b in bkgSamples if 'DYMG1200' in b.name] #+ dataSamples #+ sigSamples
justEndSequence         = False

for sigSample in sigSamples:
    sigSample.xs *= 100.
    for p in plots:
        p.plotSetting.leg_name_dict[sigSample.name] = " ".join(sigSample.name.split("_")[:2])+" #times 100"

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence = pre_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=False,)
#endModuleOutputDir = system.getPublicHtmlPath()+"/LJMet/B2G/"+out_path
endModuleOutputDir = out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots, skipSF=False))
