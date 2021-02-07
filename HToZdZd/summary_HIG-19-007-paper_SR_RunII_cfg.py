from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from HToZdZd.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from HToZdZd.EndModule.PaperPlotEndModule import PaperPlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict_RunII import *
from HToZdZd.Config.AnalysisNotePlot import sel_4e_str,sel_4mu_str,sel_2mu2e_str,sel_2e2mu_str
from HToZdZd.Config.CMS_lumi import CMS_lumi

import ROOT,os,copy

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-19_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-03-19_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/"
out_path                = "DarkPhotonSR/DataMCDistributions/2021-01-29_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/"
#end_out_path            = "DarkPhotonSR/DataMCDistributions/2020-06-04_RunII/"
end_out_path            = "DarkPhotonSR/DataMCDistributions/2021-01-29_RunII/"
nCores                  = 3
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples + sigSamples + rareBkgSamples
justEndSequence         = False
mZ12PlotRange           = [14,4.,60.]

plot_4e = Plot("mZ12_4e",["TH1D","mZ12_4e","",]+mZ12PlotRange,LambdaFunc('x: (x.massZ1[0]+x.massZ2[0])/2.'),selFunc=LambdaFunc('x: '+sel_4e_str))
plot_4mu = Plot("mZ12_4mu",["TH1D","mZ12_4mu","",]+mZ12PlotRange,LambdaFunc('x: (x.massZ1[0]+x.massZ2[0])/2.'),selFunc=LambdaFunc('x: '+sel_4mu_str))
plot_2e2mu = Plot("mZ12_2e2mu",["TH1D","mZ12_2e2mu","",]+mZ12PlotRange,LambdaFunc('x: (x.massZ1[0]+x.massZ2[0])/2.'),selFunc=LambdaFunc('x: '+sel_2mu2e_str+" or "+sel_2e2mu_str))
plots = [plot_4e,plot_4mu,plot_2e2mu,]

#inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape.root"),"READ")
inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","PlotShape.root"),"READ")
for p in plots:
    p.plotSetting.cms_lumi = CMS_lumi
    p.plotSetting.tdr_style = True
    p.plotSetting.divideByBinWidth = False
    p.plotSetting.linear_max_factor = 4.
    p.plotSetting.x_axis_title = "(m_{Z1}+m_{Z2})/2 [GeV]"
    p.plotSetting.skip_data_mc_ratio = True
    p.plotSetting.shift_last_bin = False
    p.plotSetting.skip_leg_err = True
    p.plotSetting.leg_pos = [0.20,0.60,0.89,0.90]
    p.plotSetting.leg_text_size = 0.025
    p.plotSetting.linear_max_factor = 4.0
    p.plotSetting.leg_name_dict = {
            "HToZdZd_M30": "H #rightarrow Z_{D} Z_{D} (m_{Z_{D}} = 30 GeV #kappa = 2 #times 10^{-4})",
            "HToZdZd_M5": "H #rightarrow Z_{D} Z_{D} (m_{Z_{D}} = 5 GeV #kappa = 2 #times 10^{-4})",
            "HToZdZd_M50": "H #rightarrow Z_{D} Z_{D} (m_{Z_{D}} = 50 GeV #kappa = 2 #times 10^{-4})",
            "ZPlusX": "Reducible",
            "ttZ": "t#bar{t}Z",
            "Higgs": "Higgs boson",
            }
    if p.plotSetting.divideByBinWidth: p.plotSetting.bin_width_label = "Bin Width"
    if p.key in [
            "mZ12_4mu","mZ12_4e","mZ12_2e2mu","mZ12_2mu2e",
            ]:
        p.customHistDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))
    p.plotSetting.bkgErrFunc = lambda x,y,z: 0.09*y
plot_4e.plotSetting.custom_latex_list = [
       BaseObject(plot_4e.key,x_pos=10.,y_pos=3.0,text_size=0.035,text="4e channel",),
       ]
plot_4mu.plotSetting.custom_latex_list = [
       BaseObject(plot_4mu.key,x_pos=10.,y_pos=6.0,text_size=0.035,text="4#mu channel",),
       ]
plot_2e2mu.plotSetting.custom_latex_list = [
       BaseObject(plot_2e2mu.key,x_pos=10.,y_pos=4.0,text_size=0.035,text="2e2#mu channel",),
       ]


for sigName in mergeSigSampleDict:
    for p in plots:
        p.plotSetting.line_style_dict[sigName] = 1
        p.plotSetting.line_width_dict[sigName] = 3

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=True)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+end_out_path
endSequence.add(PaperPlotEndModule(endModuleOutputDir,plots,skipSF=True,))
