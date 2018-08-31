from Core.EndModule import EndModule

import os,ROOT,numpy

from array import array

class Btageff_ratio(EndModule):
    def __init__(self,outputDir):
        self.outputDir = outputDir

    def begin(self,collector):
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            h1 = ROOT.TH2D("BTageff"+sample, "BTageff"+sample, 10,0.,200.,10,-2.4,2.4)
            h2 = ROOT.TH2D("CTageff"+sample, "CTageff"+sample, 10,0.,200.,10,-2.4,2.4)
            h3 = ROOT.TH2D("LTageff"+sample, "LTageff"+sample, 10,0.,200.,10,-2.4,2.4)


            #if "BTageff"+sample not in self.writer.objs:
                #self.writer.book("BTageff"+sample,"TH2D","BTageff"+sample,"",10,0.,200.,10,-2.4,2.4)
            #if "CTageff"+sample not in self.writer.objs:
                #self.writer.book("CTageff"+sample,"TH2D","CTageff"+sample,"",10,0.,200.,10,-2.4,2.4)
            #if "LTageff"+sample not in self.writer.objs:
                #self.writer.book("LTageff"+sample,"TH2D","LTageff"+sample,"",10,0.,200.,10,-2.4,2.4)
        
    def __call__(self,collector):
        #self.begin(collector)
        self.analyze(collector)

    def analyze(self,collector):

        hist_name = ["BTageffNum", "BTageffDem", "CTageffNum", "CTageffDem", "LTageffNum", "LTageffDem"] 
        pt_bins = numpy.array([20, 30, 50, 70, 100, 140, 200, 300, 600, 1000], dtype='float64')
        eta_bins = numpy.array([0., 2.4], dtype='float64')
        histList = []
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            #if not collector.mergeSamples and collector.sampleDict[sample].isSignal: continuei
            h1 = ROOT.TH2D("BTageff"+sample, "BTageff"+sample, 1,20.,1000.,1,-2.4,2.4)
            h2 = ROOT.TH2D("CTageff"+sample, "CTageff"+sample, 9,pt_bins,1,eta_bins)
            h3 = ROOT.TH2D("LTageff"+sample, "LTageff"+sample, 9,pt_bins,1,eta_bins)
            c1 = ROOT.TCanvas("BTageff"+sample) 
            c2 = ROOT.TCanvas("CTageff"+sample)
            c3 = ROOT.TCanvas("LTageff"+sample)

            for p in hist_name: 
                h = collector.getObj(sample,p)
                histList.append([h,sample,p])
            for h,s,p in histList:
                if s == sample:
                    if p == "BTageffNum":
                        h1 = h
                        h1.SetBins(1,20.,1000.,1,-2.4,2.4)
                    if p == "BTageffDem": #and Btemp != None:
                        h.SetBins(1,20.,1000.,1,-2.4,2.4)
                        h1.Divide(h)
                        c1.cd()
                        h1.SetStats(0)
                        h1.Draw("colz")
                        c1.SaveAs("BTageff"+sample+".png")
                        #h1.SaveAs("BTageff"+sample+".png")
                        #self.writer.objs["BTageff"+sample] = Btemp
                    if p == "CTageffNum":
                        h2 = h
                        h2.SetBins(9,pt_bins,1,eta_bins)
                    if p == "CTageffDem": #and Ctemp != None:
                        h.SetBins(9,pt_bins,1,eta_bins)
                        h2.Divide(h)
                        c2.cd()
                        h2.SetStats(0)
                        h2.Draw("colz")
                        c2.SaveAs("CTageff"+sample+".png")
                        #h2.SaveAs("CTageff"+sample+".png")
                        #self.writer.objs["CTageff"+sample] = Ctemp
                    if p == "LTageffNum":
                        h3 = h
                        h3.SetBins(9,pt_bins,1,eta_bins)
                    if p == "LTageffDem": #and Ltemp != None:
                        h.SetBins(9,pt_bins,1,eta_bins)
                        h3.Divide(h)
                        c3.cd()
                        h3.SetStats(0)
                        h3.Draw("colz")
                        c3.SaveAs("LTageff"+sample+".png")
                        #h3.SaveAs("LTageff"+sample+".png")
                        #self.writer.objs["LTageff"+sample] = Ltemp

        return True
