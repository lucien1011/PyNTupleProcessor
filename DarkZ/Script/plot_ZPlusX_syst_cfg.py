import ROOT

ROOT.gROOT.SetBatch(ROOT.kTRUE)

# ________________________________________________________________________________ ||
inputPath       = "/raid/raid7/lucien/Higgs/DarkZ/ParaInput/DarkPhotonSelection_m4l118To130_Nominal/2018-11-20_DarkPhotonSR-Unblinding/ZPlusX/StatInput.root"
outputPath      = "/home/lucien/public_html/Higgs/DarkZ/ZPlusX/Systematic/2018-11-20/mZ2.pdf"
histName        = "comb"
rebinFactor     = 20

# ________________________________________________________________________________ ||
inputFile       = ROOT.TFile(inputPath,"READ")
nominal_hist    = inputFile.Get(histName)
uniIso_hist     = inputFile.Get(histName+"_FRUniIso")
asymIso_hist    = inputFile.Get(histName+"_FRAsymIso")

histList = [
        nominal_hist,
        uniIso_hist, 
        asymIso_hist,
        ]
maximum = max([h.GetMaximum() for h in histList])
for hist in histList:
    hist.Rebin(rebinFactor)
    hist.SetStats(0)
    hist.GetXaxis().SetRangeUser(0.,60.)
    hist.GetYaxis().SetRangeUser(0.,3.)

c = ROOT.TCanvas()
uniIso_hist.SetLineColor(ROOT.kRed)
asymIso_hist.SetLineColor(ROOT.kGreen)
nominal_hist.Draw("same")
uniIso_hist.Draw("same")
asymIso_hist.Draw("same")
c.SaveAs(outputPath)

uniIso_ratio = uniIso_hist.Clone()
uniIso_ratio.Divide(nominal_hist)
asymIso_ratio = asymIso_hist.Clone()
asymIso_ratio.Divide(nominal_hist)
#for ibin in range(1,nominal_hist.GetNbinsX()+1):
#    uniIso_ratio.SetBinError(ibin,0.1.)
#    asymIso_ratio.SetBinError(ibin,0.1)
#uniIso_ratio.GetYaxis().SetRangeUser(0.,3.)
#asymIso_ratio.GetYaxis().SetRangeUser(0.,3.)
uniIso_ratio.Draw()
asymIso_ratio.Draw("same")
c.SaveAs(outputPath.replace(".pdf","_ratio.pdf"))

# ________________________________________________________________________________ ||
