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
from DarkZ.EndModule.PaperPlotEndModule import PaperPlotEndModule

from DarkZ.Config.MergeSampleDict_RunII import mergeSampleDict,mergeSigSampleDict
from DarkZ.Config.CMS_lumi import CMS_lumi

import ROOT,os,copy,math

User                    = os.environ['USER']
out_path                = "DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-06-04_RunII/"
end_out_path            = "DarkPhotonSR/DataMCDistributions/2021-01-29_RunII/"

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
    p.plotSetting.divideByBinWidth = False
    p.plotSetting.cms_lumi = CMS_lumi
    p.plotSetting.skip_leg_err = True
    p.plotSetting.skip_data_mc_ratio = False
    p.plotSetting.shift_last_bin = False
    p.plotSetting.stack_x_label_size = 0
    p.plotSetting.bin_width_label = "Event / bin"
    p.plotSetting.x_axis_title = "m_{Z2} [GeV]"
    p.plotSetting.leg_pos = [0.20,0.65,0.80,0.90]
    p.customHistDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))
    p.plotSetting.leg_name_dict = {
            "HZZd_M30": "H #rightarrow Z Z_{D} (m_{Z_{D}} = 30 GeV #varepsilon = 0.05)",
            "HZZd_M15": "H #rightarrow Z Z_{D} (m_{Z_{D}} = 15 GeV #varepsilon = 0.05)",
            "ZPlusX": "Reducible",
            "Higgs": "Higgs boson",
            }
    p.plotSetting.bkgErrFunc = lambda x,y,z: math.sqrt((0.09*y)**2+z**2)

plot_el.plotSetting.linear_max_factor = 2.5
plot_el.plotSetting.custom_latex_list = [
       BaseObject(plot_el.key,x_pos=4.,y_pos=13.,text_size=0.035,text="2e channel",),
       ]
plot_mu.plotSetting.linear_max_factor = 2.0
plot_mu.plotSetting.custom_latex_list = [
       BaseObject(plot_mu.key,x_pos=4.,y_pos=16.5,text_size=0.035,text="2#mu channel",),
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
endSequence.add(PaperPlotEndModule(endModuleOutputDir,plots,skipSF=True))
