from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2018.SkimTree_Bkg_m4l70 import * 
#from Zprime.Dataset.Run2018.SkimTree_promptCR_Bkg_m4l70 import *
from Zprime.Dataset.Run2018.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 
from Zprime.Config.PlotDefinition import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict import mergeSampleDict

from Zprime.Module.PlotforFit import PlotforFit
from Zprime.Module.Fit import Fit

#from Zprime.Skimmer.printing import printing

User                    = os.environ['USER']
out_path                = "DataMCDistributions/Run2018/fit_gaus/"
lumi                    = 59.7
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Zprime/Zto4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
haddSamples             = True
componentList           = sigSamples #bkgSamples #sigSamples
justEndSequence         = True

plots = []
#plots = general_4mu_plots

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
plotforfit              = PlotforFit("PlotforFit")
#printing                = printing("printing")

sequence                = signal_sequence
#sequence.add(printing)
sequence.add(plotforfit)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence, haddAllSamples=haddSamples)
endModuleOutputDir = system.getPublicHtmlPath()+"/Zprime/Zto4l/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
endSequence.add(Fit(endModuleOutputDir))
