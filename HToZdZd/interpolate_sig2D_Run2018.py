import os,ROOT,array

from Utils.System import system
from Core.mkdir_p import mkdir_p
from shutil import copy2

from Core.BaseObject import BaseObject

from DarkZ.interpolate_sig_func import makePlot,SignalModel

from HToZdZd.Dataset.Run2018.SkimTree_DarkPhoton_m4l70_HZdZdInterpolation import mass_points 

def getCountAndError2D(hist,central,x_width,y_width):
    x_lower_value = central*(1.-x_width)
    x_upper_value = central*(1.+x_width)
    y_lower_value = central*(1.-y_width)
    y_upper_value = central*(1.+y_width)
    error = ROOT.Double(0.)
    integral = hist.IntegralAndError(
            hist.GetXaxis().FindFixBin(x_lower_value),
            hist.GetXaxis().FindFixBin(x_upper_value),
            hist.GetYaxis().FindFixBin(y_lower_value),
            hist.GetYaxis().FindFixBin(y_upper_value),
            error,
            )
    return integral,error

# ________________________________________________________________________________________________ ||
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gStyle.SetOptFit()

User = os.environ['USER']

# ________________________________________________________________________________________________ ||
makeTFile       = True
makePlots       = True
fitlist         = ["pol5","pol6","pol7","pol8","pol9","landau",]

in_path         = "DarkPhotonSR/StatInput/2019-12-10_SignalInterpolation2D_Run2018/"
inputDir        = system.getStoragePath()+"/"+User+"/Higgs/HToZdZd/"+in_path
TFileName       = "StatInput.root"

outputDir       = system.getPublicHtmlPath()+"/Higgs/HToZdZd/Interpolation/"+os.path.basename(os.path.normpath(in_path))

y_range         = [0.,0.5]
draw_option     = "AP"

# ________________________________________________________________________________________________ ||
signals = [
                SignalModel("HToZdZd_M"+str(m),m) for m in mass_points
            ]

bins    = [
            BaseObject("MuMu",histName="MuMu",x_width=0.02,y_width=0.02),
            BaseObject("ElMu",histName="ElMu",x_width=0.05,y_width=0.02),
            BaseObject("ElEl",histName="ElEl",x_width=0.05,y_width=0.05),
            BaseObject("MuEl",histName="MuEl",x_width=0.02,y_width=0.05),
            ]

# ________________________________________________________________________________________________ ||
print("Input directory: "+inputDir)
print("Output directory: "+outputDir)
print("Mass points: "+", ".join([str(s.centre) for s in signals]))

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
            #error = ROOT.Double(0.)
            #integral = hist.IntegralAndError(hist.GetXaxis().FindBin(x1),hist.GetXaxis().FindBin(x2),error)
            integral,error = getCountAndError2D(hist,sig.centre,b.x_width,b.y_width)
            integral *= sig.yieldFactor
            error *= sig.yieldFactor
            x_points.append(sig.centre)
            y_points.append(integral)
            err_points.append(error)
            f.Close()
        gr = makePlot(x_points,y_points,err_points)
        gr.GetYaxis().SetRangeUser(*y_range)
        func = ROOT.TF1(b.histName+"_fitFunc", power, 0., 35.)
        gr.Fit(func,"q")  # q suppresses printing (quiet)
        if (makePlot):
            gr.Draw(draw_option)
            c.Draw()
            c.SaveAs(os.path.join(outputDir,b.histName+"_"+power+".pdf"))
            c.SaveAs(os.path.join(outputDir,b.histName+"_"+power+".png"))
            del c
        if (makeTFile):
            outFile.cd()
            gr.Write()
            func.Write()
