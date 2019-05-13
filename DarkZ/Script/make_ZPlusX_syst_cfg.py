import ROOT,os
from Core.Utils.printFunc import pyPrint
from Utils.System import system

ROOT.gROOT.SetBatch(ROOT.kTRUE)

def clearHist(h):
    for i in range(1,h.GetNbinsX()+1):
        if h.GetBinContent(i) < 0.: h.SetBinContent(i,0.)

def getIntegralAndError(hist):
    clearHist(hist)
    err = ROOT.Double(0.)
    integral = hist.IntegralAndError(1,hist.GetNbinsX()+1,err)
    return integral,err

# ________________________________________________________________________________ ||
#out_path    = "ZPlusX/Systematic/2019-05-03_Run2016/"
#out_path    = "ZPlusX/Systematic/2019-05-03_Run2017/"
out_path    = "ZPlusX/Systematic/2019-05-03_Run2018/"

User        = os.environ['USER']
inputPath   = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path+"/ZPlusX/DataMCDistribution.root"
histNames    = [
        "Z2_4e_mass",
        "Z2_2mu2e_mass",
        "Z2_4mu_mass",
        "Z2_2e2mu_mass",
        ]

pyPrint("Input path: "+inputPath)

# ________________________________________________________________________________ ||
f           = ROOT.TFile.Open(inputPath)
for histName in histNames:
    pyPrint("-"*20)
    pyPrint(histName)
    h_nominal   = f.Get(histName)
    integral_nominal,error_nominal = getIntegralAndError(h_nominal)
    pyPrint("Nominal: "+str(integral_nominal)+" +/- "+str(error_nominal))
    
    h_UniIso = f.Get(histName+"_UniIso")
    integral_UniIso,error_UniIso = getIntegralAndError(h_UniIso)
    pyPrint("Nominal: "+str(integral_UniIso)+" +/- "+str(error_UniIso))
    
    h_AsymIso = f.Get(histName+"_AsymIso")
    integral_AsymIso,error_AsymIso = getIntegralAndError(h_AsymIso)
    pyPrint("Nominal: "+str(integral_AsymIso)+" +/- "+str(error_AsymIso))
    
    syst = max([
                abs(integral_nominal-integral_UniIso)/integral_nominal,
                abs(integral_nominal-integral_AsymIso)/integral_nominal,
                ]
                )
    pyPrint("Systematic: %4.2f %%"%(syst*100.))
