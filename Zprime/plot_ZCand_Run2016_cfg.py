from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2016.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2016.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 
from Zprime.Producer.ZCandProducer import ZCandProducer
from Zprime.Config.ZCandPlotDefinition import plots,sampleColorDict

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict import mergeSampleDict

import copy

User                    = os.environ['USER']
#out_path                = "SR/DataMCDistributions/2019-06-03_Run2017/"
out_path                = "ZCand_Plot/DataMCDistributions/2020-04-15_Run2017/"
lumi                    = 35.9
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
justEndSequence         = False

componentList =  []
for m,cmp in sigSampleDict.iteritems():
    if m not in [5,10,20,30,40,50,60]: continue
    cmp.isZp = True
    cmp.name = cmp.name+"_Zp"
    for p in plots:
        p.plotSetting.normalize = True
        p.plotSetting.linear_max_factor = 1.5
        p.plotSetting.line_style_dict[cmp.name] = 1
        p.plotSetting.line_color_dict[cmp.name] = sampleColorDict[m]
    cmp_nonZp = copy.deepcopy(cmp)
    cmp_nonZp.isZp = False
    cmp_nonZp.name = cmp.name+"_nonZp"
    for p in plots: 
        p.plotSetting.line_style_dict[cmp_nonZp.name] = 2
        p.plotSetting.line_color_dict[cmp_nonZp.name] = sampleColorDict[m]
    componentList.append(cmp)  
    componentList.append(cmp_nonZp)
for cmp in bkgSamples:
    cmp.isZp = False
    componentList.append(cmp)  

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
zcandProducer           = ZCandProducer("ZCandProducer")

sequence                = signal_sequence
sequence.add(zcandProducer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/Zprime/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
