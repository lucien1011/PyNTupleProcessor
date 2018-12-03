from Core.Module import Module

class CategoryProducer(Module):
	def analyze(self,event):
		event.category,event.categoryNumber = self.computeCategory(event)
		if event.minMleppBjet[0] > 3.:
			event.region = "SR"
		else:
			event.region = "CR"
		return True

	def computeCategory(self,event):
		if event.NJetsH1btagged[0] == 0 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] == 0:
			if event.NJetsCSV_JetSubCalc[0] == 0:
				return "eq0H_eq0W_eq0b",1
			if event.NJetsCSV_JetSubCalc[0] == 1:
				return "eq0H_eq0W_eq1b",2
			if event.NJetsCSV_JetSubCalc[0] == 2:
				return "eq0H_eq0W_eq2b",3
			else:
				return "eq0H_eq0W_ge3b",4
		elif event.NJetsH1btagged[0] == 0 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] >= 1:
			if event.NJetsCSV_JetSubCalc[0] == 0:
				return "eq0H_ge1W_eq0b",5
			if event.NJetsCSV_JetSubCalc[0] == 1:
				return "eq0H_ge1W_eq1b",6
			if event.NJetsCSV_JetSubCalc[0] == 2:
				return "eq0H_ge1W_eq2b",7
			else:
				return "eq0H_ge1W_ge3b",8
		elif event.NJetsH1btagged[0] == 1 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] >= 0 and event.NJetsCSV_JetSubCalc[0] >= 1:
			return "eq1H_ge1W_ge1b",9
		elif event.NJetsH1btagged[0] == 2 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] >= 0 and event.NJetsCSV_JetSubCalc[0] >= 1:
			return "eq2H_ge1W_ge1b",10
		return "",-1
