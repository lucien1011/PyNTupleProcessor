from Core.EndModule import EndModule

import os,ROOT,numpy

from array import array

class Fit(EndModule):
    def __init__(self,outputDir):
        self.outputDir = outputDir

    def begin(self,collector):
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            h1 = ROOT.TH1D("FitGaus_Z1"+sample, "FitGaus_Z1"+sample, 480,0.,120.)
            h2 = ROOT.TH1D("FitGaus_Z2"+sample, "FitGaus_Z2"+sample, 600,0.,100.)

        
    def __call__(self,collector):
        #self.begin(collector)
        self.analyze(collector)

    def analyze(self,collector):
        names = self.__dict__
        hist_name = ["FitGaus_Z1","FitGaus_Z2"]
        histList = []
        #c1 = ROOT.TCanvas("FitGaus_Z1")
        #c2 = ROOT.TCanvas("FitGaus_Z2")
        i = 0
        sam = []
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            #i = i + 1
            sam.append(sample)
            c1 = ROOT.TCanvas("FitGaus_Z1"+sample)
            c2 = ROOT.TCanvas("FitGaus_Z2"+sample)

            for p in hist_name: 
                h = collector.getObj(sample,p)
                histList.append([h,sample,p])

            for h,s,p in histList:
                if s == sample: 
                    if p == "FitGaus_Z1":
                        h1 = h
                        if sample == "zpToMuMu_M1" or sample == "zpToMuMu_M2":
                            h1.GetXaxis().SetRangeUser(0.,10.)
                            h1.Fit("gaus","V","E1")
                        elif sample == "zpToMuMu_M3" or sample == "zpToMuMu_M4" or sample == "zpToMuMu_M5":
                            h1.GetXaxis().SetRangeUser(0.,10.)
                            h1.Fit("gaus","V","E1")
                        elif sample == "zpToMuMu_M10":
                            h1.GetXaxis().SetRangeUser(5.,15.)
                            h1.Fit("gaus","V","E1")
                        elif sample == "zpToMuMu_M15":
                            h1.GetXaxis().SetRangeUser(10.,20.)
                            h1.Fit("gaus","V","E1",14.5,15.5)
                        elif sample == "zpToMuMu_M20":
                            h1.GetXaxis().SetRangeUser(15.,25.)
                            h1.Fit("gaus","V","E1",19.5,20.5)
                        elif sample == "zpToMuMu_M25":
                            h1.GetXaxis().SetRangeUser(20.,30.)
                            h1.Fit("gaus","V","E1",24,26)
                        elif sample == "zpToMuMu_M30":
                            h1.GetXaxis().SetRangeUser(25.,35.)
                            h1.Fit("gaus","V","E1",29,31)
                        elif sample == "zpToMuMu_M35":
                            h1.GetXaxis().SetRangeUser(30.,40.)
                            h1.Fit("gaus","V","E1",34,36)
                        elif sample == "zpToMuMu_M40":
                            h1.GetXaxis().SetRangeUser(30.,50.)
                            h1.Fit("gaus","V","E1",38,42)
                        elif sample == "zpToMuMu_M45":
                            h1.GetXaxis().SetRangeUser(40.,50.)
                            h1.Fit("gaus","V","E1",40,50)
                        elif sample == "zpToMuMu_M50" or sample == "zpToMuMu_M55":
                            h1.GetXaxis().SetRangeUser(40.,60.)
                            h1.Fit("gaus","V","E1",40,70)
                        elif sample == "zpToMuMu_M60" or sample == "zpToMuMu_M65":
                            h1.GetXaxis().SetRangeUser(50.,70.)
                            h1.Fit("gaus","V","E1",50,80)
                        elif sample == "zpToMuMu_M70":
                            h1.GetXaxis().SetRangeUser(60.,80.)
                            h1.Fit("gaus","V","E1",60,90)
                        elif sample == "zpToMuMu_M75":
                            h1.GetXaxis().SetRangeUser(70.,80.)
                            h1.Fit("gaus","V","E1",70,80)
                        elif sample == "zpToMuMu_M80":
                            h1.GetXaxis().SetRangeUser(70.,90.)
                            h1.Fit("gaus","V","E1",70,90)
                        elif sample == "zpToMuMu_M85" or sample == "zpToMuMu_M90":
                            h1.GetXaxis().SetRangeUser(70.,100.)
                            h1.Fit("gaus","V","E1",70,100)
                        c1.cd()
                        h1.Draw()
                        c1.SaveAs("FitGaus_Z1_"+sample+".png")
                        
                    if p == "FitGaus_Z2":
                        h2 = h
                        if sample == "zpToMuMu_M1" or sample == "zpToMuMu_M2":
                            h2.GetXaxis().SetRangeUser(0.,10.)
                            h2.Fit("gaus","V","E1",0,5)
                        elif sample == "zpToMuMu_M3" or sample == "zpToMuMu_M4" or sample == "zpToMuMu_M5":
                            h2.GetXaxis().SetRangeUser(0.,10.)
                            h2.Fit("gaus","V","E1",0,10)
                        elif sample == "zpToMuMu_M10":
                            h2.GetXaxis().SetRangeUser(5.,15.)
                            h2.Fit("gaus","V","E1",0,20)
                        elif sample == "zpToMuMu_M15":
                            h2.GetXaxis().SetRangeUser(10.,20.)
                            h2.Fit("gaus","V","E1",5,25)
                        elif sample == "zpToMuMu_M20":
                            h2.GetXaxis().SetRangeUser(15.,25.)
                            h2.Fit("gaus","V","E1",15,25)
                        elif sample == "zpToMuMu_M25":
                            h2.GetXaxis().SetRangeUser(20.,30.)
                            h2.Fit("gaus","V","E1",15,35)
                        elif sample == "zpToMuMu_M30":
                            h2.GetXaxis().SetRangeUser(25.,35.)
                            h2.Fit("gaus","V","E1",20,40)
                        elif sample == "zpToMuMu_M35":
                            h2.GetXaxis().SetRangeUser(30.,40.)
                            h2.Fit("gaus","V","E1",30,40)
                        elif sample == "zpToMuMu_M40":
                            h2.GetXaxis().SetRangeUser(35.,45.)
                            h2.Fit("gaus","V","E1",35,45)
                        elif sample == "zpToMuMu_M45":
                            h2.GetXaxis().SetRangeUser(40.,50.)
                            h2.Fit("gaus","V","E1",44,50)
                        elif sample == "zpToMuMu_M50":
                            h2.GetXaxis().SetRangeUser(45.,55.)
                            h2.Fit("gaus","V","E1",44,55)
                        elif sample == "zpToMuMu_M55":
                            h2.GetXaxis().SetRangeUser(50.,60.)
                            h2.Fit("gaus","V","E1",50,60)
                        elif sample == "zpToMuMu_M60":
                            h2.GetXaxis().SetRangeUser(55.,65.)
                            h2.Fit("gaus","V","E1",55,65)
                        elif sample == "zpToMuMu_M65":
                            h2.GetXaxis().SetRangeUser(60.,70.)
                            h2.Fit("gaus","V","E1",60,70)
                        elif sample == "zpToMuMu_M70":
                            h2.GetXaxis().SetRangeUser(65.,75.)
                            h2.Fit("gaus","V","E1",65,75)
                        elif sample == "zpToMuMu_M75":
                            h2.GetXaxis().SetRangeUser(70.,80.)
                            h2.Fit("gaus","V","E1",70,80)
                        elif sample == "zpToMuMu_M80":
                            h2.GetXaxis().SetRangeUser(70.,90.)
                            h2.Fit("gaus","V","E1",75,85)
                        elif sample == "zpToMuMu_M85":
                            h2.GetXaxis().SetRangeUser(75.,95.)
                            h2.Fit("gaus","V","E1",80,90)
                        elif sample == "zpToMuMu_M90":
                            h2.GetXaxis().SetRangeUser(80.,100.)
                            h2.Fit("gaus","V","E1",85,95)
                        c2.cd()
                        h2.Draw()
                        #c2.SaveAs("FitGaus_Z2_"+sample+".png")
                        
        '''            
        legend =ROOT.TLegend(0.65,0.1,0.85,0.5)
        c7.cd()
        names['pEff' + str(1)].SetLineColor(1)
        legend.AddEntry(names['pEff' + str(1)],sam[0],"lep")
        names['pEff' + str(1)].Draw()
        for k in range(2,7):
            if k < 10:
                names['pEff' + str(k)].SetLineColor(k)
            else:
                names['pEff' + str(k)].SetLineColor(k+27)
            legend.AddEntry(names['pEff' + str(k)],sam[k-1],"lep")
            names['pEff' + str(k)].Draw("SAME")
        legend.Draw()
        #c7.SaveAs("Lepeff_pt_combine_2_3_5_10_15_20.png")

        c8.cd()
        names['pEff' + str(23)].SetLineColor(1)
        names['pEff' + str(23)].Draw()
        for k in range(24,29):
            if k < 32:
                names['pEff' + str(k)].SetLineColor(k-22)
            else:
                names['pEff' + str(k)].SetLineColor(k+5)
            names['pEff' + str(k)].Draw("SAME")
        legend.Draw()
        #c8.SaveAs("Lepeff_eta_combine_2_3_5_10_15_20.png")

        c9.cd()
        names['pEff' + str(45)].SetLineColor(1)
        names['pEff' + str(45)].Draw()
        for k in range(46,51):
            if k < 54:
                names['pEff' + str(k)].SetLineColor(k-44)
            else:
                names['pEff' + str(k)].SetLineColor(k-17)
            names['pEff' + str(k)].Draw("SAME")
        legend.Draw()
        #c9.SaveAs("Lepeff_dr_combine_2_3_5_10_15_20.png")
        '''

        return True
