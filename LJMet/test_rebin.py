import ROOT,os
from StatTools.HistHelper import HistHelper
from StatTools.TemplateWriter import TemplateWriter,Sample
from StatTools.Category_Run2017 import catList

class Signal(object):
    def __init__(self,name,br_BW,br_TZ,br_TH):
        self.name = name
        self.br_BW = br_BW
        self.br_TZ = br_TZ
        self.br_TH = br_TH
        self.finalStates = ['BWBW','THBW','THTH','TZBW','TZTH','TZTZ',]

    def calculate_scale(self,name):
        if 'BWBW' in name:    scale = 0.25
        if 'THBW' in name:    scale = 0.125 *2
        if 'THTH' in name:    scale = 0.0625
        if 'TZBW' in name:    scale = 0.125 *2
        if 'TZTH' in name:    scale = 0.0625 *2
        if 'TZTZ' in name:    scale = 0.0625
        return scale
# _________________________________________________________________________________________________________ ||
inputDir	= "~/nobackup/UF-PyNTupleRunner/LJMet/TestPlot/2018-12-04_StatInput/"
TFileName	= "StatInput.root"
samplesSig	= [
        #'TTM1100','TTM1200','TTM1300','TTM1400','TTM1500','TTM1600','TTM1700','TTM1800'
        #'TTM1100BWBW','TTM1100THBW','TTM1100THTH','TTM1100TZBW','TTM1100TZTH','TTM1100TZTZ',
        #'TTM1200BWBW','TTM1200THBW','TTM1200THTH','TTM1200TZBW','TTM1200TZTH','TTM1200TZTZ',
        #'TTM1300BWBW','TTM1300THBW','TTM1300THTH','TTM1300TZBW','TTM1300TZTH','TTM1300TZTZ',
        #'TTM1400BWBW','TTM1400THBW','TTM1400THTH','TTM1400TZBW','TTM1400TZTH','TTM1400TZTZ',
        #'TTM1500BWBW','TTM1500THBW','TTM1500THTH','TTM1500TZBW','TTM1500TZTH','TTM1500TZTZ',
        #'TTM1600BWBW','TTM1600THBW','TTM1600THTH','TTM1600TZBW','TTM1600TZTH','TTM1600TZTZ',
        #'TTM1700BWBW','TTM1700THBW','TTM1700THTH','TTM1700TZBW','TTM1700TZTH','TTM1700TZTZ',
        #'TTM1800BWBW','TTM1800THBW','TTM1800THTH','TTM1800TZBW','TTM1800TZTH','TTM1800TZTZ',
        #Signal("TTM1100",0.5,0.25,0.25),
        #Signal("TTM1200",0.5,0.25,0.25),
        #Signal("TTM1300",0.5,0.25,0.25),
        #Signal("TTM1400",0.5,0.25,0.25),
        #Signal("TTM1500",0.5,0.25,0.25),
        #Signal("TTM1600",0.5,0.25,0.25),
        #Signal("TTM1700",0.5,0.25,0.25),
        Signal("TTM1800",0.5,0.25,0.25),
        ]
samplesBck	= ["EWK","TTJets","SingleTop","QCD","DATA",]
statUnc		= 0.3

# _________________________________________________________________________________________________________ ||
inputFile	= ROOT.TFile(os.path.join(inputDir,"Bkg",TFileName),"READ")

helper = HistHelper()

# ____________________________________________________________________________________ ||
# Get new binning
for cat in catList:
    histName = cat.name
    if "isM" in histName: continue
    histTotEl = inputFile.Get(histName)
    histTotMu = inputFile.Get(histName.replace("isE","isM"))
    if not (histTotEl.Integral() and histTotMu.Integral()):
        cat.skip = True
        continue
    else:
        cat.skip = False
    cat.xbins = helper.make_binning_with_stat_unc([histTotEl,histTotMu],statUnc)
    cat.xbins_array = helper.convert_list_to_array(cat.xbins)

# ____________________________________________________________________________________ ||
# Make root file for each signal model with a certain branching fraction assumption
for signal in samplesSig:
    outputPath	= "templates_minMlbST_"+signal.name+"_bW"+str(signal.br_BW).replace('.','p')+"_tZ"+str(signal.br_TZ).replace('.','p')+"_tH"+str(signal.br_TH).replace('.','p')+"_41p298fb_BKGNORM_rebinned_stat0p3.root"
    outputFile	= ROOT.TFile(outputPath,"RECREATE")
    writer = TemplateWriter(samples=samplesBck,outputPath=outputPath)
    for cat in catList:
        histName = cat.name
        if "isM" in histName or cat.skip: continue
        for i,finalState in enumerate(signal.finalStates):
            sampleFile = ROOT.TFile(os.path.join(inputDir,signal.name+finalState,TFileName),"READ")
            writer.files.append(sampleFile)
            histElSig = sampleFile.Get(histName)
            histMuSig = sampleFile.Get(histName.replace("isE","isM"))
            try:
                histElSig.Scale(signal.calculate_scale(finalState))
            except AttributeError:
                histElSig = histTotEl.Clone()
                writer.emptyHist(histElSig)
            try:
                histMuSig.Scale(signal.calculate_scale(finalState))
            except AttributeError:
                histMuSig = histTotMu.Clone()
                writer.emptyHist(histMuSig)

            if not i:
                histElSigSum = histElSig
                histMuSigSum = histMuSig
            else:
                histElSigSum.Add(histElSigSum)
                histMuSigSum.Add(histMuSigSum)
        writer.sampleDict["sig"] = Sample(name="sig")
        writer.sampleDict["sig"].nominalMuHist = histMuSigSum.Rebin(len(cat.xbins)-1,"__".join([cat.name.replace("isE","isM"),writer.sampleDict["sig"].name]),cat.xbins_array)
        writer.sampleDict["sig"].nominalElHist = histElSigSum.Rebin(len(cat.xbins)-1,"__".join([cat.name,writer.sampleDict["sig"].name]),cat.xbins_array)
        for sample in samplesBck:
            writer.sampleDict[sample] = Sample(name=sample)
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
