import os, sys
import ROOT
from ROOT import TH1F,TFile,TTree,TCanvas, TProfile, TNtuple, gErrorIgnoreLevel, kInfo, kWarning, TLegend, TLine
from tqdm import tqdm
tqdm_disable = False
ROOT.gErrorIgnoreLevel = kWarning;

F1 = TFile("results_FromZp/WpTo3l_ZpM60/WpTo3l_ZpM60_0_DataMCDistribution.root")
F2 = TFile("results_notFromZp/WpTo3l_ZpM60/WpTo3l_ZpM60_0_DataMCDistribution.root")

hists_1 = [F1.Get("Lep1_pt"),F1.Get("Lep1_eta"),F1.Get("Lep1_phi"),
	   F1.Get("Lep2_pt"),F1.Get("Lep2_eta"),F1.Get("Lep2_phi"),
	   F1.Get("Lep3_pt"),F1.Get("Lep3_eta"),F1.Get("Lep3_phi"),]
	   #F1.Get("dRLep1Lep2"),F1.Get("dRLep1Lep3"),F1.Get("dRLep2Lep3")]
hists_2 = [F2.Get("Lep1_pt"),F2.Get("Lep1_eta"),F2.Get("Lep1_phi"),
	   F2.Get("Lep2_pt"),F2.Get("Lep2_eta"),F2.Get("Lep2_phi"),
           F2.Get("Lep3_pt"),F2.Get("Lep3_eta"),F2.Get("Lep3_phi"),]
	   #F2.Get("dRLep1Lep2"),F2.Get("dRLep1Lep3"),F2.Get("dRLep2Lep3")]

c1 = TCanvas("c1","c1",900,700);
c1.SetRightMargin(0.09);
c1.SetLeftMargin(0.15);
c1.SetBottomMargin(0.15);

line = TLine(0,0,0,0)

legend = TLegend(0.7,0.65,1,.75);
legend.AddEntry(hists_1[0],"From Zp","lep");
legend.AddEntry(hists_2[0],"Not From Zp","lep");
#legend.AddEntry("line","Threshold","lep");
legend.Draw();

c1.Print("results/Comparison_Plots.pdf[")

for i in range(0,len(hists_1)):
    hists_1[i].SetLineColor(ROOT.kBlue)
    hists_2[i].SetLineColor(ROOT.kRed)
    
    hists_1[i].Scale(hists_2[i].Integral()/hists_1[i].Integral())

    hists_1[i].Draw()
    hists_2[i].Draw("SAME")
    
    #ROOT.gPad.SetLogy();
    c1.Update()
    
    #line = TLine(thresholds[i], c1.GetUymin(), thresholds[i], c1.GetUymax()*100000)
    #line.SetLineColor(ROOT.kBlack)
    #line.Draw("SAME")
    
    legend.Draw()
    
    c1.Print("results/Comparison_Plots.pdf");
    
c1.Print("results/Comparison_Plots.pdf]")

