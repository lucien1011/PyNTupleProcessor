from Core.Module import Module

class AnalysisSkimmer(Module):
	def analyze(self,event):
		if event.leptonPt_singleLepCalc[0] < 60.: return False
		if event.corr_met_singleLepCalc[0] < 50.: return False
		if event.NJets_JetSubCalc[0] < 3: return False
		if event.theJetPt_JetSubCalc_PtOrdered[0] < 200.: return False
		if event.theJetPt_JetSubCalc_PtOrdered[1] < 100.: return False
		if event.theJetPt_JetSubCalc_PtOrdered[2] < 50.: return False
		if not (event.minDR_lepJet > 0.4 or event.ptRel_lepJet > 40): return False
		if not (event.DataPastTrigger[0] == 1 and event.MCPastTrigger[0] == 1): return False


		return True
