from Core.Module import Module

class DataMCWeighter(Module):
	def analyze(self,event):
		event.weight *= event.pileupWeight[0]
		event.weight *= event.lepIdSF[0]
		event.weight *= event.EGammaGsfSF[0]
		if "TTJets" in self.dataset.name:
			event.weight *= event.topPtWeight13TeV[0]
		return True
