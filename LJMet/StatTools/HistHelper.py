import os,ROOT,math,array

class HistHelper(object):
	def make_binning_with_stat_unc(self,inHists,statUnc):
		if len(inHists) == 0: raise RuntimeError
		nBins = inHists[0].GetNbinsX()
		binContentDict = {}
		binErrorDict = {}
		for iHist,inHist in enumerate(inHists):
			binContentDict[iHist] = 0.
			binErrorDict[iHist] = 0.

		xbins = []
		for iBin in range(1,nBins+1):
			for iHist,inHist in enumerate(inHists):
				binContentDict[iHist] += inHist.GetBinContent(nBins+1-iBin)
				binErrorDict[iHist] += inHist.GetBinError(nBins+1-iBin)**2
			if all([ binContent > 0. and math.sqrt(binErrorDict[iHist])/binContent <= statUnc for iHist,binContent in binContentDict.iteritems() ]):
				for iHist,inHist in enumerate(inHists):
					binContentDict[iHist] = 0.
					binErrorDict[iHist] = 0.
				xbins.append(inHists[0].GetXaxis().GetBinLowEdge(nBins+1-iBin))
		if xbins[-1] != 0: xbins.append(0.)
		return xbins[::-1]

	def convert_list_to_array(self,list):
		return array.array('d',list)

