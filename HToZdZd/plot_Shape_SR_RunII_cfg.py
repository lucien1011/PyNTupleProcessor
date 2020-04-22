from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from HToZdZd.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import * 
#from HToZdZd.Dataset.Run2016.SkimTree_DarkSUSY_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_HToZdZd_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict_RunII import *
from HToZdZd.Config.AnalysisNotePlot import *

import ROOT,os,copy

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-09-06_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2019-09-06_RunII/"
out_path                = "DarkPhotonSR/DataMCDistributions/2020-02-29_RunII/"

out_path                = "DarkPhotonSR/DataMCDistributions/2020-02-29_RunII/"
nCores                  = 3
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples + sigSamples
justEndSequence         = False

plots = general_plots 

#inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape.root"),"READ")
inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","PlotShape.root"),"READ")
for p in plots:
    p.plotSetting.divideByBinWidth = True 
    if p.plotSetting.divideByBinWidth: p.plotSetting.bin_width_label = "Bin Width"
    if p.key in [
            "mZ2_4mu","mZ2_4e","mZ2_2e2mu","mZ2_2mu2e",
            "mZ12_4mu","mZ12_4e","mZ12_2e2mu","mZ12_2mu2e",
            ]:
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

endSequence = EndSequence(skipHadd=True)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False,))
