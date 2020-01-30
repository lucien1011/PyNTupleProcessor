import ROOT,os
from Core.mkdir_p import mkdir_p
from Core.BaseObject import BaseObject
from Utils.System import system

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
baseDir         = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-08-21_136p1_RunII_RatioCut0p05/"
inputPath       = baseDir+"ZPlusX/StatInput.root"
inputNormPath   = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-06_SR2D_hadd_RunII/ZPlusX/StatInput.root"
outputDir       = os.path.dirname(inputNormPath)
binList         = [
                        # Stat Input
                        #BaseObject("ElEl",rebin=100,histName="comb"),
                        #BaseObject("MuEl",rebin=100,histName="comb"),
                        #BaseObject("MuMu",rebin=100,histName="comb"),
                        #BaseObject("ElMu",rebin=100,histName="comb"),
                        #BaseObject("Mu",rebin=800,histName="comb"),
                        #BaseObject("El",rebin=800,histName="comb"),
                
                        # Plot
                        BaseObject("MuMu",rebin=800,histName="comb",normHistName="MuMu",),
                        BaseObject("ElMu",rebin=800,histName="comb",normHistName="ElMu",),
                        BaseObject("MuEl",rebin=800,histName="comb",normHistName="MuEl",),
                        BaseObject("ElEl",rebin=800,histName="comb",normHistName="ElEl",),
                    ]
drawFit         = True
fitFunc         = "landau"

# _____________________________________________________________________________ ||
inputFile = ROOT.TFile(inputPath,"READ")
inputNormFile = ROOT.TFile(inputNormPath,"READ")
mkdir_p(os.path.dirname(outputDir))
if drawFit: c = ROOT.TCanvas()
outputFile = ROOT.TFile(os.path.join(outputDir,"shape.root"),"RECREATE")
for bin in binList:
    print "Processing "+bin.name
    histName = bin.histName
    inputHist = inputFile.Get(histName).Clone()
    inputHistClone = inputHist.Clone()
    inputNormHist = inputNormFile.Get(bin.normHistName)
    inputHist.Rebin(bin.rebin)
    inputHist.Fit(fitFunc)
    func = inputHist.GetFunction(fitFunc)
    func.SetName(bin.name+"_shape")
    outputHist = inputNormHist.Clone(bin.name+"_shapehist").ProjectionX()
    for ibin in range(1,inputNormHist.GetNbinsX()+1):
        x_value = inputNormHist.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,func.Eval(x_value))
    outputHist.Scale(inputNormHist.Integral()/outputHist.Integral())
    outputFile.cd()
    outputHist.Write()
    func.Write()
    if drawFit:
        outputHist.SetStats(0)
        outputHist.Draw()
        c.SaveAs(os.path.join(outputDir,"fit_"+bin.name+".pdf"))
inputFile.Close()
inputNormFile.Close()

# _____________________________________________________________________________ ||

