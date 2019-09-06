from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from DarkZ.Dataset.Run2017.SkimTree_DarkPhoton_m4l70 import * 
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import HZZd_M15,HZZd_M30
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_ppZZd4l import * 
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer
#from DarkZ.Config.PlotDefinition import *
from DarkZ.Config.AnalysisNotePlot import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from DarkZ.Config.MergeSampleDict import mergeSampleDict

import ROOT,os,copy

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/ShapeTemplate/2019-07-25_Run2016/"
#out_path                = "DarkPhotonSR/ShapeTemplate/2019-07-29_Run2017/"
#end_out_path            = "DarkPhotonSR/ShapeTemplate/2019-07-29_Run2017/"
#out_path                = "DarkPhotonSR/ShapeTemplate/2019-08-23_Run2017/"
#end_out_path            = "DarkPhotonSR/ShapeTemplate/2019-08-23_Run2017/"
out_path                = "DarkPhotonSR/ShapeTemplate/2019-09-05_Run2017/"
end_out_path            = "DarkPhotonSR/ShapeTemplate/2019-09-05_Run2017/"
lumi                    = 41.7
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
sigSamples              = [HZZd_M15,HZZd_M30,ppZZd4l_M15,ppZZd4l_M30,]
componentList           = bkgSamples + [data2017,] + sigSamples
justEndSequence         = False

plots = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape.root"),"READ")
for p in plots:
    p.plotSetting.divideByBinWidth = False
    if p.plotSetting.divideByBinWidth: p.plotSetting.bin_width_label = "Bin Width"
    if "mZ2" in p.key:
        p.customHistDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))
        #p.customPdfDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))
        #p.customPdfDict = {}
        #leptonChannel = p.key.split("_")[-1]
        #p.customPdfDict["ZPlusX"] = BaseObject(p.key,hist=inputShapeFile.Get("mZ2"+"_"+leptonChannel+"_shapehist").Clone(p.key))

for sig in sigSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_width_dict[sig.name] = 4
        p.plotSetting.line_color_dict[sig.name] = ROOT.kRed
for sig in ppZZdSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 9
        p.plotSetting.line_width_dict[sig.name] = 4
        p.plotSetting.line_color_dict[sig.name] = ROOT.kOrange

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+end_out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
