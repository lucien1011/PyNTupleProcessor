from Core.Module import Module

class ControlSkimmer(Module):
    def analyze(self,event):
        if event.NJets_JetSubCalc[0] < 4: return False
        if event.theJetPt_JetSubCalc_PtOrdered[0] < 300.: return False
        if event.theJetPt_JetSubCalc_PtOrdered[1] < 150.: return False
        if event.theJetPt_JetSubCalc_PtOrdered[2] < 100.: return False
        if event.theJetPt_JetSubCalc_PtOrdered[3] < 30.: return False
        if event.NJetsAK8_JetSubCalc[0] < 2: return False
        if event.corr_met_MultiLepCalc[0] < 75.: return False
        if any(eta > 2.4 for eta in event.theJetEta_JetSubCalc_PtOrdered): return False
        if not (event.DataPastTrigger[0] == 1 and event.MCPastTrigger[0] == 1): return False
        if not ((event.isElectron[0] == 1 and event.isMuon[0] == 0) or (event.isElectron[0] == 0 and event.isMuon[0] == 1)): return False
        if event.minDR_leadAK8otherAK8[0] < 3.: return False
        return True
