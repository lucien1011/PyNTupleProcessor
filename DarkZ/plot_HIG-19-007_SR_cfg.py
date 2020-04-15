from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import *
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer
#from DarkZ.Config.PlotDefinition import *
from DarkZ.Config.AnalysisNotePlot import *
#from DarkZ.Config.AnalysisNotePlot_MassWindowBinning import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from DarkZ.Config.MergeSampleDict_RunII import mergeSampleDict,mergeSigSampleDict

import os,ROOT

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-18_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-19_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-27_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-27_RunII_HZZ/"
out_path                = "DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/"
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples + sigSamples
eventSelection          = LambdaFunc("x: x.mass4l[0] > 118 and x.mass4l[0] < 130")
justEndSequence         = False
mZ2PlotRange_el         = [36,0.,36.]
mZ2PlotRange_mu         = [72,0.,36.]

plots = [
        Plot("mZ2_el",["TH1D","mZ2_el","",]+mZ2PlotRange_el, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4e_str+" or "+sel_2mu2e_str)),
        Plot("mZ2_mu",["TH1D","mZ2_mu","",]+mZ2PlotRange_mu, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4mu_str+" or "+sel_2e2mu_str)),
        ]

for sample in ["HZZd_M"+str(m) for m in [5,20,30]]:
    if sample not in mergeSampleDict:
        mergeSampleDict[sample] = []
    mergeSampleDict[sample].append(sample+"_Run2016")
    mergeSampleDict[sample].append(sample+"_Run2017")
    mergeSampleDict[sample].append(sample+"_Run2018")

for sig in sigSamples:
    for p in plots:
        p.plotSetting.line_style_dict[sig.name] = 10
        p.plotSetting.line_width_dict[sig.name] = 4
        p.plotSetting.line_color_dict[sig.name] = ROOT.kRed

for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
variableProducer        = VariableProducer("VariableProducer")

sequence                = darkphoton_signal_sequence
sequence.add(variableProducer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
