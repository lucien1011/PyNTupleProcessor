from Core.Module import Module

class DataMCWeighter(Module):
    def analyze(self,event):
        if self.dataset.isData: return True
        event.weight *= event.pileupWeight[0]
        event.weight *= event.lepIdSF[0]
        event.weight *= event.EGammaGsfSF[0]
        event.weight *= event.triggerSF[0]
        event.weight *= event.isoSF[0]
        event.weight *= event.L1NonPrefiringProb_CommonCalc[0]
        if 'WJets' in self.dataset.name: event.weight *= event.HTSF_Pol[0]
        return True
#		if "TTJets" in self.dataset.name:
#			event.weight *= event.topPtWeight13TeV[0]
#        return True
