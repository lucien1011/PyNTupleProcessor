#!/bin/bash
#####################################################################################################
## PURPOSE: Check to see which files are missing after running plot_DarkPhoton.py with radius cuts.
##          This is typically used on files like: "DataMCDistribution_radiuscut1p2GeV.root" 
##          for which a particular radius cut failed to get produced. Iterate over radius cuts.
## SYNTAX:  python <script.py>
## NOTES:   User should scroll down to main and check the firstnum and secondnum variables.
## AUTHOR:  Jake Rosenzweig
## DATE:    2019-03-15
## UPDATED: 
#####################################################################################################

#____________________________________________________________________________________________________
# User Parameters
import glob
import os

#____________________________________________________________________________________________________
# Functions
def checkfiles(pathtofile, findfile, firstnum, secondnum):
    '''
    firstnum and secondnum should be iterables (lists, ranges, etc.)
    '''

    firstnum = [str(x) for x in firstnum]
    secondnum = [str(x) for x in secondnum]

    #absdir = parentdir + bkgdir

    for first in firstnum:
        for second in secondnum:
            
            filename = findfile.replace('NUM1',first).replace('NUM2',second)
            fileinquestion = pathtofile+filename

            if ( not os.path.exists(fileinquestion) ):
                print "WARNING!!!",fileinquestion,"DOES NOT EXIST!"
                print 
            #else:
            #    print fileinquestion,"exists"


getLastDir = lambda x : x.split('/')[-2]+'/' 

#____________________________________________________________________________________________________
# Main
parentdir = "/raid/raid7/rosedj1/Higgs/HToZdZd/DarkPhotonSR/DataMCDistributions/RadiusCuts/SignifRadiusCut_0p1to3p0in0p1GeVsteps/"
findfile = "DataMCDistribution_radiuscutNUM1"+"p"+"NUM2GeV.root"

pathtosignifdirslist = glob.glob(parentdir+'*/')
signifdirslist = [getLastDir(x) for x in pathtosignifdirslist]

for signifdir in pathtosignifdirslist:
    bkgdirpaths = glob.glob(signifdir+"*/")
    bkgdirnames = [getLastDir(x) for x in bkgdirpaths]

    for bkgdir in bkgdirnames:
        checkfiles( signifdir+bkgdir, findfile, [0], range(1,10) )
        checkfiles( signifdir+bkgdir, findfile, [1,2], range(0,10) )
        checkfiles( signifdir+bkgdir, findfile, [3], range(1) )
