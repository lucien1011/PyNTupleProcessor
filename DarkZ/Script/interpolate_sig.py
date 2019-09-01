import os,ROOT,array

from Utils.System import system
from Core.mkdir_p import mkdir_p
from shutil import copy2

from Bin import Bin

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gStyle.SetOptFit()

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

User = os.environ['USER']

makeTFile = True
makePlots = True
fitlist = ["pol2","pol3","pol4","pol5"]
#draw_option = 'Draw'
#tfile_option = 'TFile'
#saveOption = "TFile"

# ________________________________________________________________________________________________ ||
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-05-23_m4lSR-m4lSB_HZZd-ppZZd/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2016/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2017/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2018/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2016/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2017/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2018/"

in_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2016/"
#in_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2017/"
#in_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2018/"

inputDir = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+in_path
TFileName = "StatInput.root"
# ________________________________________________________________________________________________ ||
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/HZZd/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2016/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/ppZZd/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2016/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/HZZd/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2017/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/ppZZd/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2017/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/HZZd/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2018/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/ppZZd/2019-07-17_m4lSR-m4lSB_HZZd-ppZZd_Run2018/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2016/ppZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2017/ppZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2018/ppZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2016/HZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2017/HZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-07-31_m4lSR-m4lSB_HZZd-ppZZd_Run2018/HZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2016/HZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2017/HZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2018/HZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2016/ppZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2017/ppZZd/"
#outputDir = "/home/lucien/public_html/Higgs/DarkZ/Interpolation/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run2018/ppZZd/"

outputDir = "/home/"+User+"/public_html/Higgs/DarkZ/Interpolation/20190823_m4lSR-m4lSB_HZZd-ppZZd_Run2016/ppZZd/"
#outputDir = "/home/"+User+"/public_html/Higgs/DarkZ/Interpolation/20190823_m4lSR-m4lSB_HZZd-ppZZd_Run2016/HZZd/"
# ________________________________________________________________________________________________ ||
signals = [
                SignalModel("ppZZd4l_M5",5),
                SignalModel("ppZZd4l_M15",15),
                SignalModel("ppZZd4l_M30",30),
                #SignalModel("HZZd_M4",4),
                #SignalModel("HZZd_M7",7),
                #SignalModel("HZZd_M10",10),
                #SignalModel("HZZd_M15",15),
                #SignalModel("HZZd_M20",20),
                #SignalModel("HZZd_M25",25),
                #SignalModel("HZZd_M30",30),
            ]
bins = [
        Bin("MuMu_HiggsLowSB",0.02),
        Bin("MuMu_HiggsSR",0.02),
        Bin("MuMu_HiggsHighSB",0.02),
        Bin("ElMu_HiggsLowSB",0.02),
        Bin("ElMu_HiggsSR",0.02),
        Bin("ElMu_HiggsHighSB",0.02),
        Bin("ElEl_HiggsLowSB",0.05),
        Bin("ElEl_HiggsSR",0.05),
        Bin("ElEl_HiggsHighSB",0.05),
        Bin("MuEl_HiggsLowSB",0.05),
        Bin("MuEl_HiggsSR",0.05),
        Bin("MuEl_HiggsHighSB",0.05),
        #Bin("2mu_HiggsLowSB",0.02),
        #Bin("2e_HiggsLowSB",0.05),
        #Bin("2mu_HiggsSR",0.02),
        #Bin("2e_HiggsSR",0.05),
        #Bin("2mu_HiggsHighSB",0.02),
        #Bin("2e_HiggsHighSB",0.05),
        ]

# ________________________________________________________________________________________________ ||
print("Input directory: "+inputDir)
print("Output directory: "+outputDir)

mkdir_p(outputDir)
copy2('/home/rosedj1/index.php',outputDir)

for power in fitlist:
    for b in bins:
        if (makePlot):
            c = ROOT.TCanvas()
    #         leg = TLegend(0.65,0.7,0.9,0.9)
        if (makeTFile):
            outFile = ROOT.TFile(os.path.join(outputDir,b.histName+"_"+power+".root"),"RECREATE")
        x_points = []
        err_points = []
        y_points = []
        # Get events in StatInput.root
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
    #     gr.SetTitle("")
        func = ROOT.TF1(b.histName+"_fitFunc", power, 0., 35.)
        gr.Fit(func,"q")  # q suppresses printing (quiet)
        if (makePlot):
    #         c.BuildLegend(0,0,0,0)
    #         gr.PaintStats(func)
            gr.Draw()
    #         ROOT.gPad.Update()
    #         ROOT.gStyle.SetOptStat(0111)
    #         c.Update()
            c.Draw()
            c.SaveAs(os.path.join(outputDir,b.histName+"_"+power+".pdf"))
            c.SaveAs(os.path.join(outputDir,b.histName+"_"+power+".png"))
            del c
        if (makeTFile):
            outFile.cd()
            gr.Write()
            func.Write()
