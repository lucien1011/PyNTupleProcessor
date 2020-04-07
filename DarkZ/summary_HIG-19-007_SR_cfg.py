from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from DarkZ.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import *
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

plot_el = Plot("mZ2_el",["TH1D","mZ2_el","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4e_str+" or "+sel_2mu2e_str))
plot_mu = Plot("mZ2_mu",["TH1D","mZ2_mu","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4mu_str+" or "+sel_2e2mu_str))
plots = [
        plot_el,
        plot_mu,
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
    p.plotSetting.leg_pos = [0.60,0.75,0.89,0.90]
    p.plotSetting.linear_max_factor = 1.5
    if "mZ2" in p.key:
        p.customHistDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))
    p.plotSetting.leg_name_dict = {
            "HZZd_M30": "H #rightarrow Z Z_{d} , m_{X} = 30 GeV, #varepsilon = 0.05",
            "HZZd_M15": "H #rightarrow Z Z_{d} , m_{X} = 15 GeV, #varepsilon = 0.05",
            "ZPlusX": "Z+X",
            }

plot_el.plotSetting.custom_latex_list = [
       BaseObject(plot_el.key,x_pos=2.,y_pos=11.,text_size=0.035,text="2e channel",),
       ]
plot_mu.plotSetting.custom_latex_list = [
       BaseObject(plot_mu.key,x_pos=2.,y_pos=35.,text_size=0.035,text="2#mu channel",),
       ]

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
