from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from LJMet.Weighter.XSWeighter import XSWeighter
from LJMet.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from LJMet.Weighter.DataMCWeighter import DataMCWeighter

from LJMet.Dataset.LJMet94X_1lepTT_101118newB_step1hadds_2018 import *

mergeSampleDict = {


		"DYJets":	["DY"],
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
		"TTV":		[
						'TTWl','TTZl',
					],
		"QCD":		[
						'QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
					],
		}

out_path                = "TestPlot/2018-11-19/"
lumi                    = 41.298
nCores                  = 5
outputDir               = out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples
justEndSequence         = False

plots = [
        Plot("AK4HT",        ["TH1D","AK4HT","",25,500.0,3000.0],      LambdaFunc('x: x.AK4HT[0]'),),
        ]

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
xsWeighter              = XSWeighter("XSWeighter")
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
anaSkimmer              = AnalysisSkimmer("AnalysisSkimmer")

sequence                = Sequence()
sequence.add(anaSkimmer)
sequence.add(xsWeighter)
sequence.add(dataMCWeighter)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=False,)
endModuleOutputDir = out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
