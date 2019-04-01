import numpy as np
import os
import glob
import subprocess

from ROOT import *

#____________________________________________________________________________________________________
# Significance defintions
def standardSignifAndErr(S, B, Serr, Berr):
    Signif = S/np.sqrt(B)
    SignifERR = np.sqrt(  1/B*(Serr**2) + (1/4)*(S**2)/(B**3)*(Berr**2)  )

    return Signif, SignifERR

def sclSignifAndErr(S, B, Serr, Berr):
    pass
    #return Signif, SignifERR

def punziSignifAndErr(S, B, Serr, Berr): 
    a=2
    b=5
    eff = S/(S+B)
    Smin = a*a/8 + 9*b*b/13 + a*np.sqrt(B) + b/2*np.sqrt( b*b+4*a*np.sqrt(B)+4*B )
    Signif = Smin/eff
    SignifErr = Signif*0.05
    return Signif, SignifErr
    

def amsSignifAndErr(S, B, Serr, Berr):
    '''
    Andrey knows this as S_cL significance!
    '''
    lnrat = np.log(1+S/B)
    Signif = np.sqrt(2*( (S+B)*lnrat - S  ))

    errwrtS = 1/Signif * lnrat
    errwrtB = errwrtS - (S/B) / Signif
    SignifErr = np.sqrt( (errwrtS*Serr)**2 + (errwrtB*Berr)**2  )
    return Signif, SignifErr

#____________________________________________________________________________________________________
# Other Functions
def getIntegralArr(signalFile, histo, massratio_cuts=range(1,2), dim=1, DEBUG=0):
    '''
    This function can take in a signal file for a given Zd mass or a hadded background file.
    Returns an array of integral values 

    signalFile      = full file path to HToZdZd signal file or hadded bkg file
    massratio_cuts  = array of abs( (Z1-Z2)/(Z1+Z2) ) values
    histo           = which histogram in signalFile you want to analyze, e.g. mass_ratio_2e2mu
    '''
    signalArr   = np.array([])
    errorArr    = np.array([])
    integErr    = Double(0)

    sigfile = TFile.Open(signalFile)
    if (DEBUG): print "sigfile is: ", sigfile
    sigmassratio = sigfile.Get(histo)
    if (DEBUG): print "sig histo is: ", sigmassratio
    totalbinsX = sigmassratio.GetNbinsX()
    if (DEBUG): print "total binsX in this histo: ", totalbinsX
    if dim==2: 
        totalbinsY = sigmassratio.GetNbinsY() 
        if (DEBUG): print "total binsY in this histo: ", totalbinsY
    #if (DEBUG): print "Found %i bins in file %s" % (totalbinsX, signalFile)

    for cut in massratio_cuts:

    # Get integral of signal for different ZmassRatio cuts:
        # The x-axis goes from 0 to 1. It is the (Z1-Z2)/(Z1+Z2) cut. This is the "ZmassRatio".
        # The larger this value, the less likely the two Zd's are the same particle.
        # Therefore the smaller the number of events we should observe.
        # If our cut is 10%, then we need the Integral from 0 to 0.1 on the x-axis.
        # Need to identify the corresponding bin at 0.1. 
        # The integral will act as "number of events" for signal or for background.

        # e.g. if you have 8 total bins, and want to cut at 25%, then the finalbin = 2
        finalbin = int( round( float(totalbinsX)*cut ))
        #sigInteg = sigmassratio.Integral(1,finalbin)
        if dim==1:
            sigInteg = sigmassratio.IntegralAndError(1,finalbin,integErr) # stores error in third argument
        if dim==2:
            sigInteg = sigmassratio.IntegralAndError(1,finalbin,1,finalbin,integErr) # stores error in third argument
        signalArr = np.append(signalArr, sigInteg)
        errorArr = np.append(errorArr, integErr)
        if (DEBUG): 
            print "Making massRatioCut of %f%%" % (cut*100.)
            print "Therefore cutting at bin: %i" % finalbin
            print "%s \nintegral gives: %f" % (signalFile, sigInteg)
            print "error on the integral: %f" % integErr, "\n"

    return signalArr, errorArr

##############################
# I don't think this is used anymore...
#def makeTGraph( massratio_cuts, signifArr, massratio_cutsErr, signifErrArr, finalstate, zdmass):
#    tg = TGraphErrors(signifArr.size, massratio_cuts, signifArr, massratio_cutsErr, signifErrArr)
#    #tg.Draw("ACPZ") # Z=no caps on error bars
#    #tg.Draw("ACP3Z")
#    
#    leg.AddEntry(tg,finalstate,"lpf")
#    return tg, leg

#def haddFiles(haddOutPath,dirToRootFiles,haddOutFileName,bkgFileGlobName):
#    # Delete produced hadded file if it already exists
#    if os.path.exists(haddOutPath): 
#        print "Removing %s" % (haddOutPath)
#        os.remove(haddOutPath)
#    
#    # hadd bkg files
#    bkgfilelist = glob.glob(dirToRootFiles + bkgFileGlobName)
#    print "Hadding files..."
#    subprocess.call(['hadd','%s' % haddOutPath] + bkgfilelist)
#    if os.path.exists(haddOutPath): print "Successfully hadded files into %s" % haddOutFileName
##############################

def haddFiles(haddOutPath,dirToRootFiles,haddOutFileName,bkgFileGlobName,Overwrite=False):
    # Delete files if User says to Overwrite
    if Overwrite: 
        print "Removing %s" % (haddOutPath)
        os.remove(haddOutPath)

    # Delete produced hadded file if it already exists
    #if os.path.exists(haddOutPath): 
    #    print "Removing %s" % (haddOutPath)
    #    os.remove(haddOutPath)
    
    # hadd bkg files
    bkgfilelist = glob.glob(dirToRootFiles + bkgFileGlobName)
    print "Hadding files..."
    subprocess.call(['hadd','-f','%s' % haddOutPath] + bkgfilelist)
    if os.path.exists(haddOutPath): print "Successfully hadded files into %s" % haddOutFileName

def setInfinAndNANToZero(arr):
    '''
    Set all "inf" and "nan" values of an array (arr) to zero.
    '''
    arr[ abs(arr)==np.inf] = 0
    np.nan_to_num(arr)
    #return arr ### You don't even need to return the array!
#____________________________________________________________________________________________________
# Dictionary to collect significance functions
signifdict = {
        "Standard Signif.":standardSignifAndErr,
        "S_cL Signif.":sclSignifAndErr,
        "Punzi Signif.":punziSignifAndErr,
        "AMS Signif.":amsSignifAndErr,
        }

