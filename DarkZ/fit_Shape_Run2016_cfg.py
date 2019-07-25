import ROOT,os
from Core.mkdir_p import mkdir_p

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# _____________________________________________________________________________ ||
inputPath       = "/raid/raid7//lucien/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/2019-07-25_Run2016/ZPlusX/DataMCDistribution.root"
outputDir       = "/raid/raid7//lucien/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/2019-07-25_Run2016/ZPlusX/"
histNames       = [
                        "mZ2_4e",
                        "mZ2_low-m4l_4e",
                        "mZ2_mid-m4l_4e",
                        "mZ2_high-m4l_4e",
                        "mZ2_2mu2e",
                        "mZ2_low-m4l_2mu2e",
                        "mZ2_mid-m4l_2mu2e",
                        "mZ2_high-m4l_2mu2e",
                        "mZ2_4mu",
                        "mZ2_low-m4l_4mu",
                        "mZ2_mid-m4l_4mu",
                        "mZ2_high-m4l_4mu",
                        "mZ2_2e2mu",
                        "mZ2_low-m4l_2e2mu",
                        "mZ2_mid-m4l_2e2mu",
                        "mZ2_high-m4l_2e2mu",
                    ]
drawFit         = True

# _____________________________________________________________________________ ||
inputFile = ROOT.TFile(inputPath,"READ")
mkdir_p(os.path.dirname(outputDir))
if drawFit: c = ROOT.TCanvas()
outputFile = ROOT.TFile(os.path.join(outputDir,"shape.root"),"RECREATE")
for histName in histNames:
    inputHist = inputFile.Get(histName)
    inputHistClone = inputHist.Clone()
    inputHist.Rebin(20)
    inputHist.Fit("landau")
    func = inputHist.GetFunction("landau")
    func.SetName(histName+"_shape")
    outputHist = inputHistClone.Clone(histName+"_shapehist")
    for ibin in range(1,inputHistClone.GetNbinsX()+1):
        x_value = inputHistClone.GetXaxis().GetBinCenter(ibin)
        outputHist.SetBinContent(ibin,func.Eval(x_value))
    outputHist.Scale(inputHist.Integral()/outputHist.Integral())
    outputFile.cd()
    inputHist.Write()
    outputHist.Write()
    func.Write()
    if drawFit:
        inputHist.SetStats(0)
        inputHist.Draw()
        c.SaveAs(os.path.join(outputDir,"fit_"+histName+".pdf"))
inputFile.Close()

# _____________________________________________________________________________ ||

