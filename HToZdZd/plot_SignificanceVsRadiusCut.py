#####################################################################################################
## PURPOSE: Make plots of significance vs. RadiusCuts for a single mass point.
## SYNTAX:  python <script.py>
## NOTES:   This code must point to signal and background files with very fine binning.
##          The mass point will have an entire array of significance values, one for each 
##
##
##          massRatioCut. User should check `User's parameters' below.
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-02-13
#####################################################################################################

import os
import numpy as np

from ROOT import *
from Config.Significance import *
from Config.Utils import copyFile, makeDirs
from Config.tdrStyle import *

setTDRStyle()

#____________________________________________________________________________________________________
# Programs for User to run: 1 = run, 0 = don't run
HaddFiles   = 1 # set to 1 if you rebin the background files using a plot_DarkPhoton_SR.py script
AnalyzeFiles= 1 
DRAW        = 1 # must also make AnalyzeFiles = 1 to make plots
DEBUG       = 0

#____________________________________________________________________________________________________
# User's parameters. Look them over and make sure they're appropriate for your work.
masslist         = [15]    # Zd mass points you want to run over
#masslist         = [15,30,50,60]    # Zd mass points you want to run over
finalstatelist    = ["4e","4mu","2e2mu","2mu2e"]
signifFunclist    = ["Standard Signif.","AMS Signif."] # keys to a dictionary of significance functions
start,stop,interv = 0.2, 5.0, 0.2   # radius cut [GeV]: start, stop, interval
binwid            = 0.05            # in GeV

# Inputs
dirToRootFiles    = "/raid/raid7/rosedj1/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/RadiusCuts/"
signalFile        = "SignifRadiusCut_mZdMASS/HToZdZd_MZDMASS/DataMCDistribution_radiuscutRADCUTGeV.root" 
bkgFile           = "allhaddedbkgs_RADCUTGeV.root"
bkgFileGlobName   = "SignifRadiusCut_mZdMASS/[!H]*/DataMCDistribution*RADCUT*.root"
histotemplate     = "Z1mass_vs_Z2mass_mZdMASS_fsFINALSTATE_rcutRADCUTGeV_binwidBINWIDGeV" # histo in root file

# Outputs
haddOutFileName   = "SignifRadiusCut_mZdMASS/"+bkgFile 
outputDir         = "/home/rosedj1/public_html/HToZdZd/SignificancePlots/AllKindsOfSignificance/RadiusCutsTEST/"
plotFileName      = "SignificanceVsRadiusCut_mZdMASS_FINALSTATE" # Generic file name format. The `MASS' will become mZd value
linecolor         = 1 # 1=kBlack
graphOptions      = "APC"

#____________________________________________________________________________________________________
# Automatic variables
radius_cuts     = np.arange(start, stop*1.01, interv) # stop is exclusive; make sure to include stop value
bkgPath         = dirToRootFiles+haddOutFileName
signalPath      = dirToRootFiles+signalFile
#bkgPath         = dirToRootFiles+bkgFile
massliststr     = [str(i) for i in masslist] # the replace method only accepts strings
binwidstr       = str(binwid).replace('.','p')
maxradcutstr    = str(radius_cuts[-1])[:3].replace('.','p')
ROOT.gROOT.SetBatch(kTRUE)  # kTRUE = will NOT draw canvas
print "\n\n"    # for readability

#____________________________________________________________________________________________________
# hadd all bkg files
# If User requests to hadd files, hadd them by force
if ( HaddFiles ): 

    for zdmass in massliststr:
        for radcut in radius_cuts:

            radcutstr = str(radcut)[:3].replace('.','p')
            tempHaddOutName = haddOutFileName.replace('MASS',zdmass).replace('RADCUT',radcutstr)
            tempHaddOutPath = dirToRootFiles+tempHaddOutName
            tempGlobName = bkgFileGlobName.replace('MASS',zdmass).replace('RADCUT',radcutstr)
            haddFiles(tempHaddOutPath,dirToRootFiles,tempHaddOutName,tempGlobName,Overwrite=HaddFiles)
#____________________________________________________________________________________________________
# Make plots
if (AnalyzeFiles):
    for zdmass in massliststr:

        #tempSigPath = signalPath.replace("MASS",zdmass)
        #tempBkgPath = bkgPath.replace("MASS",zdmass)

        for finalstate in finalstatelist:
            sigArr,sigErrArr,bkgArr,bkgErrArr = np.array([]),np.array([]),np.array([]),np.array([])

            ## Prepare signal array
            for radcut in radius_cuts:
                radcutstr = str(radcut)[:3].replace('.','p')

                ## If hadded bkg file doesn't exist, create it
                import os
                if not (os.path.exists( bkgPath.replace('MASS',zdmass).replace('RADCUT',radcutstr) )):
                    tempHaddOutName = haddOutFileName.replace('MASS',zdmass).replace('RADCUT',radcutstr)
                    tempHaddOutPath = dirToRootFiles+tempHaddOutName
                    tempGlobName = bkgFileGlobName.replace('MASS',zdmass).replace('RADCUT',radcutstr)
                    haddFiles(tempHaddOutPath,dirToRootFiles,tempHaddOutName,tempGlobName,Overwrite=HaddFiles)

                #if (HaddFiles): 
                #    tempGlobName = bkgFileGlobName.replace('MASS',zdmass).replace('RADCUT',radcutstr)
                #    haddFiles(haddOutFileName,dirToRootFiles,haddOutFileName,tempGlobName)
                #    #haddFiles(bkgPath+'_'+radcutstr,dirToRootFiles,haddOutFileName,tempGlobName)
                
                ## Prepare naming of files
                tempSigPath = signalPath.replace("MASS",zdmass).replace('RADCUT',radcutstr)
                tempBkgPath = bkgPath.replace("MASS",zdmass).replace('RADCUT',radcutstr)
                #tempBkgPath = tempBkgPath.replace('RADCUT',radcutstr)
                temphisto = histotemplate.replace('MASS',zdmass).replace('FINALSTATE',finalstate).replace('RADCUT',radcutstr).replace('BINWID',binwidstr)
                if (DEBUG): print "Looking into histo: ", temphisto

                ## Will actually just grab a single value! i.e. array will have just one entry
                sigval, sigErrval = getIntegralArr(tempSigPath, temphisto, dim=2, DEBUG=DEBUG)
                bkgval, bkgErrval = getIntegralArr(tempBkgPath, temphisto, dim=2, DEBUG=DEBUG)

                sigArr = np.append(sigArr,sigval)
                sigErrArr = np.append(sigErrArr,sigErrval)
                bkgArr = np.append(bkgArr,bkgval)
                bkgErrArr = np.append(bkgErrArr,bkgErrval)

                setInfinAndNANToZero(sigArr)
                setInfinAndNANToZero(sigErrArr)
                setInfinAndNANToZero(bkgArr)
                setInfinAndNANToZero(bkgErrArr)

            mg = TMultiGraph() # Multigraph allows you to draw multiple TGraphs on same canvas
            leg = TLegend(0.77,0.78,0.97,0.93)
            #leg = TLegend(0.7,0.7,0.9,0.9)
            tmplinecolor = linecolor

            # Load files
            #sigArr, sigErrArr = getIntegralArr(tempSigPath, massratio_cuts, finalstate)
            #bkgArr, bkgErrArr = getIntegralArr(bkgPath, massratio_cuts, finalstate)
            radius_cutsErr = np.zeros(radius_cuts.size) # x-axis doesn't have errors?
            #massratio_cutsErr = np.zeros(massratio_cuts.size) # x-axis doesn't have errors?


            for signifFunc in signifFunclist:

                # Calculate significance
                signifArr, signifErrArr = signifdict[signifFunc](sigArr, bkgArr, sigErrArr, bkgErrArr)
                if (DEBUG): 
                    print "BEFORE SET NAN AND INF TO ZERO:"
                    print "Using significance function:",signifFunc
                    print "sigArr looks like:\n",sigArr
                    print "bkgArr looks like:\n",bkgArr
                    print "signifArr looks like:\n",signifArr
                    print "signifErrArr looks like:\n",signifErrArr

                setInfinAndNANToZero(signifArr)
                setInfinAndNANToZero(signifErrArr)

                if (DEBUG): 
                    print "AFTER SET NAN AND INF TO ZERO:"
                    print "Using significance function:",signifFunc
                    print "sigArr looks like:\n",sigArr
                    print "bkgArr looks like:\n",bkgArr
                    print "signifArr looks like:\n",signifArr
                    print "signifErrArr looks like:\n",signifErrArr

                tg = TGraphErrors(signifArr.size, radius_cuts, signifArr, radius_cutsErr, signifErrArr)
                #mg.AddmakeTGraph(massratio_cuts, signifArr, massratio_cutsErr, signifErrArr, finalstate, zdmass) 
                tg.SetLineColor(tmplinecolor)
                tg.SetLineWidth(2)
                mg.Add(tg)
                tmplinecolor+=1
                #tg, legentry = makeTGraph(massratio_cuts, signifArr, massratio_cutsErr, signifErrArr, finalstate, zdmass) 
                leg.AddEntry(tg,signifFunc,"lp") # l=line, p=point, f=fill
#____________________________________________________________________________________________________
# Draw plots
            if (DRAW):
                c1 = TCanvas()
                plottitle   = "SigVsRadiusCut, mZd = %s GeV, final state = %s," % (zdmass, finalstate)
                xtitle      = "Radius Cut [GeV]" 
                ytitle      = "Significance"
                mg.SetTitle(plottitle +";"+ xtitle+";"+ ytitle)
                mg.Draw(graphOptions)
                leg.Draw("same")

                tempFileName = plotFileName.replace("MASS",zdmass)
                tempFileName = tempFileName.replace("FINALSTATE",finalstate)

                makeDirs(outputDir)
                copyFile("/home/rosedj1/","index.php",outputDir)
                c1.SaveAs(outputDir+tempFileName + ".pdf")
                c1.SaveAs(outputDir+tempFileName + ".png")

