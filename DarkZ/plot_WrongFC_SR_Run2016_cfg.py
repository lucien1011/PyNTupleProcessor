
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2016.WrongFC_MC import * 
from DarkZ.Dataset.Run2016.WrongFC_Data import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.WrongFCPlot import *
from DarkZ.Config.MergeSampleDict import mergeSampleDict

#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l70_Run2016Data_v1/2018-09-20/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l108To140_Run2016Data_v1/2018-10-24_SR/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l118To130_Run2016Data_v1/2019-01-21_SR/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l70/2019-03-08_SR_FRWeightUniIso/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-08_SR_FRWeight-mZ2-6/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l70/2019-03-08_SR_FRWeight-mZ2-6/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-08_SR_FRWeight-mZ2-6/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-08_SR/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-13_SR_FRWeight-mZ2-6/"
out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l100-170/2019-05-23_SR_FRWeight-mZ2-6/"

plots =  general_plots

#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 3
outputDir               = system.getStoragePath()+"/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [qqZZTo4L,Data_Run2016,WFC_Reducible,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = wrongFC_signal_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
