#!/bin/bash
#####################################################################################################
## PURPOSE: 
## SYNTAX:  
## NOTES:   
## AUTHOR:  
## DATE:    
## UPDATED: 
#####################################################################################################

#____________________________________________________________________________________________________
# User Parameters
import ROOT
import sys
from DataFormats.FWLite import Events, Handle
import numpy as np
#import matplotlib.pyplot as plt
#___________________________________________________________________________
# User Parameters
onTier2 = True

#___________________________________________________________________________
# Automatic Stuff
t2_prefix = "root://cmsio5.rc.ufl.edu/"

if onTier2:
    inputfile = str(t2_prefix+sys.argv[1])
else:
    inputfile = str(sys.argv[1])
openfile = ROOT.TFile.Open(inputfile,"READ")

events = Events(openfile)
## Handle(Type). Example Handles:
#handle = Handle('std::vector<reco::GenParticle>')
handle = Handle('vector<reco::GenParticle>')
label = ("genParticles","","SIM") 

# Each item in this for loop is an entire gg-->H-->ZZd-->4lep process ###
numProcess = 0
for count,e in enumerate(events, 1):
    if count > 100: break
    e.getByLabel(label,handle)
    genParticles = handle.product()
    numProcess+=1
# Each item in this for loop is a single particle in the process above ###
    for p in genParticles:
        if not p.isHardProcess(): continue
            #print p.pdgId(),p.pt(),p.eta()
            # Potentially interesting quantities:
            # charge(), p4(), p(), energy(), et?, et2?,
            # mass(), massSqr(), pt(), phi(), theta(), eta()
            # rapidity(), vertex(), status(), longLived()
            # isElectron(), isMuon(), is StandAloneMuon()
            # isGlobalMuon(), isTrackerMuon(), isCaloMuon()
            # is Photon(), isConvertedPhoton(), isJet()
        if p.pdgId() == 1023: 
            #print "-"*20 
            print "Process %d: %f" % (count, p.mass() )
print "\n", "Number of events analyzed:", numProcess  
print "Total number of isHardProcess events in root file:", count, "\n"
