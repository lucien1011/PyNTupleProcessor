import ROOT,os
from Core.BaseObject import BaseObject
from Core.mkdir_p import mkdir_p
from Utils.System import system

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
User                = "lucien"
inputFitFilePath    = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/ZPlusX/DataMCDistribution.root"
inputParaFilePath   = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/DarkPhotonSR/DataMCDistributions/2020-04-06_RunII/ZPlusX/DataMCDistribution.root"
outputDir           = os.path.dirname(inputParaFilePath)
outputFileName      = "PlotShape.root"

binList             = [
                        BaseObject("Mu",rebin=1,histName="mZ2_mu",normHistName="mZ2_mu",),
                        BaseObject("El",rebin=1,histName="mZ2_el",normHistName="mZ2_el",),
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
        x_up = outputHist.GetXaxis().GetBinUpEdge(ibin)
        x_low = outputHist.GetXaxis().GetBinLowEdge(ibin)
        outputHist.SetBinContent(ibin,fitFunc.Eval(x) if x_up < 8.5 or x_low > 11. else 0.)
        #outputHist.SetBinContent(ibin,fitFunc.Eval(x))
        outputHist.SetBinError(ibin,0.)
    outputHist.SetBinContent(outputHist.GetNbinsX()+1,0.)
    outputHist.SetBinError(outputHist.GetNbinsX()+1,0.)
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
