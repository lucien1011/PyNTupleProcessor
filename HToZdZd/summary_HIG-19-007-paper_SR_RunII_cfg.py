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
from HToZdZd.Config.AnalysisNotePlot import sel_4e_str,sel_4mu_str,sel_2mu2e_str,sel_2e2mu_str

import ROOT,os,copy

User                    = os.environ['USER']
out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-18_RunII/"

end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-03-18_RunII/"
nCores                  = 3
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples + sigSamples
justEndSequence         = False
mZ12PlotRange           = [15,4.,60.]

plots = [ 
        Plot("mZ12_4e",["TH1D","mZ12_4e","",]+mZ12PlotRange,LambdaFunc('x: (x.massZ1[0]+x.massZ2[0])/2.'),selFunc=LambdaFunc('x: '+sel_4e_str)), 
        Plot("mZ12_4mu",["TH1D","mZ12_4mu","",]+mZ12PlotRange,LambdaFunc('x: (x.massZ1[0]+x.massZ2[0])/2.'),selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mZ12_2e2mu",["TH1D","mZ12_2e2mu","",]+mZ12PlotRange,LambdaFunc('x: (x.massZ1[0]+x.massZ2[0])/2.'),selFunc=LambdaFunc('x: '+sel_2mu2e_str+" or "+sel_2e2mu_str)),
        ]

#inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape.root"),"READ")
inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","PlotShape.root"),"READ")
for p in plots:
    p.plotSetting.tdr_style = True
    p.plotSetting.cms_lumi = True
    p.plotSetting.divideByBinWidth = True
    p.plotSetting.linear_max_factor = 4.
    p.plotSetting.x_axis_title = "(m_{Z1}+m_{Z2})/2 [GeV]"
    p.plotSetting.skip_data_mc_ratio = True
    p.plotSetting.skip_leg_err = True
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

for sigName in mergeSigSampleDict:
    for p in plots:
        p.plotSetting.line_style_dict[sigName] = 1
        p.plotSetting.line_width_dict[sigName] = 3

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=True)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+end_out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True,))
