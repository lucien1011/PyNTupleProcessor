from Core.EndModule import EndModule

import os,ROOT,math

ROOT.gROOT.SetBatch(ROOT.kTRUE)

class PlotEndModule(EndModule):
    def __init__(self,outputDir,plots):
        self.outputDir = outputDir
        self.plots = plots

    def __call__(self,collector):
        c = ROOT.TCanvas()
        outputDir = self.outputDir
        if not os.path.exists(os.path.abspath(outputDir)):
            os.makedirs(os.path.abspath(outputDir))
        #outputFile = ROOT.TFile(outputDir+"SkimTreeGasGain.root","RECREATE")
        for plot in self.plots:
            maximum = max([collector.getObj(sample,plot.rootSetting[1]).GetMaximum() for isample,sample in enumerate(collector.samples)])
            leg = ROOT.TLegend(0.63,0.58,0.89,0.87)
            for isample,sample in enumerate(collector.samples):
                hist = collector.getObj(sample,plot.rootSetting[1])
                leg.AddEntry(hist,sample)
                hist.SetStats(0)
                hist.SetLineColor(isample+1)
                hist.GetYaxis().SetRangeUser(0.,1.2*maximum)
                if isample:
                    hist.Draw("same")
                else:
                    hist.Draw()
            leg.Draw()
            c.SaveAs(outputDir+plot.key+".png")
            c.SaveAs(outputDir+plot.key+".pdf")

