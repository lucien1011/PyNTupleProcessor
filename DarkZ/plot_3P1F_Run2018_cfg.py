
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2018.ZXCR_MC_DarkPhoton import * 
from DarkZ.Dataset.Run2018.ZXCR_Data_DarkPhoton import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.ZXCRPlot import *
from DarkZ.Config.MergeSampleDict import mergeSampleDict

#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2018Data_m4l118-130/2019-04-02_3P1F_DataVsPred_FRWeightFromVukasinWZRemoved/"
#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2018Data_m4l100-170/2019-05-23_3P1F_DataVsPred_FRWeightFromVukasinWZRemoved/"
out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2018Data_m4l118-130/2020-02-28_3P1F_DataVsPred_FRWeightFromVukasinWZRemoved/"

plots =  general_plots

#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

predCR.isSignal         = False

nCores                  = 5
outputDir               = system.getStoragePath()+"/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [Data_Run2018,predCR,WZTo3LNu,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        #dataset.lumi = 35.9
        dataset.lumi = 59.7
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_3p1f_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
