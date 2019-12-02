import ROOT,os
from Core.mkdir_p import mkdir_p
from Core.BaseObject import BaseObject
from Utils.System import system

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
baseDir         = system.getStoragePath()+"/lucien/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/2019-07-29_Run2017/"
inputPath       = baseDir+"ZPlusX/DataMCDistribution.root"
outputDir       = baseDir+"ZPlusX/"
outFileName     = "shape_veto.root"
binList         = [
                        #BaseObject("mZ2_4e",rebin=5,histName="mZ2_4e"),
                        #BaseObject("mZ2_low-m4l_4e",rebin=5,histName="mZ2_low-m4l_4e"),
                        #BaseObject("mZ2_mid-m4l_4e",rebin=5,histName="mZ2_mid-m4l_4e"),
                        #BaseObject("mZ2_high-m4l_4e",rebin=5,histName="mZ2_high-m4l_4e"),
                        #BaseObject("mZ2_2mu2e",rebin=5,histName="mZ2_2mu2e"),
                        #BaseObject("mZ2_low-m4l_2mu2e",rebin=5,histName="mZ2_low-m4l_2mu2e"),
                        #BaseObject("mZ2_mid-m4l_2mu2e",rebin=5,histName="mZ2_mid-m4l_2mu2e"),
                        #BaseObject("mZ2_high-m4l_2mu2e",rebin=5,histName="mZ2_high-m4l_2mu2e"),
                        #BaseObject("mZ2_4mu",rebin=10,histName="mZ2_4mu"),
                        #BaseObject("mZ2_low-m4l_4mu",rebin=5,histName="mZ2_low-m4l_4mu"),
                        #BaseObject("mZ2_mid-m4l_4mu",rebin=5,histName="mZ2_mid-m4l_4mu"),
                        #BaseObject("mZ2_high-m4l_4mu",rebin=10,histName="mZ2_high-m4l_4mu"),
                        #BaseObject("mZ2_2e2mu",rebin=10,histName="mZ2_2e2mu"),
                        #BaseObject("mZ2_low-m4l_2e2mu",rebin=5,histName="mZ2_low-m4l_2e2mu"),
                        #BaseObject("mZ2_mid-m4l_2e2mu",rebin=5,histName="mZ2_mid-m4l_2e2mu"),
                        #BaseObject("mZ2_high-m4l_2e2mu",rebin=10,histName="mZ2_high-m4l_2e2mu"),
                        BaseObject("mZ2_4e",rebin=5,histName="mZ2_4e"),
                        BaseObject("mZ2_low-m4l_4e",rebin=5,histName="mZ2_4e"),
                        BaseObject("mZ2_mid-m4l_4e",rebin=5,histName="mZ2_4e"),
                        BaseObject("mZ2_high-m4l_4e",rebin=5,histName="mZ2_4e"),
                        BaseObject("mZ2_2mu2e",rebin=5,histName="mZ2_2mu2e"),
                        BaseObject("mZ2_low-m4l_2mu2e",rebin=5,histName="mZ2_2mu2e"),
                        BaseObject("mZ2_mid-m4l_2mu2e",rebin=5,histName="mZ2_2mu2e"),
                        BaseObject("mZ2_high-m4l_2mu2e",rebin=5,histName="mZ2_2mu2e"),
                        BaseObject("mZ2_4mu",rebin=10,histName="mZ2_4mu"),
                        BaseObject("mZ2_low-m4l_4mu",rebin=10,histName="mZ2_4mu"),
                        BaseObject("mZ2_mid-m4l_4mu",rebin=10,histName="mZ2_4mu"),
                        BaseObject("mZ2_high-m4l_4mu",rebin=10,histName="mZ2_4mu"),
                        BaseObject("mZ2_2e2mu",rebin=10,histName="mZ2_2e2mu"),
                        BaseObject("mZ2_low-m4l_2e2mu",rebin=10,histName="mZ2_2e2mu"),
                        BaseObject("mZ2_mid-m4l_2e2mu",rebin=10,histName="mZ2_2e2mu"),
                        BaseObject("mZ2_high-m4l_2e2mu",rebin=10,histName="mZ2_2e2mu"),
                    ]
drawFit         = True
rebin           = 5

# _____________________________________________________________________________ ||
inputFile = ROOT.TFile(inputPath,"READ")
mkdir_p(os.path.dirname(outputDir))
if drawFit: c = ROOT.TCanvas()
outputFile = ROOT.TFile(os.path.join(outputDir,outFileName),"RECREATE")
for bin in binList:
    histName = bin.histName
    inputHist = inputFile.Get(histName).Clone()
    inputHistClone = inputHist.Clone()
    inputNormHist = inputFile.Get(bin.name)
    inputHist.Rebin(bin.rebin)
    inputHist.Fit("landau")
    func = inputHist.GetFunction("landau")
    func.SetName(bin.name+"_shape")
    outputHist = inputNormHist.Clone(bin.name+"_shapehist")
    for ibin in range(1,inputNormHist.GetNbinsX()+1):
        x_value = inputNormHist.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,func.Eval(x_value) if x_value < 8.5 or x_value > 11. else 0.)
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

# _____________________________________________________________________________ ||

