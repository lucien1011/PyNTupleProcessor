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

from DarkZ.Config.MergeSampleDict_RunII import mergeSampleDict

import ROOT,os,copy

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/ShapeTemplate/2019-07-29_RunII/"
#end_out_path            = "DarkPhotonSR/ShapeTemplate/2019-07-29_RunII/"
#out_path                = "DarkPhotonSR/ShapeTemplate/2019-09-05_RunII/"
#end_out_path            = "DarkPhotonSR/ShapeTemplate/2019-09-05_RunII/"
out_path                = "DarkPhotonSR/ShapeTemplate/2019-11-21_RunII/"
#end_out_path            = "DarkPhotonSR/ShapeTemplate/2019-11-21_RunII/"
end_out_path            = "DarkPhotonSR/ShapeTemplate/2020-02-28_RunII/"
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
includeSignalSample     = False
componentList           = bkgSamples + dataSamples 
if includeSignalSample: componentList += sigSamples 

plots = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

for p in plots:
    p.plotSetting.tdr_style = True
    p.plotSetting.divideByBinWidth = True
    p.plotSetting.cms_lumi = True
    p.plotSetting.bin_width_label = "Event / bin"
    if p.key.startswith("mZ1"): p.plotSetting.x_axis_title = "m_{Z1} [GeV]"
    if p.key.startswith("mZ2"): p.plotSetting.x_axis_title = "m_{Z2} [GeV]"
    if p.key.startswith("m4l"): p.plotSetting.x_axis_title = "m_{4\ell} [GeV]"
    if p.key == "mZ2_mid-m4l_4mu": p.plotSetting.ratio_range = [0.,6.]

sigSamples = []
mergeSigSampleDict = {}
if includeSignalSample:
    for sample in sample2016.sigSamples:
        if "M15" not in sample.name and "M30" not in sample.name: continue
        for p in plots:
            p.plotSetting.line_style_dict[sample.name] = 10
            p.plotSetting.line_width_dict[sample.name] = 4
            p.plotSetting.line_color_dict[sample.name] = ROOT.kRed
        sample2016 = copy.deepcopy(sample)
        sample2017 = copy.deepcopy(sample)
        sample2018 = copy.deepcopy(sample)
        mergeSigSampleDict[sample.name] = []
        sample2016.name += "_Run2016"
        mergeSigSampleDict[sample.name].append(sample2016.name)
        sigSamples.append(sample2016)
        sample2017.name += "_Run2017"
        mergeSigSampleDict[sample.name].append(sample2017.name)
        sigSamples.append(sample2017)
        sample2018.name += "_Run2018"
        mergeSigSampleDict[sample.name].append(sample2018.name)
        sigSamples.append(sample2018)
    componentList += sigSamples

    for sample in sample_ppZZd.ppZZdSamples:
        if "M15" not in sample.name and "M30" not in sample.name: continue
        for p in plots:
            p.plotSetting.line_style_dict[sample.name] = 9
            p.plotSetting.line_width_dict[sample.name] = 4
            p.plotSetting.line_color_dict[sample.name] = ROOT.kOrange
        sample2016 = copy.deepcopy(sample)
        sample2017 = copy.deepcopy(sample)
        sample2018 = copy.deepcopy(sample)
        mergeSigSampleDict[sample.name] = []
        sample2016.name += "_Run2016"
        mergeSigSampleDict[sample.name].append(sample2016.name)
        sigSamples.append(sample2016)
        sample2017.name += "_Run2017"
        mergeSigSampleDict[sample.name].append(sample2017.name)
        sigSamples.append(sample2017)
        sample2018.name += "_Run2018"
        mergeSigSampleDict[sample.name].append(sample2018.name)
        sigSamples.append(sample2018)
    componentList += sigSamples


#inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape.root"),"READ")
inputShapeFile = ROOT.TFile(os.path.join(outputDir,"ZPlusX","shape_veto.root"),"READ")
for p in plots:
    #p.plotSetting.divideByBinWidth = False
    #if p.plotSetting.divideByBinWidth: p.plotSetting.bin_width_label = "Bin Width"
    #p.plotSetting.bin_width_label = "Bin Width"
    if "mZ2" in p.key:
        p.customHistDict["ZPlusX"] = BaseObject(p.key,hist=copy.deepcopy(inputShapeFile.Get(p.key+"_shapehist")))

for sig in ppZZdSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 9
        p.plotSetting.line_width_dict[sig.name] = 4
        p.plotSetting.line_color_dict[sig.name] = ROOT.kOrange

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(
        skipHadd=True,
        skipComponentHadd=True,
        )
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+end_out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))
