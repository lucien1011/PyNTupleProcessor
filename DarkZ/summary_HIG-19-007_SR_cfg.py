from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from DarkZ.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import *
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer
#from DarkZ.Config.PlotDefinition import *
from DarkZ.Config.AnalysisNotePlot import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from DarkZ.Config.MergeSampleDict_RunII import mergeSampleDict,mergeSigSampleDict

import ROOT,os,copy

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-18_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-03-18_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-19_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-03-19_RunII/"
out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-27_RunII/"
end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-03-27_RunII/"
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
skipHadd                = True
componentList           = bkgSamples + dataSamples + sigSamples 
mZ2PlotRange            = [36,0.,36.]

plots = [
        Plot("mZ2_el",["TH1D","mZ2_el","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4e_str+" or "+sel_2mu2e_str)),
        Plot("mZ2_mu",["TH1D","mZ2_mu","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4mu_str+" or "+sel_2e2mu_str)),
        ]

#inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape.root"),"READ")
inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","PlotShape.root"),"READ")
for p in plots:
    p.plotSetting.tdr_style = True
    p.plotSetting.divideByBinWidth = True
    p.plotSetting.cms_lumi = True
    p.plotSetting.skip_leg_err = True
    p.plotSetting.skip_data_mc_ratio = False
    p.plotSetting.shift_last_bin = False
    p.plotSetting.bin_width_label = "Event / bin"
    p.plotSetting.x_axis_title = "m_{Z2} [GeV]"
    if "mZ2" in p.key:
        p.customHistDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))

for sigName in mergeSigSampleDict:
    for p in plots:
        p.plotSetting.line_style_dict[sigName] = 1
        p.plotSetting.line_width_dict[sigName] = 3

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(
        skipHadd=skipHadd,
        skipComponentHadd=skipHadd,
        )
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+end_out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))
