import ROOT,os
from Core.mkdir_p import mkdir_p
from Core.BaseObject import BaseObject
from Utils.System import system

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
baseDir         = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-08-21_136p1_RunII_RatioCut0p05/"
inputPath       = baseDir+"ZPlusX/StatInput.root"
#inputNormPath   = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/2019-08-23_Run2016/ZPlusX/DataMCDistribution.root"
#inputNormPath   = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/2019-08-23_Run2017/ZPlusX/DataMCDistribution.root"
inputNormPath   = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/2019-08-23_Run2018/ZPlusX/DataMCDistribution.root"
#outputDir       = system.getPublicHtmlPath()+"/Higgs/HToZdZd/Parametrization/2019-08-21_136p1_RunII_RatioCut0p05/"
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
                        BaseObject("mZ2_mu",rebin=800,histName="comb"),
                        BaseObject("mZ2_el",rebin=800,histName="comb"),
                    ]
drawFit         = True

# _____________________________________________________________________________ ||
inputFile = ROOT.TFile(inputPath,"READ")
inputNormFile = ROOT.TFile(inputNormPath,"READ")
mkdir_p(os.path.dirname(outputDir))
if drawFit: c = ROOT.TCanvas()
outputFile = ROOT.TFile(os.path.join(outputDir,"shape.root"),"RECREATE")
for bin in binList:
    histName = bin.histName
    inputHist = inputFile.Get(histName).Clone()
    inputHistClone = inputHist.Clone()
    inputNormHist = inputNormFile.Get(bin.name)
    inputHist.Rebin(bin.rebin)
    inputHist.Fit("landau")
    func = inputHist.GetFunction("landau")
    func.SetName(bin.name+"_shape")
    outputHist = inputNormHist.Clone(bin.name+"_shapehist")
    for ibin in range(1,inputNormHist.GetNbinsX()+1):
        x_value = inputNormHist.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,func.Eval(x_value))
    outputHist.Scale(inputNormHist.Integral()/outputHist.Integral())
    outputFile.cd()
    inputHist.Write()
    outputHist.Write()
    func.Write()
    if drawFit:
        outputHist.SetStats(0)
        outputHist.Draw()
        c.SaveAs(os.path.join(outputDir,"fit_"+bin.name+".pdf"))
inputFile.Close()
inputNormFile.Close()

# _____________________________________________________________________________ ||

