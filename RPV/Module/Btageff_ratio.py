from Core.EndModule import EndModule

import os,ROOT

class Btageff_ratio(EndModule):
    def __init__(self,outputDir,):
        self.outputDir = outputDir

    def __call__(self,collector):
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            if "BTageff"+sample not in self.writer.objs:
                self.writer.book("BTageff"+sample,"TH2D","BTageff"+sample,"",10,0.,200.,10,-2.4,2.4)
            if "CTageff"+sample not in self.writer.objs:
                self.writer.book("CTageff"+sample,"TH2D","CTageff"+sample,"",10,0.,200.,10,-2.4,2.4)
            if "LTageff"+sample not in self.writer.objs:
                self.writer.book("LTageff"+sample,"TH2D","LTageff"+sample,"",10,0.,200.,10,-2.4,2.4)
        
    def analyze(self,collector):
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            if not collector.mergeSamples and collector.sampleDict[sample].isSignal: continue
            for p in enumerate(collector.sampleDict[sample]):                
                h = collector.getObj(p,plot.rootSetting[1])
                histList.append([h,sample,p])
            for h,sample,plot in histList:
                if histList[2] == "BTageffNum":
                    Btemp = h
                if histList[2] == "BTageffDem" and Btemp != None:
                    Btemp.Divide(h)
                    self.writer.objs["BTageff"+sample] = Btemp
                if histList[2] == "CTageffNum":
                    Ctemp = h
                if histList[2] == "CTageffDem" and Ctemp != None:
                    Ctemp.Divide(h)
                    self.writer.objs["CTageff"+sample] = Ctemp
                if histList[2] == "LTageffNum":
                    Ltemp = h
                if histList[2] == "LTageffDem" and Ltemp != None:
                    Ltemp.Divide(h)
                    self.writer.objs["LTageff"+sample] = Ltemp

        return True
