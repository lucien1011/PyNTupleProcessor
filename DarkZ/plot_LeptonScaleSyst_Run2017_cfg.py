import ROOT,os
from Core.BaseObject import BaseObject
from Core.mkdir_p import mkdir_p

# ________________________________________________________________________________________ ||
ROOT.gROOT.SetBatch(ROOT.kTRUE)

# ________________________________________________________________________________________ ||
inputDir        = "/raid/raid7//lucien/Higgs/DarkZ/LeptonScale/2019-11-20_Run2017/"
bkgSamples      = [
                    "Higgs",
                    "qqZZ",
                    "ggZZ",
                    ]
plots           = [
                    BaseObject(
                        lepCat+"_Higgs"+m4l+"_LepScaleUp",
                        varHistName = lepCat+"_Higgs"+m4l+"_LepScale-Up",
                        nomHistName = lepCat+"_Higgs"+m4l+"",
                        rebin = 5000,
                        samples = bkgSamples,
                        fileName = "StatInput.root",
                        ) for lepCat in ["MuMu","ElMu","ElEl","MuEl",] for m4l in ["SR","HighSB","LowSB",]
                    ] + [        
                    BaseObject(
                        lepCat+"_Higgs"+m4l+"_LepResUp",
                        varHistName = lepCat+"_Higgs"+m4l+"_LepRes-Up",
                        nomHistName = lepCat+"_Higgs"+m4l+"_LepScale-Up",
                        rebin = 5000,
                        samples = bkgSamples,
                        fileName = "StatInput.root",
                        ) for lepCat in ["MuMu","ElMu","ElEl","MuEl",] for m4l in ["SR","HighSB","LowSB",]
                    ]
outputDir       = "/home/lucien/public_html/Higgs/DarkZ/LeptonScaleRes/2019-11-20_Run2017/"

# ________________________________________________________________________________________ ||
mkdir_p(outputDir)
for p in plots:
    p.fileDict = {}
    p.varHistDict = {}
    p.nomHistDict = {}
    for i,sample in enumerate(p.samples):
        p.fileDict[sample] = ROOT.TFile(os.path.join(inputDir,sample,p.fileName),"READ")
        p.varHistDict[sample] = p.fileDict[sample].Get(p.varHistName)
        p.nomHistDict[sample] = p.fileDict[sample].Get(p.nomHistName)
        if not i: 
            p.varHist = p.varHistDict[sample].Clone(p.name)
            p.nomHist = p.nomHistDict[sample].Clone()
        else:
            p.varHist.Add(p.varHistDict[sample])
            p.nomHist.Add(p.nomHistDict[sample])
    p.varHist.Rebin(p.rebin)
    p.nomHist.Rebin(p.rebin)
    p.varHist.Divide(p.nomHist)
    systs = [abs(p.varHist.GetBinContent(ibin)-1.) for ibin in range(1,p.varHist.GetNbinsX()+1) if p.varHist.GetBinContent(ibin) and p.varHist.GetBinError(ibin)/p.varHist.GetBinContent(ibin) < 0.5]
    print p.name+": %4.4f %4.4f"%(min(systs),max(systs))
    c = ROOT.TCanvas()
    p.varHist.SetStats(0)
    p.varHist.Draw()
    c.SaveAs(os.path.join(outputDir,p.name+".pdf"))
    for sample in p.samples:
        p.fileDict[sample].Close()

