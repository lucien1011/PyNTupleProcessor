from Core.Module import Module

class CategoryProducer(Module):
	def analyze(self,event):
		self.computeCategory(event)
		#return event.category and event.categoryNumber and event.region
		return True

	def computeCategory(self,event):
		event.category = None
		event.categoryNumber = None
		event.region = None
		event.lepCategory = None
		if event.isElectron[0] == 1 and event.isMuon[0] == 0:
			event.lepCategory = "isE"
		elif event.isElectron[0] == 0 and event.isMuon[0] == 1:
			event.lepCategory = "isM"

		if event.minMleppBjet[0] > 3.:
			event.region = "isSR"
			if event.NJetsH1btagged[0] == 0 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] == 0:
				if event.NJetsCSV_JetSubCalc[0] == 0:
					event.category = "nH0_nW0_nB0"
					event.categoryNumber = 1
				elif event.NJetsCSV_JetSubCalc[0] == 1:
					event.category = "nH0_nW0_nB1"
					event.categoryNumber = 2
				elif event.NJetsCSV_JetSubCalc[0] == 2:
					event.category = "nH0_nW0_nB2"
					event.categoryNumber = 3
				else:
					event.category = "nH0_nW0_nB3p"
					event.categoryNumber = 4
			elif event.NJetsH1btagged[0] == 0 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] >= 1:
				if event.NJetsCSV_JetSubCalc[0] == 0:
					event.category = "nH0_nW1p_nB0"
					event.categoryNumber = 5
				elif event.NJetsCSV_JetSubCalc[0] == 1:
					event.category = "nH0_nW1p_nB1"
					event.categoryNumber = 6
				elif event.NJetsCSV_JetSubCalc[0] == 2:
					event.category = "nH0_nW1p_nB2"
					event.categoryNumber = 7
				else:
					event.category = "nH0_nW1p_nB3p"
					event.categoryNumber = 8
			elif event.NJetsH1btagged[0] > 0 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] >= 0 and event.NJetsCSVnotH_JetSubCalc[0] >= 1:
				event.category ="nH1b_nW0p_nB1p"
				event.categoryNumber = 9
			elif event.NJetsH2btagged[0] > 0 and event.NPuppiWtagged_0p55[0] >= 0 and event.NJetsCSVnotH_JetSubCalc[0] >= 1:
				event.category ="nH2b_nW0p_nB1p"
				event.categoryNumber = 10
		else:
			event.region = "isCR"
			if event.NJetsH1btagged[0] == 0 and event.NJetsH2btagged[0] == 0 and event.NPuppiWtagged_0p55[0] >= 0:
				if event.NJetsCSV_JetSubCalc[0] == 0:
					event.category = "nH0_nW0p_nB0"
					event.categoryNumber = 11
				elif event.NJetsCSV_JetSubCalc[0] >= 1:
					event.category = "nH0_nW0p_nB1p"
					event.categoryNumber = 12
