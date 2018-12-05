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

from LJMet.Dataset.LJMet_step1test_yiting import *

mergeSampleDict = {


		"EWK":		[
						"DY",
						'WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',
						'TTWl','TTZl',
					],
		"WJets":	['WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',],
		"TTJets":	[
						'TTJetsHad0','TTJetsHad700','TTJetsHad1000',
						'TTJetsSemiLep0','TTJetsSemiLep700','TTJetsSemiLep1000',
						'TTJets2L2nu0','TTJets2L2nu700','TTJets2L2nu1000',
						'TTJetsPH700mtt','TTJetsPH1000mtt',
					],
		"SingleTop":	[
							'Ts','Tt','Tbt','TtW','TbtW',
						],
		"QCD":		[
						'QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
					],
		"Bkg":		[
						"DY",
						'WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',
						'TTWl','TTZl',
						'WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',
						'TTJetsHad0','TTJetsHad700','TTJetsHad1000',
						'TTJetsSemiLep0','TTJetsSemiLep700','TTJetsSemiLep1000',
						'TTJets2L2nu0','TTJets2L2nu700','TTJets2L2nu1000',
						'TTJetsPH700mtt','TTJetsPH1000mtt',
						'Ts','Tt','Tbt','TtW','TbtW',
						'QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
					],
		}

out_path                = "TestPlot/2018-12-04_StatInput/"
#out_path                = "TestPlot/2018-12-05_test/"
lumi                    = 41.298
nCores                  = 1
outputDir               = out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + dataSamples
componentList           = sigSamples
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
