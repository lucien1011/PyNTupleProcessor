####################################################################################################
## PURPOSE: Make plots of significance vs. ZmassRatioDifferenceCuts for a single mass point.
## SYNTAX:  python <script.py>
## NOTES:   This code must point to signal and background files with very fine binning.
##          The mass point will have an entire array of significance values, one for each 
##          massRatioCut. User should check `User's parameters' below.
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-02-13

from ROOT import *
from Config.Significance import *
from Config.Utils import copyFile, makeDirs
from Config.tdrStyle import *

import os
import subprocess
import numpy as np
import glob

setTDRStyle()

#____________________________________________________________________________________________________
# Programs for User to run: 1 = run, 0 = don't run
HaddFiles   = 0 # set to 1 if you rebin the background files using a plot_DarkPhoton_SR.py script
AnalyzeFiles= 1 
DRAW        = 1 # must also make AnalyzeFiles = 1 to make plots
DEBUG       = 0

#____________________________________________________________________________________________________
# User's parameters. Look them over and make sure they're appropriate for your work.
#masslist        = [15]             # Zd mass points you want to run over
masslist        = [15,30,50,60]             # Zd mass points you want to run over
massratio_cuts  = np.arange(0.,0.100,0.002) # (start, stop, interval)
finalstatelist  = ["mass_ratio_4e","mass_ratio_4mu","mass_ratio_2e2mu","mass_ratio_2mu2e"]
#finalstatelist  = ["mass_ratio_2e2mu"]
signifFunclist  = ["Standard Signif.","AMS Signif."]
#signifFunclist  = ["Standard Signif.","AMS Signif.","Punzi Signif."]

# Inputs
dirToRootFiles  = "/raid/raid7/rosedj1/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/2019-02-12_NoRatioCut_SignificanceTesting/"
signalFile      = "HToZdZd_MZDMASS/DataMCDistribution.root" 
bkgFile         = "allhaddedbkgs.root"

# Outputs
haddOutFileName = "allhaddedbkgs.root" 
outputDir       = "/home/rosedj1/public_html/HToZdZd/SignificancePlots/AllKindsOfSignificance/"
plotFileName    = "SignificanceVsmassRatioCut_mZdMASS_FINALSTATE" # Generic file name format. The `MASS' will become mZd value
linecolor       = 1 # 1=kBlack
graphOptions    = "APC"
#graphOptions    = "ACPZ"
ROOT.gROOT.SetBatch(kTRUE)  # kTRUE = will NOT draw canvas

#____________________________________________________________________________________________________
# Automatic variables
haddOutPath     = dirToRootFiles+haddOutFileName
signalPath      = dirToRootFiles+signalFile
bkgPath         = dirToRootFiles+bkgFile
masslist        = [str(i) for i in masslist] # the replace method only accepts strings

#____________________________________________________________________________________________________
# hadd all bkg files
if (HaddFiles): haddFiles(haddOutpath,dirToRootFiles,haddOutFileName)

#____________________________________________________________________________________________________
# Make plots
if (AnalyzeFiles):
    for zdmass in masslist:

        tempSignalPath = dirToRootFiles + signalFile.replace("MASS",zdmass)

        for finalstate in finalstatelist:
            mg = TMultiGraph() # Multigraph allows you to draw multiple TGraphs on same canvas
            leg = TLegend(0.77,0.78,0.97,0.93)
            #leg = TLegend(0.7,0.7,0.9,0.9)
            tmplinecolor = linecolor

            # Load files
            sigArr, sigErrArr = getIntegralArr(tempSignalPath, massratio_cuts, finalstate)
            bkgArr, bkgErrArr = getIntegralArr(bkgPath,        massratio_cuts, finalstate)
            massratio_cutsErr = np.zeros(massratio_cuts.size) # x-axis doesn't have errors?

            c1 = TCanvas()

            for signifFunc in signifFunclist:

                    # make array of different TGraphs
                    #for tgraph in tgraphlist:
                    #for finalstate in finalstatelist:
                        #graph = makeTGraph(massratio_cuts, signifArr, massratio_cutsErr, signifErrArr, finalstate, zdmass)
                #sigArr, sigErrArr = getIntegralArr(signalPath, massratio_cuts, finalstate)
                #bkgArr, bkgErrArr = getIntegralArr(bkgPath,    massratio_cuts, finalstate)

                # Calculate significance
                signifArr, signifErrArr = signifdict[signifFunc](sigArr, bkgArr, sigErrArr, bkgErrArr)
                #signifArr, signifErrArr = standardSignifAndErr(sigArr, bkgArr, sigErrArr, bkgErrArr)
                if (DEBUG): 
                    print "Using significance function:",signifFunc
                    print "sigArr looks like:\n",sigArr
                    print "bkgArr looks like:\n",bkgArr
                    print "signifArr looks like:\n",signifArr
                    print "signifErrArr looks like:\n",signifErrArr

                tg = TGraphErrors(signifArr.size, massratio_cuts, signifArr, massratio_cutsErr, signifErrArr)
                #mg.AddmakeTGraph(massratio_cuts, signifArr, massratio_cutsErr, signifErrArr, finalstate, zdmass) 
                tg.SetLineColor(tmplinecolor)
                tg.SetLineWidth(2)
                mg.Add(tg)
                tmplinecolor+=1
                #tg, legentry = makeTGraph(massratio_cuts, signifArr, massratio_cutsErr, signifErrArr, finalstate, zdmass) 
                leg.AddEntry(tg,signifFunc,"lp") # l=line, p=point, f=fill
                #finalstate="ALLfinalstates" # for naming purposes
            #tg.SetLineColor(1) 
            #tg.GetXaxis().SetTitle("Mass Ratio Cut, #abs{ Z_{1}-Z_{2}/(Z_{1}+Z_{2} }")
            #tg.GetYaxis().SetTitle("Significance")
            #tg.GetYaxis().SetTitle("Significance = #frac{S}{#sqrt{B}}")
            plottitle   = "SigVsMassRatio, mZd = %s GeV, final state = %s," % (zdmass, finalstate)
            xtitle      = "Mass Ratio Cut, |(Z_{1}-Z_{2})/(Z_{1}+Z_{2})|" 
            ytitle      = "Significance"
            mg.SetTitle(plottitle +";"+ xtitle+";"+ ytitle)
            mg.Draw(graphOptions)
            leg.Draw("same")

            tempFileName = plotFileName.replace("MASS",zdmass)
            tempFileName = tempFileName.replace("FINALSTATE",finalstate)

    #            else: 
    #                tg = TGraphErrors(signifArr.size, massratio_cuts, signifArr, massratio_cutsErr, signifErrArr)
    #                #tg = TGraph(signifArr.size, massratio_cuts, signifArr)
    #                                
    #                tempFileName = plotFileName.replace("MASS",zdmass)
    #                tempFileName = tempFileName.replace("FINALSTATE",finalstate)

            makeDirs(outputDir)
            copyFile("/home/rosedj1/","index.php",outputDir)
            c1.SaveAs(outputDir+tempFileName + ".pdf")
            c1.SaveAs(outputDir+tempFileName + ".png")

