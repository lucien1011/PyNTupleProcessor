from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

bkgSkimTreeDir      = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/102X_MCProd_DarkZNTuple/"
bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cmsuf/data/store/user/t2/users/rosedj1/Higgs/HZZ4l/NTuple/Run2/MC2018_M19_Mar12_4l_2018Jets_JER_bestCandLegacy/"
dataTreeDir         = bkgSkimTreeDir
inUFTier2           = True
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = False

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
handleSumWeight(
        qqZZTo4L,
        system,
        bkgTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.txt",
        bkgSkimTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu",bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
handleSumWeight(
        ggZZTo4mu,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
        bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples = [
        qqZZTo4L,
        ggZZTo4mu,
        ]
