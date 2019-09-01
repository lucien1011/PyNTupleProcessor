from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from HToZdZd.Dataset.Run2017.SkimTree_DarkPhoton_m4l70 import * 
#from HToZdZd.Dataset.Run2016.SkimTree_DarkSUSY_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_HToZdZd_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict import *
from HToZdZd.Config.AnalysisNotePlot import *

import ROOT,os,copy

User                    = os.environ['USER']
out_path                = "DarkPhotonSR/DataMCDistributions/2019-08-23_Run2017/"
end_out_path            = "DarkPhotonSR/DataMCDistributions/2019-08-23_Run2017/"
nCores                  = 3
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
sigSamples              = [      
                                #HToZdZd_MZD4,
                                HToZdZd_MZD5,
                                #HToZdZd_MZD6,
                                #HToZdZd_MZD7,
                                #HToZdZd_MZD8,
                                #HToZdZd_MZD9,
                                HToZdZd_MZD10,
                                #HToZdZd_MZD15, 
                                #HToZdZd_MZD20,
                                #HToZdZd_MZD25,
                                HToZdZd_MZD30,
                                #HToZdZd_MZD35,
                                #HToZdZd_MZD40,
                                #HToZdZd_MZD45,
                                #HToZdZd_MZD50,
                                #HToZdZd_MZD55,
                                HToZdZd_MZD60,
                                ]
componentList           = bkgSamples + [
                                data2017,
                                ] + sigSamples
justEndSequence         = False

plots = general_mu_plots + general_el_plots

inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape.root"),"READ")
for p in plots:
    p.plotSetting.divideByBinWidth = False
    if p.plotSetting.divideByBinWidth: p.plotSetting.bin_width_label = "Bin Width"
    if p.key in ["mZ2_mu", "mZ2_el"]:
        p.customHistDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))
        #p.customPdfDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))
        #p.customPdfDict = {}
        #leptonChannel = p.key.split("_")[-1]
        #p.customPdfDict["ZPlusX"] = BaseObject(p.key,hist=inputShapeFile.Get("mZ2"+"_"+leptonChannel+"_shapehist").Clone(p.key))

for sig in sigSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_width_dict[sig.name] = 4

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
