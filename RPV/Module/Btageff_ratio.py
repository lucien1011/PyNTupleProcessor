from Core.EndModule import EndModule

import os,ROOT

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
        histList = []
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            #if not collector.mergeSamples and collector.sampleDict[sample].isSignal: continuei
            h1 = ROOT.TH2D("BTageff"+sample, "BTageff"+sample, 10,0.,200.,10,-2.4,2.4)
            h2 = ROOT.TH2D("CTageff"+sample, "CTageff"+sample, 10,0.,200.,10,-2.4,2.4)
            h3 = ROOT.TH2D("LTageff"+sample, "LTageff"+sample, 10,0.,200.,10,-2.4,2.4)

            for p in hist_name: 
                h = collector.getObj(sample,p)
                histList.append([h,sample,p])
            for h,s,p in histList:
                if s == sample:
                    if p == "BTageffNum":
                        h1 = h
                    if p == "BTageffDem": #and Btemp != None:
                        h1.Divide(h)
                        h1.SaveAs("BTageff"+sample+".png")
                        #self.writer.objs["BTageff"+sample] = Btemp
                    if p == "CTageffNum":
                        h2 = h
                    if p == "CTageffDem": #and Ctemp != None:
                        h2.Divide(h)
                        h2.SaveAs("CTageff"+sample+".png")
                        #self.writer.objs["CTageff"+sample] = Ctemp
                    if p == "LTageffNum":
                        h3 = h
                    if p == "LTageffDem": #and Ltemp != None:
                        h3.Divide(h)
                        h3.SaveAs("LTageff"+sample+".png")
                        #self.writer.objs["LTageff"+sample] = Ltemp

        return True
