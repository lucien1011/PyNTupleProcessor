from Core.Module import Module

class ThetaTemplateProducer(Module):
	def __init__(self,name,varName="minMlbST",lumiStr="41fb"):
		super(ThetaTemplateProducer,self).__init__(name)
		self.varName = varName
		self.lumiStr = lumiStr

	def analyze(self,event):
		if not event.category: return True
		if not event.region: return True
		if not event.lepCategory: return True
		catStr = "_".join(
				[
					self.varName,
					self.lumiStr,
					event.lepCategory,
					event.category,
					event.region,
				]
				)
		if "nH0" in catStr:
			value = event.minMleppBjet[0]
			xbin = 1000.
		else:
			value = event.AK4HTpMETpLepPt[0]
			xbin = 5000.

		if catStr not in self.writer.objs:
			self.writer.book(
					catStr,
					"TH1D",
					catStr,
					"",
					101,
					0.,
					xbin,
					)
			self.writer.objs[catStr].Sumw2()
		self.writer.objs[catStr].Fill(value,event.weight)

		return True
