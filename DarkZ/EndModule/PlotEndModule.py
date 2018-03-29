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
        for isample,sample in enumerate(collector.samples):
            for plot in self.plots:
                hist = collector.getObj(sample,plot.rootSetting[1])
                hist.SetStats(0)
                hist.Draw()
                c.SaveAs(outputDir+sample+"-"+plot.key+".png")

