import ROOT,os
from Core.BaseObject import BaseObject

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
inputFitFilePath    = "/raid/raid7//lucien/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/2019-07-29_Run2018/ZPlusX/shape.root"
#inputParaFilePath   = "/raid/raid7//lucien/Higgs/DarkZ/ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2018/ZPlusX/StatInput.root"
inputParaFilePath   = "/raid/raid7//lucien/Higgs/DarkZ/ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2018/ZPlusX/StatInput.root"
outputDir           = os.path.dirname(inputParaFilePath)
outputFileName      = "ParaShape.root"

fitFuncName_4mu     = "mZ2_4mu_shape"
fitFuncName_2e2mu   = "mZ2_2e2mu_shape"
fitFuncName_4e      = "mZ2_4e_shape"
fitFuncName_2mu2e   = "mZ2_2mu2e_shape"
binList             = [
                        BaseObject("MuMu_HiggsSR",fitFuncName=fitFuncName_4mu,inputParaName="MuMu_HiggsSR"),
                        BaseObject("MuMu_HiggsLowSB",fitFuncName=fitFuncName_4mu,inputParaName="MuMu_HiggsLowSB"),
                        BaseObject("MuMu_HiggsHighSB",fitFuncName=fitFuncName_4mu,inputParaName="MuMu_HiggsHighSB"),
                        BaseObject("ElMu_HiggsSR",fitFuncName=fitFuncName_2e2mu,inputParaName="ElMu_HiggsSR"),
                        BaseObject("ElMu_HiggsLowSB",fitFuncName=fitFuncName_2e2mu,inputParaName="ElMu_HiggsLowSB"),
                        BaseObject("ElMu_HiggsHighSB",fitFuncName=fitFuncName_2e2mu,inputParaName="ElMu_HiggsHighSB"),
                        BaseObject("ElEl_HiggsSR",fitFuncName=fitFuncName_4e,inputParaName="ElEl_HiggsSR"),
                        BaseObject("ElEl_HiggsLowSB",fitFuncName=fitFuncName_4e,inputParaName="ElEl_HiggsLowSB"),
                        BaseObject("ElEl_HiggsHighSB",fitFuncName=fitFuncName_4e,inputParaName="ElEl_HiggsHighSB"),
                        BaseObject("MuEl_HiggsSR",fitFuncName=fitFuncName_2mu2e,inputParaName="MuEl_HiggsSR"),
                        BaseObject("MuEl_HiggsLowSB",fitFuncName=fitFuncName_2mu2e,inputParaName="MuEl_HiggsLowSB"),
                        BaseObject("MuEl_HiggsHighSB",fitFuncName=fitFuncName_2mu2e,inputParaName="MuEl_HiggsHighSB"),
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
