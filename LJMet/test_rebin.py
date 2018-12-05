import ROOT,os
from StatTools.HistHelper import HistHelper
from StatTools.TemplateWriter import TemplateWriter,Sample
from StatTools.Category_Run2017 import catList

# _________________________________________________________________________________________________________ ||
inputDir	= "~/nobackup/UF-PyNTupleRunner/LJMet/TestPlot/2018-12-04_StatInput/"
TFileName	= "StatInput.root"
samples		= ["EWK","TTJets","SingleTop","QCD","DATA","TTM1200BWBW",]
statUnc		= 0.3
outputPath	= "test.root"

# _________________________________________________________________________________________________________ ||
inputFile	= ROOT.TFile(os.path.join(inputDir,"Bkg",TFileName),"READ")
outputFile	= ROOT.TFile(outputPath,"RECREATE")

helper = HistHelper()
writer = TemplateWriter(samples=samples,outputPath=outputPath)

for cat in catList:
	histName = cat.name
	if "isM" in histName: continue
	histTotEl = inputFile.Get(histName)
	histTotMu = inputFile.Get(histName.replace("isE","isM"))
	if not (histTotEl.Integral() and histTotMu.Integral()): continue
	cat.xbins = helper.make_binning_with_stat_unc([histTotEl,histTotMu],statUnc)
	cat.xbins_array = helper.convert_list_to_array(cat.xbins)
	for sample in samples:
		writer.sampleDict[sample] = Sample(name=sample if "TTM" not in sample else "sig")
		sampleFile = ROOT.TFile(os.path.join(inputDir,sample,TFileName),"READ")
		writer.files.append(sampleFile)
		histEl = sampleFile.Get(histName)
		histMu = sampleFile.Get(histName.replace("isE","isM"))
		try:
			writer.sampleDict[sample].nominalMuHist = histMu.Rebin(len(cat.xbins)-1,"__".join([cat.name.replace("isE","isM"),writer.sampleDict[sample].name]),cat.xbins_array)
		except AttributeError:
			writer.sampleDict[sample].nominalMuHist = histTotMu.Rebin(len(cat.xbins)-1,"__".join([cat.name.replace("isE","isM"),writer.sampleDict[sample].name]),cat.xbins_array)
			writer.emptyHist(writer.sampleDict[sample].nominalMuHist)
		try:
			writer.sampleDict[sample].nominalElHist = histEl.Rebin(len(cat.xbins)-1,"__".join([cat.name,writer.sampleDict[sample].name]),cat.xbins_array)
		except AttributeError:
			writer.sampleDict[sample].nominalElHist = histTotEl.Rebin(len(cat.xbins)-1,"__".join([cat.name,writer.sampleDict[sample].name]),cat.xbins_array)
			writer.emptyHist(writer.sampleDict[sample].nominalElHist)
	writer.write()
writer.end()
