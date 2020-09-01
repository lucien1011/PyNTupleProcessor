import ROOT,os
from Core.BaseObject import BaseObject
from Utils.System import system

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
inputFitFilePath    = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-06_SR2D_hadd_RunII/ZPlusX/shape.root"
inputParaFilePath   = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-06_SR2D_Run2016/ZPlusX/StatInput.root"
#inputParaFilePath   = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-06_SR2D_Run2017/ZPlusX/StatInput.root"
#inputParaFilePath   = system.getStoragePath()+"/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-06_SR2D_Run2018/ZPlusX/StatInput.root"
outputDir           = os.path.dirname(inputParaFilePath)
outputFileName      = "ParaShape.root"
muWidth             = 0.02
elWidth             = 0.05
lowM                = 4.
highM               = 62.6
binList             = [
                        BaseObject("MuMu",fitFuncName="MuMu_shape",inputParaName="MuMu",cutPoints=[(lowM,lowM*(1.-muWidth)),(highM,highM*(1.-muWidth)),(highM,highM*(1.+muWidth)),(lowM,highM*(1.+muWidth)),]),
                        BaseObject("ElMu",fitFuncName="ElMu_shape",inputParaName="ElMu",cutPoints=[(lowM,lowM*(1.-elWidth)),(highM,highM*(1.-elWidth)),(highM,highM*(1.+elWidth)),(lowM,highM*(1.+elWidth)),]),
                        BaseObject("ElEl",fitFuncName="ElEl_shape",inputParaName="ElEl",cutPoints=[(lowM,lowM*(1.-elWidth)),(highM,highM*(1.-elWidth)),(highM,highM*(1.+elWidth)),(lowM,highM*(1.+elWidth)),]),
                        BaseObject("MuEl",fitFuncName="MuEl_shape",inputParaName="MuEl",cutPoints=[(lowM,lowM*(1.-muWidth)),(highM,highM*(1.-muWidth)),(highM,highM*(1.+muWidth)),(lowM,highM*(1.+muWidth)),]),
                        ]

# _____________________________________________________________________________ ||
inputFitFile = ROOT.TFile(inputFitFilePath,"READ")
inputParaFile = ROOT.TFile(inputParaFilePath,"READ")
outputFile = ROOT.TFile(os.path.join(outputDir,outputFileName),"RECREATE")
outputFile.cd()
for b in binList:
    fitFunc = inputFitFile.Get(b.fitFuncName)
    tcut = ROOT.TCutG(b.name+"_cut",len(b.cutPoints))
    for i,p in enumerate(b.cutPoints): tcut.SetPoint(i,p[0],p[1])
    paraInputHist = inputParaFile.Get(b.inputParaName).ProjectionX(b.name+"_px_norm",1,inputParaFile.Get(b.inputParaName).GetNbinsX()+1,"["+b.name+"_cut"+"]")
    outputHist = paraInputHist.Clone(b.name)
    for ibin in range(1,outputHist.GetNbinsX()+1):
        x = outputHist.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,fitFunc.Eval(x))
    outputHist.Scale(paraInputHist.Integral()/outputHist.Integral())
    outputHist.Write()
    fitFunc.Write()
outputFile.Close()

# _____________________________________________________________________________ ||
