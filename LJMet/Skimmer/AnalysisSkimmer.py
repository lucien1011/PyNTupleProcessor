from Core.Module import Module

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
		#pre-selections
        if event.leptonPt_singleLepCalc[0] < 60.: return False
        if event.corr_met_singleLepCalc[0] < 75.: return False
        if event.NJets_JetSubCalc[0] < 3: return False
        if event.theJetPt_JetSubCalc_PtOrdered[0] < 300.: return False
        if event.theJetPt_JetSubCalc_PtOrdered[1] < 150.: return False
        if event.theJetPt_JetSubCalc_PtOrdered[2] < 100.: return False
        if event.NJetsAK8_JetSubCalc[0] < 2: return False
        if event.theJetAK8Pt_JetSubCalc_PtOrdered[0] < 200.: return False
        if event.theJetAK8Pt_JetSubCalc_PtOrdered[1] < 200.: return False
        if any(eta > 2.4 for eta in event.theJetEta_JetSubCalc_PtOrdered): return False
        if not (event.DataPastTrigger[0] == 1 and event.MCPastTrigger[0] == 1): return False
        if not ((event.isElectron[0] == 1 and event.isMuon[0] == 0) or (event.isElectron[0] == 0 and event.isMuon[0] == 1)): return False
        if self.cutflow == "SR":
            if not (event.minDR_leadAK8otherAK8[0] < 3. and event.minDR_leadAK8otherAK8[0] > 0.8): return False
        elif self.cutflow == "CR":
            if event.minDR_leadAK8otherAK8[0] < 3.: return False
        elif self.cutflow == "Preselection":
            pass
        return True
