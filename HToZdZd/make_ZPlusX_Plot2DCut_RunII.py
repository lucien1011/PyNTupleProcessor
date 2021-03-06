import ROOT,os
from Core.BaseObject import BaseObject
from Core.mkdir_p import mkdir_p

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
inputFitFilePath    = "/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-08-21_136p1_RunII_RatioCut0p05/ZPlusX/StatInput.root"
inputParaFilePath   = "/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/2020-02-29_RunII/ZPlusX/DataMCDistribution.root"
outputDir           = os.path.dirname(inputParaFilePath)
outputFileName      = "PlotShape.root"

binList             = [
                        BaseObject("MuMu",rebin=800,histName="comb",normHistName="mZ2_4mu",),
                        BaseObject("ElMu",rebin=800,histName="comb",normHistName="mZ2_2e2mu",),
                        BaseObject("MuEl",rebin=800,histName="comb",normHistName="mZ2_2mu2e",),
                        BaseObject("ElEl",rebin=800,histName="comb",normHistName="mZ2_4e",),
                        BaseObject("MuMu",rebin=800,histName="comb",normHistName="mZ12_4mu",),
                        BaseObject("ElMu",rebin=800,histName="comb",normHistName="mZ12_2e2mu",),
                        BaseObject("MuEl",rebin=800,histName="comb",normHistName="mZ12_2mu2e",),
                        BaseObject("ElEl",rebin=800,histName="comb",normHistName="mZ12_4e",),
                        ]
fitFuncName         = "landau"
drawFit             = False

# _____________________________________________________________________________ ||
inputFitFile = ROOT.TFile(inputFitFilePath,"READ")
inputParaFile = ROOT.TFile(inputParaFilePath,"READ")
mkdir_p(outputDir)
outputFile = ROOT.TFile(os.path.join(outputDir,outputFileName),"RECREATE")
outputFile.cd()
for b in binList:
    fitHist = inputFitFile.Get(b.histName)
    fitHist.Rebin(b.rebin)
    fitHist.Scale(1./fitHist.Integral())
    fitHist.Fit(fitFuncName)
    fitFunc = fitHist.GetFunction(fitFuncName)
    fitFunc.SetName(b.name+"_fitFunc")
    paraInputHist = inputParaFile.Get(b.normHistName)
    outputHist = paraInputHist.Clone(b.normHistName+"_shapehist")
    for ibin in range(1,outputHist.GetNbinsX()+1):
        x = outputHist.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,fitFunc.Eval(x))
    print "Scale to "+str(paraInputHist.Integral())+" from "+str(outputHist.Integral())
    if outputHist.Integral(): 
        outputHist.Scale(paraInputHist.Integral()/outputHist.Integral())
    if paraInputHist.Integral() < 0.:
        outputHist.Scale(0.)
    outputHist.Write()
    fitFunc.Write()
    if drawFit:
        c = ROOT.TCanvas()
        outputHist.SetStats(0)
        fitFunc.Draw()
        c.SaveAs(os.path.join(outputDir,"fit_"+b.name+".pdf"))
outputFile.Close()

# _____________________________________________________________________________ ||
