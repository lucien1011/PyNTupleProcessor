import os,ROOT,array

from Utils.System import system
from Core.mkdir_p import mkdir_p

from DarkZ.Script.Bin import Bin

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# ________________________________________________________________________________________________ ||
def makePlot(x_points,y_points,err_points):
    if len(x_points) != len(y_points) or len(x_points) != len(err_points) or len(err_points) != len(y_points): raise RuntimeError
    n = len(x_points)
    gr = ROOT.TGraphErrors(n,array.array('d',x_points),array.array('d',y_points),array.array('d',[0.]*n),array.array('d',err_points))
    return gr

class SignalModel(object):
    def __init__(self,
            sig_name,
            centre,
            ):
        self.sig_name = sig_name
        self.centre = centre

draw_option = 'Draw'
tfile_option = 'TFile'
both_option = 'Both'

# ________________________________________________________________________________________________ ||
#out_path    = "DarkPhotonSR/StatInput/2019-07-18_Run2016/"
#out_path    = "DarkPhotonSR/StatInput/2019-08-19_Run2016/"
#out_path    = "DarkPhotonSR/StatInput/2019-08-19_Run2017/"
#out_path    = "DarkPhotonSR/StatInput/2019-08-19_Run2018/"
out_path    = "DarkPhotonSR/StatInput/2019-08-21_Run2016/"
#out_path    = "DarkPhotonSR/StatInput/2019-08-21_Run2017/"
#out_path    = "DarkPhotonSR/StatInput/2019-08-21_Run2018/"


# ________________________________________________________________________________________________ ||
outputDir   = "/home/lucien/public_html/Higgs/HToZdZd/Interpolation/"+os.path.basename(os.path.normpath(out_path))

# ________________________________________________________________________________________________ ||
inputDir    = system.getStoragePath()+"/lucien/Higgs/HToZdZd/"+out_path
TFileName   = "StatInput.root"
saveOption  = "Both"

# ________________________________________________________________________________________________ ||
signals = [
                SignalModel("HToZdZd_MZD"+str(m),m) for m in range(5,11)+range(15,61,5)
            ]
bins = [
        Bin("MuMu",0.02),
        Bin("MuMu",0.02),
        Bin("MuMu",0.02),
        Bin("ElMu",0.02),
        Bin("ElMu",0.02),
        Bin("ElMu",0.02),
        Bin("ElEl",0.05),
        Bin("ElEl",0.05),
        Bin("ElEl",0.05),
        Bin("MuEl",0.05),
        Bin("MuEl",0.05),
        Bin("MuEl",0.05),
        Bin("Mu",0.02),
        Bin("El",0.05),
        ]

# ________________________________________________________________________________________________ ||
print("Input directory: "+inputDir)
print("Output directory: "+outputDir)

mkdir_p(outputDir)

for b in bins:
    if saveOption == draw_option or saveOption == both_option:
        c = ROOT.TCanvas()
    if saveOption == tfile_option or saveOption == both_option:
        outFile = ROOT.TFile(os.path.join(outputDir,b.histName+".root"),"RECREATE")
    x_points = []
    err_points = []
    y_points = []
    for sig in signals:
        fName = os.path.join(inputDir,sig.sig_name,TFileName)
        f = ROOT.TFile(fName,"READ")
        hist = f.Get(b.histName)
        error = ROOT.Double(0.)
        x1,x2 = b.getWindowWidth(sig.centre)
        #integral = hist.IntegralAndError(hist.GetXaxis().FindBin(x1),hist.GetXaxis().FindBin(x2),error)
        integral = hist.IntegralAndError(0,hist.GetNbinsX()+1,error)
        x_points.append(sig.centre)
        y_points.append(integral)
        err_points.append(error)
        f.Close()
    gr = makePlot(x_points,y_points,err_points)
    func = ROOT.TF1(b.histName+"_fitFunc", "landau", 0., 80.)
    gr.Fit(func)
    if saveOption == draw_option or saveOption == both_option:
        gr.Draw()
        c.SaveAs(os.path.join(outputDir,b.histName+".pdf"))
        del c
    if saveOption == tfile_option or saveOption == both_option:
        outFile.cd()
        gr.Write()
        func.Write()
