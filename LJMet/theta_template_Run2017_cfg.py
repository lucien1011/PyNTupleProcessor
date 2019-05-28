from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from Plotter.Plotter import Plotter
from Plotter.PlotSetting import PlotSetting
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from LJMet.Weighter.XSWeighter import XSWeighter
from LJMet.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from LJMet.Weighter.DataMCWeighter import DataMCWeighter
from LJMet.Producer.CategoryProducer import CategoryProducer
from LJMet.Producer.ThetaProducer import ThetaTemplateProducer

from LJMet.Dataset.LJMet_step1_tptp2017 import *

from LJMet.Config.MergeSampleDict_StatInput import mergeSampleDict

#out_path                = "TestPlot/2018-12-04_StatInput/"
#out_path                = "TestPlot/2018-12-05_test/"
out_path                = "ThetaInput/2019-05-27_StatInput/"
lumi                    = 41.298
nCores                  = 5
outputDir               = out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples + sigSamples
justEndSequence         = False 

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

xsWeighter              = XSWeighter("XSWeighter")
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
anaSkimmer              = AnalysisSkimmer("AnalysisSkimmer")
catProducer				= CategoryProducer("CategoryProducer")
thetaProducer			= ThetaTemplateProducer("TemplateProducer")

sequence                = Sequence()
sequence.add(anaSkimmer)
sequence.add(xsWeighter)
sequence.add(dataMCWeighter)
sequence.add(catProducer)
sequence.add(thetaProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

#endSequence = EndSequence(skipHadd=False,haddDataSamples=True,skipComponentHadd=True)
endSequence = EndSequence(skipHadd=False,haddDataSamples=True,skipComponentHadd=False)
endSequence.allDataName = "DATA"
