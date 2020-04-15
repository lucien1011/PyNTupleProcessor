import ROOT,os
from Core.BaseObject import BaseObject
from Core.mkdir_p import mkdir_p

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
inputFitFilePath    = "/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-08-21_136p1_RunII_RatioCut0p05/ZPlusX/StatInput.root"
inputParaFilePath   = "/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2020-02-29_SR2D_Run2017/ZPlusX/StatInput.root"
#outputDir           = "/home/lucien/public_html/Higgs/HToZdZd/Parametrization/2020-02-29_SR2D_Run2017/"
outputDir           = os.path.dirname(inputParaFilePath)
outputFileName      = "ParaShape.root"

binList             = [
                        BaseObject("MuMu",rebin=800,histName="comb",normHistName="MuMu",),
                        BaseObject("ElMu",rebin=800,histName="comb",normHistName="ElMu",),
                        BaseObject("MuEl",rebin=800,histName="comb",normHistName="MuEl",),
                        BaseObject("ElEl",rebin=800,histName="comb",normHistName="ElEl",),
                        ]
fitFuncName         = "landau"
drawFit             = True

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
    paraInputHist = inputParaFile.Get(b.name)
    outputHist = paraInputHist.Clone(b.name+"_shape")
    normHist = paraInputHist.Clone(b.name+"_norm")
    for ibin in range(1,outputHist.GetNbinsX()+1):
        x = outputHist.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,fitFunc.Eval(x))
    print "Scale to "+str(paraInputHist.Integral())+" from "+str(outputHist.Integral())
    if outputHist.Integral(): 
        outputHist.Scale(paraInputHist.Integral()/outputHist.Integral())
    outputHist.Write()
    fitFunc.Write()
    normHist.Write()
    if drawFit:
        c = ROOT.TCanvas()
        outputHist.SetStats(0)
        fitFunc.Draw()
        c.SaveAs(os.path.join(outputDir,"fit_"+b.name+".pdf"))
outputFile.Close()

# _____________________________________________________________________________ ||
