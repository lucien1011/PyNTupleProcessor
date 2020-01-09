from ROOT import TFile,TTree,TH1D,TCanvas,TGraphErrors,TF1,TLegend,gROOT,kTRUE,gStyle,gPad,TH1Editor,TF1Convolution
import os, sys, shutil
import numpy as np
import numpy

#from Core.Utils.tdrStyle import setTDRStyle
from DarkZ.Script.Fitting.Mass_Collection_cls import HistCollection
from DarkZ.Script.Fitting.Cls_MyHist import MyHist
from DarkZ.Script.Fitting.Functions_Navigation import make_dir_copy_file
from DarkZ.Script.Fitting.Fns_Math import lorentzian

# %%capture
# %config InlineBackend.figure_format ='retina'

#-----------------------#
#----- Config File -----#
#-----------------------#
# mass_list = [1,2,3,4,7,15,20,25,30,35]   # Official HZZd samples
mass_list = [7]
# year_list = ["2016","2017","2018"]
year = "2017"
fs_list = ["4e","2e2mu"]
# fs_list = ["4e","4mu","2e2mu","2mu2e"]
n_stdev_list = [x/4. for x in range(1,9)]  # Make whole range of n_stdev for fitting.
# n_stdev_list = [x/4. for x in range(1,21)]  # Make whole range of n_stdev for fitting.

combine_bins = 1  # Merge this number of bins together. E.g., '2' merges every two bins into one bin.
fit_around_center = "mpv"  # Choose either "mean" or "mpv" (most-probably value).

print_info = True
save_fit_plots = True
save_mass_res_plot = False

# NOTES "__massval__" gets substituted out later.
infile_template = "/raid/raid7/rosedj1/Higgs/DarkZ/DarkPhotonSR/DataMCDistributions/HToZZd_Run%s_mXtoll_gausfit/HZZd_M__massval__/DataMCDistribution.root"%year
outpath_plots = "/home/rosedj1/public_html/Higgs/DarkZ/DarkPhotonSR/HZZd4l_mXtoll_gausfit_officialsamples_noLowmassX2cut_fitaroundmean/"
fullpath_phpfile = "/home/rosedj1/index.php"

#----------------------------#
#----- Histo Collection -----#
#----------------------------#
# Make collection of histograms, one for each final state.
list_of_collections = [HistCollection(fs) for fs in fs_list]

for hcoll in list_of_collections:
    hcoll.mass_list = mass_list

for mass in mass_list:
    # For a given file, collect all the histograms.
    mass_str = str(mass)
    infile = infile_template.replace('__massval__',mass_str)
    print "Opening file:\n", infile, "\n"
    f1 = TFile.Open(infile)

    # Make list of histos.
    for hcoll in list_of_collections:
        print "5 is good"

        myhist = MyHist(hcoll.fs, mass, year)
        print "6 is good"
#         print myhist
        # Open and load real histogram.
        myhist.hist = f1.Get("mZ2_" + hcoll.fs)
#         h_ls, f_ls, c_ls, nstd_ls = myhist.fit_with_gaus(n_stdev_list, draw=False, fit_around_center=fit_around_center,rebin=combine_bins)
        myhist.fit_with_gaus(
            n_stdev_list, 
            draw=False, 
            fit_around_center=fit_around_center, 
            combine_bins=combine_bins)
        print "You pass!"
        myhist.print_fit_info(print_info)
#         myhist.save_plots(fullpath_phpfile,outpath_plots,save_plots=save_fit_plots)
        myhist.get_best_fit_sigma(verbose=print_info)  # Must get_best_fit_sigma to make mass_res_plot.

#-------------------------------------#
#----- Make rel. resolution plot -----#
#-------------------------------------#
n_pts = len(mass_list)
c1 = TCanvas()
c1.Draw()
leg = TLegend(0.60,0.70,0.90,0.90)

count = 1
graph_list = []

# y_max_list = [max(hcoll.rel_sigma_list) for hcoll in list_of_collections]
# y_max = max(y_max_list)
# y_min = 0.0
print "Masses:",hcoll.mass_list

for hcoll in list_of_collections:
    rel_sigma_list = [h.best_fit_rel_sigma for h in hcoll.hist_list]
    rel_sigma_err_list = [h.best_fit_rel_sigma_err for h in hcoll.hist_list]
    print "Best relative sigmas of final state",hcoll.fs,":"
    print rel_sigma_list,"\n"
    print "Best relative sigmas errors:"
    print rel_sigma_err_list

    masses = np.array(hcoll.mass_list, dtype=float)
    rel_sigmas = np.array(rel_sigma_list, dtype=float)
    rel_sigma_errs = np.array(rel_sigma_err_list, dtype=float)

    x_min = min(masses)-3  # To see a little bit more. 
    x_max = max(masses)+3  
    y_min = 0
    y_max = 0.12
#     y_max = max(rel_sigmas)*1.2

    graph_list.append( TGraphErrors(n_pts, masses, rel_sigmas, np.zeros(n_pts), rel_sigma_errs) )
#    graph = TGraphErrors(n_pts, masses, rel_sigmas, np.zeros(n_pts), rel_sigma_errs)
#    graph.SetLineColor(count)
    graph_list[-1].SetMarkerStyle(count+19)  # 20=circle, 21=square, 22=tri, 23=upside down tri
    graph_list[-1].SetMarkerColor(count)

#     gr->Draw("AC*");
# gr->GetXaxis()->SetRangeUser(0.2,0.4);
# gr->Draw("AC*");
# c1->Update();

#     graph_list[-1].SetMinimum(y_min)
#     graph_list[-1].SetMaximum(y_max)
    graph_list[-1].SetTitle("%s MC, Relative Mass Resolution for X#rightarrowll" % year) 
    graph_list[-1].GetXaxis().SetTitle("m_{X} [GeV]")
    graph_list[-1].GetYaxis().SetTitle("#sigma_{X}/m_{X}")
    graph_list[-1].GetXaxis().SetRangeUser(x_min,x_max)
    graph_list[-1].GetYaxis().SetRangeUser(y_min,y_max)
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

if (save_mass_res_plot):
    make_dir_copy_file(fullpath_phpfile,outpath_plots)
    graph_title = "MC_OfficialSamples_Relative_Mass_Resolution_vs_mZ2_"
    c1.SaveAs(outpath_plots + graph_title + year + ".pdf")
    c1.SaveAs(outpath_plots + graph_title + year + ".png")

#        with open(outfile_params, "w") as f:
#            f.write(mass+'\t'+rel_sigma+'\n')
