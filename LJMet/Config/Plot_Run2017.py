from Core.Utils.LambdaFunc import LambdaFunc
from Plotter.Plot import Plot
from Plotter.PlotSetting import PlotSetting

plots = [
		#multiplicities:
        Plot("Njets",        ["TH1D","Njets","jet multiplicity",10,0,10],	LambdaFunc('x: x.NJets_JetSubCalc[0]'),),
        Plot("AK8Njets",     ["TH1D","AK8Njets","AK8 jet multiplicity",10,0,10],	LambdaFunc('x: x.NJetsAK8_JetSubCalc[0]'),),
        Plot("Nbjets",       ["TH1D","Nbjets","b tag multiplicity",10,0,10],	LambdaFunc('x: x.NJetsCSV_JetSubCalc[0]'),),
        Plot("NbjetsWithSF", ["TH1D","NbjetsWithSF","b tag multiplicity",10,0,10],	LambdaFunc('x: x.NJetsCSVwithSF_JetSubCalc[0]'),),
        Plot("NWtag",        ["TH1D","NWtag","W tag multiplicity",10,0,10],	LambdaFunc('x: x.NJetsWtagged[0]'),), #check if it's 0p6 or something else?
        Plot("Nh1btag",      ["TH1D","Nh1btag","h1b tag multiplicity",5,0,5],	LambdaFunc('x: x.NJetsH1btagged[0]'),),
        Plot("Nh2btag",      ["TH1D","Nh2btag","h2b tag multiplicity",5,0,5],	LambdaFunc('x: x.NJetsH2btagged[0]'),),
        Plot("PV",       	 ["TH1D","PV","PV",40,0,40],	LambdaFunc('x: x.nPV_singleLepCalc[0]'),),

		#properties:
        Plot("MET",        	 ["TH1D","MET","MET",50,0.0,1500.0],	LambdaFunc('x: x.corr_met_singleLepCalc[0]'),),
		Plot("lept",      	 ["TH1D","lept","lepton p_{T}",50,0.0,1000],	LambdaFunc('x: x.leptonPt_singleLepCalc[0]'),),
        Plot("lepeta",       ["TH1D","lepeta","lepton #eta",40,-4,4],	LambdaFunc('x: x.leptonEta_singleLepCalc[0]'),),

        Plot("jetspt",       ["TH1D","jetspt","jet p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered'), isCollection=True),
        Plot("jetseta",      ["TH1D","jetseta","jet #eta",40,-4,4],	LambdaFunc('x: x.theJetEta_JetSubCalc_PtOrdered'), isCollection=True),
        Plot("jet1pt",       ["TH1D","jet1pt","j1 p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered[0]'),),
        Plot("jet2pt",       ["TH1D","jet2pt","j2 p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered[1]'),),
        Plot("jet3pt",       ["TH1D","jet3pt","j3 p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetPt_JetSubCalc_PtOrdered[2]'),),

        Plot("jetsptAK8",    ["TH1D","jetsptAK8","AK8 jet p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered'), isCollection=True),
		Plot("jetsetaAK8",   ["TH1D","jetsetaAK8","AK8 jet #eta",40,-4,4],	LambdaFunc('x: x.theJetAK8Eta_JetSubCalc_PtOrdered'), isCollection=True),
		Plot("jetsCHSPrunedMassAK8",   ["TH1D","jetsCHSPrunedMassAK8","AK8 jet pruned mass", 30, 0.,300.],	LambdaFunc('x: x.theJetAK8CHSPrunedMass_JetSubCalc_PtOrdered'), isCollection=True),
		Plot("jetsSoftDropMassAK8",   ["TH1D","jetsSoftDropMassAK8","AK8 jet soft drop mass", 30, 0.,300.],	LambdaFunc('x: x.theJetAK8SoftDrop_PtOrdered'), isCollection=True),
		Plot("jetsSoftDropCorrAK8",   ["TH1D","jetsSoftDropCorrAK8","AK8 jet soft drop corr", 30, 0.,300.],	LambdaFunc('x: x.theJetAK8SoftDropCorr_JetSubCalc_PtOrdered'), isCollection=True),
		Plot("jetsSoftDropRawAK8",   ["TH1D","jetsSoftDropRawAK8","AK8 jet soft drop corr", 30, 0.,300.],	LambdaFunc('x: x.theJetAK8SoftDropRaw_JetSubCalc_PtOrdered'), isCollection=True),
        
        #Plot("jet1ptAK8",    ["TH1D","jet1ptAK8","AK8 j1 p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered[0]'),),
        #Plot("jet2ptAK8",    ["TH1D","jet2ptAK8","AK8 j2 p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered[1]'),),
        #Plot("jet3ptAK8",    ["TH1D","jet3ptAK8","AK8 j3 p_{T}",50,0.0,1500],	LambdaFunc('x: x.theJetAK8Pt_JetSubCalc_PtOrdered[2]'),),

		#Plot("Tau21",       ["TH1D","Tau21","AK8 jet #tau_{2}/#tau_{1}",50,0,1],	LambdaFunc('x: x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered[0]/x.theJetAK8NjettinessTau1_JetSubCalc_PtOrdered[0]'),),
		#Plot("Tau32",       ["TH1D","Tau32","AK8 jet #tau_{3}/#tau_{2}",50,0,1],	LambdaFunc('x: x.theJetAK8NjettinessTau3_JetSubCalc_PtOrdered[0]/x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered[0]'),),
		Plot("Tau21",       ["TH1D","Tau21","",50,0,1],	LambdaFunc('x: [ tau2/x.theJetAK8NjettinessTau1_JetSubCalc_PtOrdered[itau] for itau,tau2 in enumerate(x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered)]'), isCollection=True, plotSetting=PlotSetting(x_axis_title="AK8 jet #tau_{2}/#tau_{1}")),
		Plot("Tau32",       ["TH1D","Tau32","",50,0,1],	LambdaFunc('x: [ tau3/x.theJetAK8NjettinessTau2_JetSubCalc_PtOrdered[itau] for itau,tau3 in enumerate(x.theJetAK8NjettinessTau3_JetSubCalc_PtOrdered)]'), isCollection=True, plotSetting=PlotSetting(x_axis_title="AK8 jet #tau_{3}/#tau_{2}")),


		#variables may use to define the signal region & control region:
        Plot("minDeltaRAK8Jet1Jet",["TH1D","minDeltaRAK8Jet1Jet","",50,0,5],	LambdaFunc('x: x.minDR_leadAK8otherAK8[0]'),plotSetting=PlotSetting(x_axis_title="min #DeltaR(AK8 j1, AK8 ji)")),
        Plot("minDeltaRlepJet",    ["TH1D","minDeltaRlepJet","",50,0,5],	LambdaFunc('x: x.minDR_lepJet[0]'),plotSetting=PlotSetting(x_axis_title="min #DeltaR(l, j)")),
        Plot("deltaRlepj1",		   ["TH1D","deltaRlepj1","",50,0,5],	LambdaFunc('x: x.deltaR_lepJets[0]'),plotSetting=PlotSetting(x_axis_title="#DeltaR(l, j1)")),
        Plot("deltaRlepj2",        ["TH1D","deltaRlepj2","",50,0,5],	LambdaFunc('x: x.deltaR_lepJets[1]'),plotSetting=PlotSetting(x_axis_title="#DeltaR(l, j2)")),
        Plot("deltaRlepj3",        ["TH1D","deltaRlepj3","",50,0,5],	LambdaFunc('x: x.deltaR_lepJets[2]'),plotSetting=PlotSetting(x_axis_title="#DeltaR(l, j3)")),
		#deltaR_lepBJets vector
		#deltaR_lepAK8s vector

		#for tt + jets CR
        Plot("minMlb",       ["TH1D","minMlb","",40,0.0,800.0],	LambdaFunc('x: x.minMleppBjet[0]'),plotSetting=PlotSetting(x_axis_title="min M(l, b)")),
		#for W + jets CR
        #Plot("minMlj",       ["TH1D","minMlj","",50,0.0,1000.0],	LambdaFunc('x: x.minMleppJet[0] if len(x.minMleppJet) == 1 else None'),plotSetting=PlotSetting(x_axis_title="min M(l, j)")),

		#variables used for fit:
        Plot("AK4HT",        ["TH1D","AK4HT","",25,500.0,3000.0],	LambdaFunc('x: x.AK4HT[0]'),plotSetting=PlotSetting(x_axis_title="AK4 H_{T}")),
        Plot("AK4ST",        ["TH1D","AK4ST","",50,0.0,5000.0],	LambdaFunc('x: x.AK4HTpMETpLepPt[0]'),plotSetting=PlotSetting(x_axis_title="AK4 S_{T}")),

		Plot("Category", ["TH1D","Category","",12,0.5,12.5],	LambdaFunc('x: x.categoryNumber if x.categoryNumber else None'), plotSetting=PlotSetting(x_axis_labels=
			[
				"0H/0W/0b",
                "0H/0W/1b",
                "0H/0W/2b",
                "0H/0W/3b",
                "0H/1W/0b",
                "0H/1W/1b",
                "0H/1W/2b",
                "0H/1W/3b",
                "1H/0W/1b",
                "2H/0W/1b",
                "0H/0W/0b",
                "0H/0W/1b",
			],
			)),
        ]
