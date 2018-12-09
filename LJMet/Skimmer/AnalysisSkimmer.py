from Core.Module import Module

class AnalysisSkimmer(Module):
	def analyze(self,event):
		#pre-selections
		if event.leptonPt_singleLepCalc[0] < 60.: return False
		if event.corr_met_singleLepCalc[0] < 50.: return False
		if event.NJets_JetSubCalc[0] < 3: return False
		if event.theJetPt_JetSubCalc_PtOrdered[0] < 200.: return False
		if event.theJetPt_JetSubCalc_PtOrdered[1] < 100.: return False
		if event.theJetPt_JetSubCalc_PtOrdered[2] < 50.: return False
		if not (event.minDR_lepJet[0] > 0.4 or event.ptRel_lepJet[0] > 40.): return False
		if not (event.DataPastTrigger[0] == 1 and event.MCPastTrigger[0] == 1): return False
		#signal region selection
		if event.theJetPt_JetSubCalc_PtOrdered[0] < 300.: return False
		if event.theJetPt_JetSubCalc_PtOrdered[1] < 150.: return False
		if event.theJetPt_JetSubCalc_PtOrdered[2] < 100.: return False
		#if event.NPuppiWtagged_0p55[0] == 0 and event.NJetsH1btagged[0] == 0 and event.NJetsH2btagged[0] == 0 and (event.NJets_JetSubCalc[0] >= 4 and event.theJetPt_JetSubCalc_PtOrdered[3] > 30.): return False
		#if event.NJetsH1btagged[0] >= 1 or event.NJetsH2btagged[0] >= 1:
		#	if event.NJetsCSV_JetSubCalc[0] == 0: return False
		if event.corr_met_singleLepCalc[0] < 75: return False
		if event.NJetsAK8_JetSubCalc[0] < 2: return False
		#if event.minMleppBjet[0] > 3: return False
		#if not ((event.isElectron[0] == 1 and event.isMuon[0] == 0) or (event.isElectron[0] == 0 and event.isMuon[0] == 1)): return False
		if not (event.isElectron[0] == 0 and event.isMuon[0] == 1): return False
		return True
