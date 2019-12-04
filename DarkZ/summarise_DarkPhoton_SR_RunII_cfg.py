from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system
from Core.BaseObject import BaseObject
from Core.mkdir_p import mkdir_p

from DarkZ.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import *
#from DarkZ.Config.PlotDefinition import *
#from DarkZ.Config.AnalysisNotePlot import *
from DarkZ.Config.AnalysisNotePlot_MassWindowBinning import *

from Plotter.PlotEndModule import PlotEndModule

from DarkZ.Config.MergeSampleDict_RunII import mergeSampleDict

import os,ROOT,shutil

User                    = os.environ['USER']
baseDir                 = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/"
outputBaseDir           = "2019-11-21_RunII/"
outputDir               = os.path.join(baseDir,outputBaseDir)
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples
plots = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

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

for s in sample2016.bkgSamples: s.input = BaseObject("2016",inputDir=os.path.join(baseDir,"2019-11-21_Run2016/"),postfix="_Run2016",)
for s in sample2017.bkgSamples: s.input = BaseObject("2017",inputDir=os.path.join(baseDir,"2019-11-21_Run2017/"),postfix="_Run2017",)
for s in sample2018.bkgSamples: s.input = BaseObject("2018",inputDir=os.path.join(baseDir,"2019-11-21_Run2018/"),postfix="_Run2018",)
for s in sample2016.dataSamples: s.input = BaseObject("2016",inputDir=os.path.join(baseDir,"2019-11-21_Run2016/"),postfix="",)
for s in sample2017.dataSamples: s.input = BaseObject("2017",inputDir=os.path.join(baseDir,"2019-11-21_Run2017/"),postfix="",)
for s in sample2018.dataSamples: s.input = BaseObject("2018",inputDir=os.path.join(baseDir,"2019-11-21_Run2018/"),postfix="",)
for cmp in componentList:
    targetDir = os.path.join(outputDir,cmp.name)
    sourceDir = os.path.join(cmp.input.inputDir,cmp.name.replace(cmp.input.postfix,""))
    shutil.copytree(sourceDir,targetDir)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/"+outputBaseDir
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
