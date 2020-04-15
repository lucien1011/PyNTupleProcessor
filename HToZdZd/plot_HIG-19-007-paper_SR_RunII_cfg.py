from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZdZd.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict_RunII import *
from HToZdZd.Config.AnalysisNotePlot import sel_4e_str,sel_4mu_str,sel_2mu2e_str,sel_2e2mu_str

import os,ROOT

#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-18_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-19_RunII/"
out_path                = "DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/"
User                    = os.environ['USER']
nCores                  = 5
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples + sigSamples + rareBkgSamples
justEndSequence         = True
skipHadd                = False  
mZ12PlotRange           = [14,4.,60.]
var_mZ12_str            = 'x: (x.massZ1[0]+x.massZ2[0])/2.'
var_mZ1_str             = 'x.massZ1[0]'
var_mZ2_str             = 'x.massZ2[0]'

plots = [ 
        Plot("mZ12_4e",["TH1D","mZ12_4e","",]+mZ12PlotRange,LambdaFunc(var_mZ12_str),selFunc=LambdaFunc('x: '+sel_4e_str)), 
        Plot("mZ12_4mu",["TH1D","mZ12_4mu","",]+mZ12PlotRange,LambdaFunc(var_mZ12_str),selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mZ12_2e2mu",["TH1D","mZ12_2e2mu","",]+mZ12PlotRange,LambdaFunc(var_mZ12_str),selFunc=LambdaFunc('x: '+sel_2mu2e_str+" or "+sel_2e2mu_str)),
        Plot("mZ1mZ2_4e",["TH2D","mZ1mZ2_4e","",]+mZ12PlotRange+mZ12PlotRange, LambdaFunc('x: ['+var_mZ1_str+','+var_mZ2_str+']'), selFunc=LambdaFunc('x: '+sel_4e_str),dim=2),
        Plot("mZ1mZ2_4mu",["TH2D","mZ1mZ2_4mu","",]+mZ12PlotRange+mZ12PlotRange, LambdaFunc('x: ['+var_mZ1_str+','+var_mZ2_str+']'), selFunc=LambdaFunc('x: '+sel_4mu_str),dim=2),
        Plot("mZ1mZ2_2e2mu",["TH2D","mZ1mZ2_2e2mu","",]+mZ12PlotRange+mZ12PlotRange, LambdaFunc('x: ['+var_mZ1_str+','+var_mZ2_str+']'), selFunc=LambdaFunc('x: '+sel_2mu2e_str+" or "+sel_2e2mu_str),dim=2),
        ]

for sig in sigSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_width_dict[sig.name] = 4

for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

for p in plots:
    if p.dim == 2: 
        p.plotSetting.leg_pos = [0.39,0.70,0.59,0.92]
        p.plotSetting.x_axis_title = "m_{Z1} [GeV]"
        p.plotSetting.y_axis_title = "m_{Z2} [GeV]"
        p.plotSetting.minimum = 0.
        p.plotSetting.marker_size = 0.7
        p.plotSetting.marker_style_dict = {
                "Higgs": 21,
                "qqZZ": 22,
                "ZZ": 22,
                "ggZZ": 23,
                "Data": 34,
                }
        p.plotSetting.marker_color_dict = {
                "qqZZ": ROOT.kOrange,
                "ZZ": ROOT.kOrange,
                "ggZZ": ROOT.kGreen,
                "Data": ROOT.kBlack
                }
        p.plotSetting.marker_size_dict = {
                "ggZZ": 0.4,
                "Data": 1.0,
                }
        p.plotSetting.draw_option = "colz"
        p.selectedSamples = ["Higgs","ZZ","Data",]
        #p.plotSetting.cms_lumi = True
        #p.plotSetting.tdr_style = True
        #p.plotSetting.SetNColumns = 4
    else:
        p.plotSetting.divideByBinWidth = True

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_unblind_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=False,haddDataSamples=True,)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
