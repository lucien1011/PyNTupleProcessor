####################################################################################################
## PURPOSE: Make plots of significance vs. ZmassRatioDifferenceCuts for a single mass point.
## SYNTAX:  python <script.py>
## NOTES:   This code must point to signal and background files with very fine binning.
##          The mass point will have an entire array of significance values, one for each 
##          massRatioCut. User should check `User's parameters' below.
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-02-13

from ROOT import *
from Config.Significance import standardSignif, standardSignifErr
from Config.Utils import copyFile, makeDirs
from Config.tdrStyle import *

import os
import subprocess
import numpy as np
import glob

#____________________________________________________________________________________________________
# Programs for User to run: 1 = run, 0 = don't run
haddFiles   = 0 # set to 1 if you rebin the background files using a plot_DarkPhoton_SR.py script
analyzeFiles= 1 
makePlot    = 1 # also make analyzeFiles = 1
PRINT       = 1
DEBUG       = 0

#____________________________________________________________________________________________________
# User's parameters. Look them over and make sure they're appropriate for your work.
massList        = [30]
massRatioCuts   = np.arange(0.,0.100,0.001) # steps of 0.1%
# Inputs
dirToRootFiles  = "/raid/raid7/rosedj1/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/2019-02-12_NoRatioCut_SignificanceTesting/"
#dirToRootFiles  = "/raid/raid7/rosedj1/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/2019-02-12_NoRatioCut_TEST3/"
signalFile      = "HToZdZd_MZD60/DataMCDistribution.root" # LATER CHANGE THIS TO HToZdZd_MZDXX
bkgFile         = "allhaddedbkgs.root"
# Outputs
haddOutFileName = "allhaddedbkgs.root" 
outputDir       = "/home/rosedj1/public_html/HToZdZd/SignificancePlots/"
plotFileName    = "SignificanceVsmassRatioCut_mZd60"
ROOT.gROOT.SetBatch(kTRUE)  # kTRUE = will NOT draw canvas

#____________________________________________________________________________________________________
# Automatic variables
haddOutPath     = dirToRootFiles+haddOutFileName
signalPath      = dirToRootFiles+signalFile
bkgPath         = dirToRootFiles+bkgFile

#____________________________________________________________________________________________________
# hadd all bkg files
if (haddFiles):

    # Delete produced hadded file if it already exists
    if os.path.exists(haddOutPath): 
        print "Removing %s" % (haddOutPath)
        os.remove(haddOutPath)
    
    # hadd bkg files
    bkgfilelist = glob.glob(dirToRootFiles + "[!H]*/DataMCDistribution.root")
    print "Hadding files..."
    subprocess.call(['hadd','%s' % haddOutPath] + bkgfilelist)
    if os.path.exists(haddOutPath): print "Successfully hadded files into %s" % haddOutFileName

#____________________________________________________________________________________________________
# Make plots
if (analyzeFiles):

    def getIntegralArr(signalFile, massRatioCuts, histo):
        '''
        This function can take in a signal file for a given Zd mass or a hadded background file.
        Returns an array of integral values 

        signalFile      = HToZdZd signal file
        massRatioCuts   = array of abs( (Z1-Z2)/(Z1+Z2) ) values
        histo           = which histogram in signalFile you want to analyze, e.g. mass_ratio_2e2mu
        '''
        signalArr   = np.array([])
        errorArr    = np.array([])
        integErr    = ROOT.Double(0)

        sigfile = TFile.Open( signalFile )
        sigmassratio = sigfile.Get( histo )
        totalbins = sigmassratio.GetNbinsX()
        if (PRINT): print "Found %i bins in file %s" % (totalbins, signalFile)

        for cut in massRatioCuts:

        # Get integral of signal for different ZmassRatio cuts:
            # The x-axis goes from 0 to 1. It is the (Z1-Z2)/(Z1+Z2) cut. This is the "ZmassRatio".
            # The larger this value, the less likely the two Zd's are the same particle.
            # Therefore the smaller the number of events we should observe.
            # If our cut is 10%, then we need the Integral from 0 to 0.1 on the x-axis.
            # Need to identify the corresponding bin at 0.1. 
            # The integral will act as "number of events" for signal or for background.

            # e.g. if you have 8 total bins, and want to cut at 25%, then the finalbin = 2
            finalbin = int( round( float(totalbins)*cut ))
            #sigInteg = sigmassratio.Integral(1,finalbin)
            sigInteg = sigmassratio.IntegralAndError(1,finalbin,integErr) # stores error in third argument
            signalArr = np.append(signalArr, sigInteg)
            errorArr = np.append(errorArr, integErr)
            if (PRINT): 
                print "Making massRatioCut of %f%%" % (cut*100.)
                print "Therefore cutting at bin: %i" % finalbin
                print "%s integral gives: %f" % (signalFile, sigInteg)
                print "error on the integral: %f" % integErr

        return signalArr, errorArr

    # Load files
    sigArr, sigErrArr = getIntegralArr(signalPath, massRatioCuts, "mass_ratio")
    bkgArr, bkgErrArr = getIntegralArr(bkgPath,    massRatioCuts, "mass_ratio")

    # x-axis doesn't have errors?
    massRatioCutsErr = np.zeros(massRatioCuts.size)

    # Calculate significance
    signifArr = standardSignif(sigArr, bkgArr)
    signifErrArr = standardSignifErr(sigArr, bkgArr, sigErrArr, bkgErrArr)
    if (PRINT): 
        print "sigArr looks like:\n",sigArr
        print "bkgArr looks like:\n",bkgArr
        print "signifArr looks like:\n",signifArr
        print "signifErrArr looks like:\n",signifErrArr

    c1 = TCanvas("c1","c1",800,800)
    c1.cd()

    tg = TGraphErrors(signifArr.size, massRatioCuts, signifArr, massRatioCutsErr, signifErrArr)
    #tg = TGraph(signifArr.size, massRatioCuts, signifArr)
    tg.Draw("ACP")
    #setTDRStyle()
    
    makeDirs(outputDir)
    copyFile("/home/rosedj1/","index.php",outputDir)
    c1.SaveAs(outputDir+plotFileName + ".pdf")
    c1.SaveAs(outputDir+plotFileName + ".png")
