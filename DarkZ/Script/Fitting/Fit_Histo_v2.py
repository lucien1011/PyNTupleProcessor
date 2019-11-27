from ROOT import *
from shutil import copyfile
import os, sys
from Core.Utils.tdrStyle import setTDRStyle

gROOT.SetBatch(kTRUE) #kTRUE = will NOT draw plots to the screen!
#setTDRStyle()

#masslist = [4,7,10,15,20,25,30]
masslist = [20]

# WARNING! "massval" gets substituted out later.
#inputfile = "/raid/raid7/rosedj1/Higgs/DarkZ/DarkPhotonSR/DataMCDistributions/20191125_RunII_fitsignalgaus/HZZd_Mmassval/DataMCDistribution.root"
inputfile = "/raid/raid7/rosedj1/Higgs/DarkZ/DarkPhotonSR/DataMCDistributions/20191127_RunII_fitsignalgaus_mX_0to40GeV/HZZd_Mmassval/DataMCDistribution.root"
out_plot_path = "/home/rosedj1/public_html/Higgs/DarkZ/DarkPhotonSR/HZZd4l_mX_gaus_fits/"

php_in_dir = "/home/rosedj1/"
if not os.path.exists(out_plot_path):
    os.mkdir(out_plot_path)
copyfile(php_in_dir+"index.php",out_plot_path+"index.php")
#out_plot_path = "/home/rosedj1/UFPyNTupleRunner/CMSSW_9_4_4/src/UF-PyNTupleRunner/DarkZ/Script/ZZd_signal_fits_gaus/"

for mass in masslist:
    mass_str = str(mass)
    infile = inputfile.replace('massval',mass_str)
    f1 = TFile.Open(infile)

    histlist = []
    histlist.append( f1.Get("mZ2_4e") )
    histlist.append( f1.Get("mZ2_2mu2e") )
    histlist.append( f1.Get("mZ2_4mu") )
    histlist.append( f1.Get("mZ2_2e2mu") )

    if mass < 10:
        mass_str = '0'+mass_str  # Make 1 -> 01, etc.

    for plot in histlist:
        plotname = str(plot.GetName()) + '_' + mass_str + 'GeV'
#        if mass < 10: 
#            x_min = 
        x_min = 0.8*mass
        x_max = 1.2*mass
        fit = TF1("fitfunc","gaus",x_min,x_max)
        fit.SetLineColor(2)
        fit.SetLineWidth(2)
        fit.SetLineStyle(2)
        plot.Fit(fit,'S')
        gStyle.SetOptFit(1111)
        c = TCanvas()
        plot.SetXTitle("m_{Z_{2}}")
        plot.SetYTitle("Events [0.2 GeV]")
        plot.SetTitle("%s" % plotname)
        plot.Draw('hist e')
        fit.Draw("same")
        #plot.Fit("gaus","","",x_min,x_max)
        c.Update()
        c.Draw()
        c.SaveAs(out_plot_path + plotname + '.pdf')
        c.SaveAs(out_plot_path + plotname + '.png')
