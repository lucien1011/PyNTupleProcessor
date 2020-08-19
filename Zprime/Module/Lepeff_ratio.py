from Core.EndModule import EndModule

import os,ROOT,numpy

from array import array

class Lepeff_ratio(EndModule):
    def __init__(self,outputDir):
        self.outputDir = outputDir

    def begin(self,collector):
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            #h1 = ROOT.TH2D("Lepeff"+sample, "Lepeff"+sample, 10,0.,200.,10,-2.4,2.4)
            h2 = ROOT.TH1D("Lepeff_pt"+sample, "Lepeff_pt"+sample, 10,0.,200)
            h3 = ROOT.TH1D("Lepeff_eta"+sample, "Lepeff_eta"+sample, 20,-2.5,2.5)
            h4 = ROOT.TH1D("Lepeff_dr"+sample, "Lepeff_dr"+sample, 20,0.,5)
            #h2 = ROOT.TH2D("CTageff"+sample, "CTageff"+sample, 10,0.,200.,10,-2.4,2.4)
            #h3 = ROOT.TH2D("LTageff"+sample, "LTageff"+sample, 10,0.,200.,10,-2.4,2.4)


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
        names = self.__dict__
        #hist_name = ["LepeffNum", "LepeffDem"]
        hist_name = ["LepeffNum_pt", "LepeffDem_pt", "LepeffNum_eta", "LepeffDem_eta", "LepeffNum_dr", "LepeffDem_dr", "LepacptNum", "LepacptDem", "EventeffNum", "EventeffDem", "testEventNum", "testEventDem", "MomId_GENlep", "nGENlep_vs_nRECOlep", "nGENlep_vs_nRECOlep_ZZprime"]
        pt_bins = numpy.array([5, 10, 15, 20, 30, 50, 70, 100, 140, 200], dtype='float64')
        eta_bins = numpy.array([-2.4,-1.42,0.,1.42,2.4], dtype='float64')
        histList = []
        #h4 = ROOT.TH1D("Lepeff_barrel_combine_M1", "Lepeff_barrel_combine_M1", 9,pt_bins)
        #h5 = ROOT.TH1D("Lepeff_barrel_combine_M5", "Lepeff_barrel_combine_M5", 9,pt_bins)
        #h6 = ROOT.TH1D("Lepeff_endcap_combine_M1", "Lepeff_endcap_combine_M1", 9,pt_bins)
        #h7 = ROOT.TH1D("Lepeff_endcap_combine_M5", "Lepeff_endcap_combine_M5", 9,pt_bins)
        c7 = ROOT.TCanvas("Lepeff_pt_combine")
        c8 = ROOT.TCanvas("Lepeff_eta_combine")
        c9 = ROOT.TCanvas("Lepeff_dr_combine")
        i = 0
        sam = []
        for isample,sample in enumerate(collector.mcSamples if not collector.mergeSamples else collector.mergeSamples):
            i = i + 1
            #histList = []
            sam.append(sample)
            #if not collector.mergeSamples and collector.sampleDict[sample].isSignal: continue
            #print(sample)
            #h1 = ROOT.TH2D("Lepeff"+sample, "Lepeff"+sample, 9,pt_bins,4,eta_bins)
            #h2 = ROOT.TH1D("Lepeff_barrel"+sample, "Lepeff_barrel"+sample, 9,pt_bins)
            #h3 = ROOT.TH1D("Lepeff_endcap"+sample, "Lepeff_endcap"+sample, 9,pt_bins)
            #h2 = ROOT.TH2D("CTageff"+sample, "CTageff"+sample, 9,pt_bins,4,eta_bins)
            #h3 = ROOT.TH2D("LTageff"+sample, "LTageff"+sample, 9,pt_bins,4,eta_bins)
            #c1 = ROOT.TCanvas("Lepeff"+sample)
            c2 = ROOT.TCanvas("Lepeff_pt"+sample)
            c3 = ROOT.TCanvas("Lepeff_eta"+sample)
            c4 = ROOT.TCanvas("Lepeff_dr"+sample)
            c5 = ROOT.TCanvas("Lepacpt"+sample)
            c6 = ROOT.TCanvas("Eventeff"+sample)
            ctest1 = ROOT.TCanvas("testEvent"+sample)
            ctest2 = ROOT.TCanvas("Lepeff_tightID"+sample)
            ctest3 = ROOT.TCanvas("Lepeff_ISO"+sample)
            cMomId = ROOT.TCanvas("MomId_GENlep"+sample)
            cnGENRECOlep = ROOT.TCanvas("nGENlep_vs_nRECOlep"+sample)
            cnGENRECOlepZZprime = ROOT.TCanvas("nGENlep_vs_nRECOlep_ZZprime"+sample)
            #c2 = ROOT.TCanvas("CTageff"+sample)
            #c3 = ROOT.TCanvas("LTageff"+sample)

            for p in hist_name: 
                h = collector.getObj(sample,p)
                histList.append([h,sample,p])

            #for h,s,p in histList:
                #if s == sample:
                    #if p == "LepeffNum":
                        #h1 = h
                        #h1.SetBins(9,pt_bins,4,eta_bins)
                    #if p == "LepeffDem": #and Btemp != None:
                        #h.SetBins(9,pt_bins,4,eta_bins)
                        #h1.Divide(h)
                        #c1.cd()
                        #h1.SetStats(0)
                        #h1.Draw("colz")
                        #c1.SaveAs("Lepeff"+sample+".png")
                        #h1.SaveAs("BTageff"+sample+".png")
                        #self.writer.objs["BTageff"+sample] = Btemp

            for h,s,p in histList:
                if s == sample:
                    if p == "LepeffNum_pt":
                        names['h' + str(i)] = h
                        names['h' + str(i)].SetBins(9,pt_bins)
                    if p == "LepeffDem_pt": #and Btemp != None:
                        temp = h
                        temp.SetBins(9,pt_bins)
                        names['pEff' + str(i)] = ROOT.TEfficiency(names['h' + str(i)],temp)
                        #pEff1.Write()
                        c2.cd()
                        names['pEff' + str(i)].Draw()
                        #c2.SaveAs("Lepeff_pt_"+sample+".png")

                    if p == "LepeffNum_eta":
                        names['h' + str(i+22)] = h
                        names['h' + str(i+22)].SetBins(20,-2.5,2.5)
                    if p == "LepeffDem_eta": #and Btemp != None:
                        temp = h
                        temp.SetBins(20,-2.5,2.5)
                        names['pEff' + str(i+22)] = ROOT.TEfficiency(names['h' + str(i+22)],temp)
                        #pEff2.Write()
                        c3.cd()
                        names['pEff' + str(i+22)].Draw()
                        #c3.SaveAs("Lepeff_eta_"+sample+".png")

                    if p == "LepeffNum_dr":
                        names['h' + str(i+44)] = h
                        names['h' + str(i+44)].SetBins(20,0.,5)
                    if p == "LepeffDem_dr": #and Btemp != None:
                        temp = h
                        temp.SetBins(20,0.,5)
                        names['pEff' + str(i+44)] = ROOT.TEfficiency(names['h' + str(i+44)],temp)
                        #pEff2.Write()
                        c4.cd()
                        names['pEff' + str(i+44)].Draw()
                        #c4.SaveAs("Lepeff_dr_"+sample+".png")

                    if p == "LepacptNum":
                        names['h' + str(i+66)] = h
                        names['h' + str(i+66)].SetBins(9,pt_bins)
                    if p == "LepacptDem": #and Btemp != None:
                        temp = h
                        temp.SetBins(9,pt_bins)
                        names['pEff' + str(i+66)] = ROOT.TEfficiency(names['h' + str(i+66)],temp)
                        #pEff2.Write()
                        c5.cd()
                        names['pEff' + str(i+66)].Draw()
                        #c5.SaveAs("Lepacpt_"+sample+".png")

                    if p == "EventeffNum":
                        names['h' + str(i+88)] = h
                        #names['h' + str(i+88)].SetBins(9,pt_bins)
                    if p == "EventeffDem": #and Btemp != None:
                        temp = h
                        #temp.SetBins(9,pt_bins)
                        names['pEff' + str(i+88)] = ROOT.TEfficiency(names['h' + str(i+88)],temp)
                        #pEff2.Write()
                        c6.cd()
                        names['pEff' + str(i+88)].Draw()
                        c6.SaveAs("Eventeff_"+sample+".png")

                    if p == "testEventNum":
                        names['h' + str(i+110)] = h
                    if p == "testEventDem": #and Btemp != None:
                        temp = h
                        names['pEff' + str(i+110)] = ROOT.TEfficiency(names['h' + str(i+110)],temp)
                        ctest1.cd()
                        names['pEff' + str(i+110)].Draw()
                        #ctest1.SaveAs("testEvent_"+sample+".png")

                    if p == "MomId_GENlep":
                        cMomId.cd()
                        h.Draw()
                        #cMomId.SaveAs("MomId_GENlep_"+sample+".png")

                    if p == "nGENlep_vs_nRECOlep":
                        cnGENRECOlep.cd()
                        h.DrawNormalized().Draw("COLZ TEXT")
                        cnGENRECOlep.SaveAs("nGENlep_vs_nRECOlep"+sample+".png")

                    if p == "nGENlep_vs_nRECOlep_ZZprime":
                        cnGENRECOlepZZprime.cd()
                        h.DrawNormalized().Draw("COLZ TEXT")
                        cnGENRECOlepZZprime.SaveAs("nGENlep_vs_nRECOlep_ZZprime"+sample+".png")

            '''
            for h,s,p in histList:
                if s == "zpToMuMu_M1" and p == "LepeffNum_barrel":
                    h4 = h
                    h4.SetBins(9,pt_bins)
                if s == "zpToMuMu_M1" and p == "LepeffDem_barrel":
                    h5 = h
                    h5.SetBins(9,pt_bins)
                if s == "zpToMuMu_M90" and p == "LepeffNum_barrel":
                    h6 = h
                    h6.SetBins(9,pt_bins)
                if s == "zpToMuMu_M90" and p == "LepeffDem_barrel":
                    h7 = h
                    h7.SetBins(9,pt_bins)

                if s == "zpToMuMu_M1" and p == "LepeffNum_endcap":
                    h8 = h
                    h8.SetBins(9,pt_bins)
                if s == "zpToMuMu_M1" and p == "LepeffDem_endcap":
                    h9 = h
                    h9.SetBins(9,pt_bins)
                if s == "zpToMuMu_M90" and p == "LepeffNum_endcap":
                    h10 = h
                    h10.SetBins(9,pt_bins)
                if s == "zpToMuMu_M90" and p == "LepeffDem_endcap":
                    h11 = h
                    h11.SetBins(9,pt_bins)
                    '''
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
        '''
        legend = ROOT.TLegend(0.65,0.1,0.85,0.3)

        pEff3 = ROOT.TEfficiency(h4,h5)
        #pEff3.Write()
        pEff4 = ROOT.TEfficiency(h6,h7)
        #pEff4.Write()
        c4.cd()
        pEff3.SetLineColor(4)
        pEff4.SetLineColor(2)
        pEff3.Draw()
        pEff4.Draw("SAME")
        legend.AddEntry(pEff3,"zpToMuMu_M1","lep")
        legend.AddEntry(pEff4,"zpToMuMu_M90","lep")
        legend.Draw()
        c4.SaveAs("Lepeff_barrel_combine_M4M5_BlueRed.png")
        pEff5 = ROOT.TEfficiency(h8,h9)
        #pEff5.Write()
        pEff6 = ROOT.TEfficiency(h10,h11)
        #pEff6.Write()
        c5.cd()
        pEff5.SetLineColor(4)
        pEff6.SetLineColor(2)
        pEff5.Draw()
        pEff6.Draw("SAME")
        legend.Draw()
        c5.SaveAs("Lepeff_endcap_combine_M1M90_BlueRed.png")
        '''
        #h = collector.getObj("AllSample","LepeffNum")
        #h1 = h
        #h1.SetBins(1,5.,200.,1,-2.4,2.4)
        #h1.SetBins(9,pt_bins,4,eta_bins)
        #h1.SaveAs("AllSample.png")
        #h = collector.getObj("AllSample","LepeffDem")
        #h.SetBins(1,5.,200.,1,-2.4,2.4)
        #h.SetBins(9,pt_bins,4,eta_bins)
        #h1.Divide(h)
        #c1.cd()
        #h1.SetStats(0)
        #h1.Draw("colz")
        #c1.SaveAs("LepeffAllSample.png")

        h = collector.getObj("AllSample","LepeffNum_pt")
        h2 = h
        h2.SetBins(9,pt_bins)
        h = collector.getObj("AllSample","LepeffDem_pt")
        h.SetBins(9,pt_bins)
        pEff1 = ROOT.TEfficiency(h2,h)
        c2.cd()
        pEff1.Draw()
        #c2.SaveAs("LepeffAllSample_pt.png")

        h = collector.getObj("AllSample","LepeffNum_eta")
        h3 = h
        h3.SetBins(20,-2.5,2.5)
        h = collector.getObj("AllSample","LepeffDem_eta")
        h.SetBins(20,-2.5,2.5)
        pEff2 = ROOT.TEfficiency(h3,h)
        c3.cd()
        pEff2.Draw()
        #c3.SaveAs("LepeffAllSample_eta.png")
        
        h = collector.getObj("AllSample","LepeffNum_dr")
        h4 = h
        h4.SetBins(20,0.,5)
        h = collector.getObj("AllSample","LepeffDem_dr")
        h.SetBins(20,0.,5)
        pEff3 = ROOT.TEfficiency(h4,h)
        c4.cd()
        pEff3.Draw()
        #c4.SaveAs("LepeffAllSample_dr.png")

        return True
