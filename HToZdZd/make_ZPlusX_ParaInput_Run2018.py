import ROOT,os
from Core.BaseObject import BaseObject

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
inputFitFilePath    = "/home/lucien/public_html/Higgs/HToZdZd/Parametrization/2019-08-21_136p1_RunII_RatioCut0p05/shape.root"
inputParaFilePath   = "/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-08-21_Run2018/ZPlusX/StatInput.root"
outputDir           = os.path.dirname(inputParaFilePath)
outputFileName      = "ParaShape.root"

fitFuncName_Mu      = "Mu_shape"
fitFuncName_El      = "El_shape"
binList             = [
                        BaseObject("Mu",fitFuncName=fitFuncName_Mu,inputParaName="Mu"),
                        BaseObject("El",fitFuncName=fitFuncName_El,inputParaName="El"),
                        ]

# _____________________________________________________________________________ ||
inputFitFile = ROOT.TFile(inputFitFilePath,"READ")
inputParaFile = ROOT.TFile(inputParaFilePath,"READ")
outputFile = ROOT.TFile(os.path.join(outputDir,outputFileName),"RECREATE")
outputFile.cd()
for b in binList:
    fitFunc = inputFitFile.Get(b.fitFuncName)
    paraInputHist = inputParaFile.Get(b.inputParaName)
    outputHist = paraInputHist.Clone(b.name)
    for ibin in range(1,outputHist.GetNbinsX()+1):
        x = outputHist.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,fitFunc.Eval(x))
    outputHist.Scale(paraInputHist.Integral()/outputHist.Integral())
    outputHist.Write()
    fitFunc.Write()
outputFile.Close()

# _____________________________________________________________________________ ||
