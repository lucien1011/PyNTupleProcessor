import os,ROOT,array

from Utils.System import system
from Core.mkdir_p import mkdir_p
from shutil import copy2

from Script.Bin import Bin

from interpolate_sig_func import makePlot,SignalModel

# ________________________________________________________________________________________________ ||
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gStyle.SetOptFit()

User = os.environ['USER']

# ________________________________________________________________________________________________ ||
makeTFile       = True
makePlots       = True
fitlist         = ["pol2","pol3","pol4","pol5","pol6"]

in_path         = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-12-02_m4lSR-m4lSB_HZZd-Run2016/"
inputDir        = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+in_path
TFileName       = "StatInput.root"

outputDir       = "/home/"+User+"/public_html/Higgs/DarkZ/Interpolation/2019-12-02_m4lSR-m4lSB_HZZd_Run2016/HZZd/"

# ________________________________________________________________________________________________ ||
signals = [
            #SignalModel("HZZd_M1",1),
            #SignalModel("HZZd_M2",2),
            #SignalModel("HZZd_M3",3),
            SignalModel("HZZd_M4",4),
            SignalModel("HZZd_M7",7),
            #SignalModel("HZZd_M10",10),
            SignalModel("HZZd_M15",15),
            SignalModel("HZZd_M20",20),
            SignalModel("HZZd_M25",25),
            SignalModel("HZZd_M30",30),
            SignalModel("HZZd_M30",35),
            ]
bins    = [
            Bin("MuMu_HiggsSR",0.02),
            Bin("ElMu_HiggsSR",0.02),
            Bin("ElEl_HiggsSR",0.05),
            Bin("MuEl_HiggsSR",0.05),
            ]

# ________________________________________________________________________________________________ ||
print("Input directory: "+inputDir)
print("Output directory: "+outputDir)

mkdir_p(outputDir)
#copy2('/home/rosedj1/index.php',outputDir)

for power in fitlist:
    for b in bins:
        if (makePlot):
            c = ROOT.TCanvas()
        if (makeTFile):
            outFile = ROOT.TFile(os.path.join(outputDir,b.histName+"_"+power+".root"),"RECREATE")
        x_points = []
        err_points = []
        y_points = []
        for sig in signals:
            fName = os.path.join(inputDir,sig.sig_name,TFileName)
            f = ROOT.TFile(fName,"READ")
            hist = f.Get(b.histName)
            error = ROOT.Double(0.)
            x1,x2 = b.getWindowWidth(sig.centre)
            integral = hist.IntegralAndError(hist.GetXaxis().FindBin(x1),hist.GetXaxis().FindBin(x2),error)
            x_points.append(sig.centre)
            y_points.append(integral)
            err_points.append(error)
            f.Close()
        gr = makePlot(x_points,y_points,err_points)
        gr.GetYaxis().SetRangeUser(0.,10.)
        func = ROOT.TF1(b.histName+"_fitFunc", power, 0., 35.)
        gr.Fit(func,"q")  # q suppresses printing (quiet)
        if (makePlot):
            gr.Draw()
            c.Draw()
            c.SaveAs(os.path.join(outputDir,b.histName+"_"+power+".pdf"))
            c.SaveAs(os.path.join(outputDir,b.histName+"_"+power+".png"))
            del c
        if (makeTFile):
            outFile.cd()
            gr.Write()
            func.Write()
