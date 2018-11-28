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
justEndSequence         = True

plots = [
		#multiplicities:
        Plot("Njets",        ["TH1D","jet multiplicity","",10,0,10],	LambdaFunc('x: x.NJets_JetSubCalc[0]'),),
        Plot("AK8Njets",     ["TH1D","AK8 jet multiplicity","",10,0,10],	LambdaFunc('x: x.NJetsAK8_JetSubCalc[0]'),),
        Plot("Nbjets",       ["TH1D","b tag multiplicity","",10,0,10],	LambdaFunc('x: x.NJetsCSV_JetSubCalc[0]'),),
        Plot("NWtag",        ["TH1D","W tag multiplicity","",10,0,10],	LambdaFunc('x: x.NPuppiWtagged_0p55[0]'),), #check if it's 0p6 or something else?
        Plot("Nh1btag",      ["TH1D","h1b tag multiplicity","",5,0,5],	LambdaFunc('x: x.NJetsH1btagged[0]'),),
        Plot("Nh2btag",      ["TH1D","h2b tag multiplicity","",5,0,5],	LambdaFunc('x: x.NJetsH2btagged[0]'),),
        Plot("PV",       	 ["TH1D","PV","",40,0,40],	LambdaFunc('x: x.nPV_singleLepCalc[0]'),),

		#properties:
        Plot("MET",        	 ["TH1D","MET","",50,0.0,1500.0],	LambdaFunc('x: x.corr_met_singleLepCalc[0]'),),
		Plot("lept",      	 ["TH1D","lepton p_{T}","",50,0.0,1000],	LambdaFunc('x: x.leptonPt_singleLepCalc[0]'),),
        Plot("lepeta",       ["TH1D","lepton #eta","",40,-4,4],	LambdaFunc('x: x.leptonEta_singleLepCalc[0]'),),
        Plot("jetspt",       ["TH1D","jet p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered'), isCollection=True),
        Plot("jetseta",      ["TH1D","jet #eta","",40,-4,4],	LambdaFunc('x: x.theJetEta_JetSubCalc_PtOrdered'), isCollection=True),
        Plot("jetsptAK8",    ["TH1D","AK8 jet p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered'), isCollection=True),
		Plot("jetsetaAK8",   ["TH1D","AK8 jet #eta","",40,-4,4],	LambdaFunc('x: x.theJetAK8Eta_JetSubCalc_PtOrdered'), isCollection=True),
        #Plot("jet1pt",       ["TH1D","j1 p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered[0]'),),
        #Plot("jet2pt",       ["TH1D","j2 p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered[1]'),),
        #Plot("jet3pt",       ["TH1D","j3 p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered[2]'),),
        #Plot("jet1ptAK8",    ["TH1D","AK8 j1 p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered[0]'),),
        #Plot("jet2ptAK8",    ["TH1D","AK8 j2 p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered[1]'),),
        #Plot("jet3ptAK8",    ["TH1D","AK8 j3 p_{T}","",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered[2]'),),

		#Plot("Tau21",       ["TH1D","AK8 jet #tau_{2}/#tau_{1}","",50,0,1],	LambdaFunc('x: x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered[0]/x.theJetAK8NjettinessTau1_JetSubCalc_PtOrdered[0]'),),
		#Plot("Tau32",       ["TH1D","AK8 jet #tau_{3}/#tau_{2}","",50,0,1],	LambdaFunc('x: x.theJetAK8NjettinessTau3_JetSubCalc_PtOrdered[0]/x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered[0]'),),
		#Plot("Tau21",       ["TH1D","AK8 jet #tau_{2}/#tau_{1}","",50,0,1],	LambdaFunc('x: [ tau2/x.theJetAK8NjettinessTau1_JetSubCalc_PtOrdered[itau] for itau,tau2 in enumerate(x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered)]'), isCollection=True),
		#Plot("Tau32",       ["TH1D","AK8 jet #tau_{3}/#tau_{2}","",50,0,1],	LambdaFunc('x: [ tau3/x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered[itau] for itau,tau3 in enumerate(x.theJetAK8NjettinessTau3_JetSubCalc_PtOrdered)]'), isCollection=True),


		#variables may use to define the signal region & control region:
        #Plot("minDeltaRAK8Jet1Jet",["TH1D","min #DeltaR(AK8 j1, AK8 j)","",50,0,50.0],	LambdaFunc('x: x.minDR_leadAK8otherAK8[0]'),),
        #Plot("minDeltaRlepJet",    ["TH1D","min #DeltaR(l, j)","",50,0,5],	LambdaFunc('x: x.minDR_lepJet[0]'),),
        #Plot("deltaRlepj1",		   ["TH1D","#DeltaR(l, j1)","",50,0,5],	LambdaFunc('x: x.deltaR_lepJets[0]'),),
        #Plot("deltaRlepj2",        ["TH1D","#DeltaR(l, j2)","",50,0,5],	LambdaFunc('x: x.deltaR_lepJets[1]'),),
        #Plot("deltaRlepj3",        ["TH1D","#DeltaR(l, j3)","",50,0,5],	LambdaFunc('x: x.deltaR_lepJets[2]'),),
		#deltaR_lepBJets vector
		#deltaR_lepAK8s vector

		#for tt + jets CR
        #Plot("minMlb",       ["TH1D","min M(l, b)","",50,0.0,1000.0],	LambdaFunc('x: x.minMleppBjet[0]'),),
		#for W + jets CR
        #Plot("minMlj",       ["TH1D","min M(l, j)","",50,0.0,1000.0],	LambdaFunc('x: x.minMleppJet[0]'),),

		#variables used for fit:
        #Plot("AK4HT",        ["TH1D","AK4 H_{T}","",25,500.0,3000.0],	LambdaFunc('x: x.AK4HT[0]'),),
        #Plot("AK4ST",        ["TH1D","AK4 S_{T}","",50,0.0,5000.0],	LambdaFunc('x: x.AK4HTpMETpLepPt[0]'),),
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
