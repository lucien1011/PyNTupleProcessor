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
        Plot("AK4HT",        ["TH1D","AK4HT","",25,500.0,3000.0],	LambdaFunc('x: x.AK4HT[0]'),),
        Plot("MET",        	 ["TH1D","MET","",50,0.0,1500.0],	LambdaFunc('x: x.corr_met_singleLepCalc[0]'),),
        Plot("AK4ST",        ["TH1D","AK4ST","",50,0.0,5000.0],	LambdaFunc('x: x.AK4HTpMETpLepPt[0]'),),
        Plot("minMlb",       ["TH1D","minMlb","",50,0.0,800.0],	LambdaFunc('x: x.minMleppBjet[0]'),),
        Plot("Njets",        ["TH1D","Njets","",10,0.0,10.0],	LambdaFunc('x: x.NJets_JetSubCalc[0]'),),
        Plot("AK8Njets",     ["TH1D","AK8Njets","",10,0.0,10.0],	LambdaFunc('x: x.NJetsAK8_JetSubCalc[0]'),),
        Plot("Nwtag",        ["TH1D","Nwtag","",10,0.0,10.0],	LambdaFunc('x: x.NJetsWtagged_0p6[0]'),),
        Plot("Nh1btag",      ["TH1D","Nh1btag","",5,0.0,5.0],	LambdaFunc('x: x.NJetsH1btagged[0]'),),
        Plot("Nh2btag",      ["TH1D","Nh2btag","",5,0.0,5.0],	LambdaFunc('x: x.NJetsH2btagged[0]'),),

        Plot("lept",      	 ["TH1D","lept","",50,0.0,1000],	LambdaFunc('x: x.leptonPt_singleLepCalc[0]'),),
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
