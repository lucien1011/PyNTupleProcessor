import os,ROOT

class Sample(object):
	def __init__(self,**kwargs):
		self.__dict__.update(kwargs)

class TemplateWriter(object):
	def __init__(self,samples,outputPath):
		self.sampleDict = {}
		self.files = []
		self.outputFile = ROOT.TFile(outputPath,"RECREATE")

	def write(self):
		self.outputFile.cd()
		for sampleName,sample in self.sampleDict.iteritems():
			sample.nominalMuHist.Write()
			sample.nominalElHist.Write()
		self.outputFile.Write()

	def emptyHist(self,hist):
		nBins = hist.GetNbinsX()
		for ibin in range(0,nBins+2):
			hist.SetBinContent(ibin,0.)
			hist.SetBinError(ibin,0.)

	def end(self):
		for f in self.files:
			f.Close()
		self.outputFile.Close()
