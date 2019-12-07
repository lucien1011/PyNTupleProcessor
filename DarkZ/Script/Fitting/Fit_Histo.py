#!/usr/bin/ python2
#------------------------------------------------------------------------------
# PURPOSE: 
# SYNTAX:  
# NOTES:   
# AUTHOR:  
# DATE:    
# UPDATED: 
#------------------------------------------------------------------------------
from ROOT import *
from shutil import copyfile
import os, sys
from Core.Utils.tdrStyle import setTDRStyle
from DarkZ.Script.Fitting.Mass_Collection_cls import HistCollection
import numpy as np
#------------------------------------------------------------------------------
# USER INPUT
gROOT.SetBatch(kTRUE) #kTRUE = will NOT draw plots to the screen!
#setTDRStyle()

mass_list = [4,7,15,20,25,30]
fs_list = ["4e","4mu","2e2mu","2mu2e"]
#mass_list = [4,20,30]
#fs_list = ["4e","4mu"]
make_rel_resolution_plot = 1
graph_title = "Relative_Resolution_vs_mZ2"

# NOTES "__massval__" gets substituted out later.
#infile_template = "/raid/raid7/rosedj1/Higgs/DarkZ/DarkPhotonSR/DataMCDistributions/20191125_RunII_fitsignalgaus/HZZd_Mmassval/DataMCDistribution.root"
infile_template = "/raid/raid7/rosedj1/Higgs/DarkZ/DarkPhotonSR/DataMCDistributions/20191127_RunII_fitsignalgaus_mX_0to40GeV/HZZd_M__massval__/DataMCDistribution.root"
outpath_plots = "/home/rosedj1/public_html/Higgs/DarkZ/DarkPhotonSR/HZZd4l_mX_gaus_fits_officialsamples/"
#outpath_plots = "/home/rosedj1/UFPyNTupleRunner/CMSSW_9_4_4/src/UF-PyNTupleRunner/DarkZ/Script/ZZd_signal_fits_gaus/"
indir_phpfile = "/home/rosedj1/"

#------------------------------------------------------------------------------
# AUTOMATONS
if not os.path.exists(outpath_plots):
    os.mkdir(outpath_plots)
copyfile(indir_phpfile+"index.php",outpath_plots+"index.php")

#hcoll_4e = HistCollection()
#hcoll_4mu = HistCollection()
#hcoll_2e2mu = HistCollection()
#hcoll_2mu2e = HistCollection()
#histlist = [hcoll_4e, hcoll_4mu, hcoll_2e2mu, hcoll_2mu2e]

#list_of_collections = []
#for fs in fs_list:
#    list_of_collections.append()
list_of_collections = [HistCollection(fs) for fs in fs_list]

for hcoll in list_of_collections:
    hcoll.mass_list = mass_list
#    f1.Get("mZ2_4e"),
#    f1.Get("mZ2_2mu2e"),
#    f1.Get("mZ2_4mu"),
#    f1.Get("mZ2_2e2mu"),

for mass in mass_list:
    # For a given file, collect all the histograms.
    mass_str = str(mass)
    infile = infile_template.replace('__massval__',mass_str)
    f1 = TFile.Open(infile)

    # Make list of histos.
    for hcoll in list_of_collections:
        hist = f1.Get("mZ2_"+hcoll.fs)
        hcoll.hist_list.append(hist)

        if mass < 10:
            mass_label = '0'+mass_str  # Make 1 -> 01, etc.

#        for plot in histlist:
        hist_title = str(hist.GetName()) + '_' + mass_label + 'GeV'
        x_min = 0.8*mass
        x_max = 1.2*mass
        fit = TF1("fitfunc","gaus",x_min,x_max)
        fit.SetLineColor(2)
        fit.SetLineWidth(2)
        fit.SetLineStyle(2)

        params = hist.Fit(fit,'S')
        const = params.Parameter(0) 
        mean = params.Parameter(1) 
        sigma = params.Parameter(2) 
        const_err = params.ParError(0)
        mean_err = params.ParError(1)
        sigma_err = params.ParError(2)

        hcoll.const_list.append(const)
        hcoll.mean_list.append(mean)
        hcoll.sigma_list.append(sigma)
        hcoll.const_err_list.append(const_err)
        hcoll.mean_err_list.append(mean_err)
        hcoll.sigma_err_list.append(sigma_err)
        hcoll.rel_sigma_list.append(sigma/float(mass))
        hcoll.rel_sigma_err_list.append(sigma_err/float(mass))

        gStyle.SetOptFit(1111)
        c = TCanvas()
#        hist.SetXTitle("m_{Z2} [GeV]")
        hist.SetXTitle("m_{X} [GeV]")
        hist.SetYTitle("Events / [0.2 GeV]")
        if hist.GetName() in ["mZ2_4e","mZ2_2mu2e"]:
#            hist.SetTitle("Z_{d} #rightarrow e^{-}e^{+}")
            hist.SetTitle("X #rightarrow e^{-}e^{+}")
        else:
#            hist.SetTitle("Z_{d} #rightarrow #mu^{-}#mu^{+}")
            hist.SetTitle("X #rightarrow #mu^{-}#mu^{+}")
        
        hist.Draw('hist e1')
        fit.Draw("same")
        #plot.Fit("gaus","","",x_min,x_max)
        c.Update()
        c.Draw()
        c.SaveAs(outpath_plots + hist_title + '.pdf')
        c.SaveAs(outpath_plots + hist_title + '.png')
        
#-------------------------------------#
#----- Make rel. resolution plot -----#
#-------------------------------------#
#if (make_rel_resolution_plot):
n_pts = len(mass_list)
c1 = TCanvas()
c1.Draw()
#leg = TLegend(0.60,0.70,0.90,0.90)
leg = TLegend()

count = 1
graph_list = []
y_max_list = [max(hcoll.rel_sigma_list) for hcoll in list_of_collections]
y_max = max(y_max_list)
y_min = 0.0

for hcoll in list_of_collections:
    masses = np.array(hcoll.mass_list,dtype=float)
    rel_sigmas = np.array(hcoll.rel_sigma_list,dtype=float)
    rel_sigma_errs = np.array(hcoll.sigma_err_list,dtype=float)

    graph_list.append( TGraphErrors(n_pts, masses, rel_sigmas, np.zeros(n_pts), rel_sigma_errs) )
#    graph = TGraphErrors(n_pts, masses, rel_sigmas, np.zeros(n_pts), rel_sigma_errs)
#    graph.SetLineColor(count)
    graph_list[-1].SetMarkerStyle(count+19)  # 20=circle, 21=square, 22=tri, 23=upside down tri
    graph_list[-1].SetMarkerColor(count)
    graph_list[-1].SetMinimum(y_min)
    graph_list[-1].SetMaximum(y_max)
    graph_list[-1].SetTitle("Relative Resolution: X #rightarrow ll")
    graph_list[-1].GetXaxis().SetTitle("m_{X} [GeV]")
    graph_list[-1].GetYaxis().SetTitle("#sigma_{X}/m_{X}")
#    if 
#    graph.Draw("apl") if count == 1 else graph.Draw('pl same')
    graph_list[-1].Draw("apl") if count == 1 else graph_list[-1].Draw('pl same')
    X_fs = hcoll.X2_fs
    net_fs = hcoll.fs
    leg.AddEntry(graph_list[-1], "X #rightarrow %s (fs = %s)" % (X_fs,net_fs), "lpe")
    c1.Update()
#    c1.Draw()
    count += 1
leg.Draw("same")

#y_min = min(rel_sigmas*0.8)  # 1.2 just to catch the error bars.
#y_max = max(rel_sigmas*1.2)  # 1.2 just to catch the error bars.
#graph_list[-1].GetYaxis().SetLimits(y_min,y_max)
#c1.Update()

c1.SaveAs(outpath_plots + graph_title + ".pdf")
c1.SaveAs(outpath_plots + graph_title + ".png")

#        with open(outfile_params, "w") as f:
#            f.write(mass+'\t'+rel_sigma+'\n')
