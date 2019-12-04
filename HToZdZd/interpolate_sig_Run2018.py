import os,ROOT,array

from Utils.System import system
from Core.mkdir_p import mkdir_p
from shutil import copy2

from DarkZ.Script.Bin import Bin

from DarkZ.interpolate_sig_func import makePlot,SignalModel

from HToZdZd.Dataset.Run2018.SkimTree_DarkPhoton_m4l70_HZdZdInterpolation import mass_points 

# ________________________________________________________________________________________________ ||
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gStyle.SetOptFit()

User = os.environ['USER']

# ________________________________________________________________________________________________ ||
makeTFile       = True
makePlots       = True
fitlist         = ["pol5","pol6","pol7","pol8","pol9","landau",]

in_path         = "DarkPhotonSR/StatInput/2019-12-04_SignalInterpolation_Run2018/"
inputDir        = system.getStoragePath()+"/"+User+"/Higgs/HToZdZd/"+in_path
TFileName       = "StatInput.root"

outputDir       = "/home/lucien/public_html/Higgs/HToZdZd/Interpolation/"+os.path.basename(os.path.normpath(in_path))

y_range         = [0.,0.5]

# ________________________________________________________________________________________________ ||
signals = [
                SignalModel("HToZdZd_M"+str(m),m) for m in mass_points
            ]
bins    = [
            Bin("MuMu",0.02),
            Bin("ElMu",0.02),
            Bin("ElEl",0.05),
            Bin("MuEl",0.05),
            ]

# ________________________________________________________________________________________________ ||
print("Input directory: "+inputDir)
print("Output directory: "+outputDir)

mkdir_p(outputDir)

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
        gr.GetYaxis().SetRangeUser(*y_range)
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
