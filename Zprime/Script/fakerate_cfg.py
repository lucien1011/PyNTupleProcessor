import ROOT
import numpy

ROOT.gROOT.SetBatch(ROOT.kTRUE)

inputPath_pass   = "/raid/raid7/kshi/Zprime/Zto4l/FakeRate/Run2017/2020-03-13/finalstate_mmmm/2P2F/Lep3/passIso_endcap/Data2017/DataMCDistribution.root"
inputPath_fail   = "/raid/raid7/kshi/Zprime/Zto4l/FakeRate/Run2017/2020-03-13/finalstate_mmmm/2P2F/Lep3/failIso_endcap/Data2017/DataMCDistribution.root"
outputPath  = "/home/kshi/public_html/Zprime/Zto4l/FakeRate/Run2017/2020-03-13/finalstate_mmmm/2P2F/Lep3/fr_ratio/fr_endcap.pdf"
file_outputPath = "/raid/raid7/kshi/Zprime/Zto4l/FakeRate/Run2017/2020-03-13/finalstate_mmmm/2P2F/Lep3/fr_ratio/ratioPlot.root"
histName    = "mu3Pt_4mu"

inputFile_pass   = ROOT.TFile(inputPath_pass,"READ")
inputFile_fail   = ROOT.TFile(inputPath_fail,"READ")
pass_hist        = inputFile_pass.Get(histName)
fail_hist        = inputFile_fail.Get(histName)

#ratioPlot = new ROOT.TFile("ratioPlot_endcap.root","NEW")

xbins = numpy.array([0.,2.,4.,6.,8.,10.,13.,17.,20.,25.,35.,100.])
#print xbins
histList = [
        pass_hist,
        fail_hist,
        ]

#for hist in histList:
    #for i in range(9) :
        #hist.SetBinContent(i,i)
    #hist.GetXaxis().SetRangeUser(0.,100.)
    #hist = hist.Rebin(8,"fr",xbins)
    #hist = hist.Sumw2

pass_hist.GetXaxis().SetRangeUser(0.,100.)
pass_hist.Sumw2()
pass_hist_new = pass_hist.Rebin(11,"fr_endcap",xbins)
fail_hist.GetXaxis().SetRangeUser(0.,100.)
fail_hist.Sumw2()
fail_hist_new = fail_hist.Rebin(11,"fr_endcap",xbins)

#x = fail_hist_new.GetBinContent(1)
#print x


c = ROOT.TCanvas()
fakerate    = pass_hist_new.Clone()
fakerate.Divide(fakerate,fail_hist_new,1,1)
#fakerate.GetXaxis().SetRangeUser(0.,100.)
#fakerate.Sumw2()
#fakerate_new = fakerate.Rebin(8,"fr",xbins)

fakerate.Draw()
#fail_hist_new.Draw()
c.SaveAs(outputPath)


fakerate    = pass_hist_new.Clone()
fakerate.Divide(fakerate,fail_hist_new,1,1)

ratioPlot_endcap    = ROOT.TFile.Open(file_outputPath,"UPDATE")
ratioPlot_endcap.cd()
fakerate.Write()
ratioPlot_endcap.Close()

