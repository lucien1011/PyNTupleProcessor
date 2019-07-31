from Core.Module import Module

class PreselectionSkimmer(Module):
    def analyze(self,event):
		#pre-selections
        if event.leptonPt_MultiLepCalc[0] < 60.: return False
        if event.NJets_JetSubCalc[0] < 3: return False
        if event.theJetPt_JetSubCalc_PtOrdered[0] < 200.: return False
        if event.theJetPt_JetSubCalc_PtOrdered[1] < 100.: return False
        if event.theJetPt_JetSubCalc_PtOrdered[2] < 50.: return False
        if event.AK4HT[0] < 400.: return False
        if event.corr_met_MultiLepCalc[0] < 60.: return False
        if any(eta > 2.4 for eta in event.theJetEta_JetSubCalc_PtOrdered): return False
        if not (event.DataPastTrigger[0] == 1 and event.MCPastTrigger[0] == 1): return False
        if not ((event.isElectron[0] == 1 and event.isMuon[0] == 0) or (event.isElectron[0] == 0 and event.isMuon[0] == 1)): return False
        return True
