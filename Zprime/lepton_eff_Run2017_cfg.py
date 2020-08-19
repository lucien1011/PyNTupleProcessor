from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

#from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
#from Zprime.Dataset.Run2017.SkimTree_promptCR_Bkg_m4l70 import *
from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 
from Zprime.Config.PlotDefinition import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict import mergeSampleDict

from Zprime.Module.Lepeff import Lepeff
from Zprime.Module.Lepeff_ratio import Lepeff_ratio

#from Zprime.Skimmer.printing import printing

User                    = os.environ['USER']
#out_path                = "DataMCDistributions/Run2017/lepeff_signal/"
#out_path                = "DataMCDistributions/Run2017/Zp_GENLep_deltaR/"
out_path                = "DataMCDistributions/Run2017/lepeff_fourlepevent_signal/"
lumi                    = 41.4
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Zprime/Zto4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
haddSamples             = True
componentList           = sigSamples
justEndSequence         = True

plots = []
#plots = general_4mu_plots

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
lepeff                  = Lepeff("Lepeff")
#printing                = printing("printing")

sequence                = eff_sequence
#sequence.add(printing)
sequence.add(lepeff)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence, haddAllSamples=haddSamples)
endModuleOutputDir = system.getPublicHtmlPath()+"/Zprime/Zto4l/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
endSequence.add(Lepeff_ratio(endModuleOutputDir))
