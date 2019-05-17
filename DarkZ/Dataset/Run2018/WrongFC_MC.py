from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

bkgSkimTreeDir              = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190402/SkimTree_DarkPhoton_WrongFC_Run2018Data_m4l70/"
inUFTier2                   = False
bkgTreeDir                  = '/cms/data/store/user/t2/users/rosedj1/Higgs/HZZ4l/NTuple/Run2/MC2018_M19_Mar12_4l_2018Jets_JER_bestCandLegacy/'
sumWeightHist               = "Ana/sumWeights"
saveSumWeightTxt            = False

# ____________________________________________________________________________________________________________________________________________ ||
WFC_Reducible_cmpList = ComponentList(
        [
            Component("WFC_Reducible",bkgSkimTreeDir+"Data_Run2018_noDuplicates_FRWeightFromVukasinWZRemoved.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WFC_Reducible = Dataset(
        "WFC_Reducible",
        WFC_Reducible_cmpList,
        isMC = True,
        skipWeight = True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("WFC_Irreducible",bkgSkimTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "WFC_Irreducible",
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
        )

## ____________________________________________________________________________________________________________________________________________ ||
#DYJetsToLL_M50_cmpList = ComponentList(
#        [
#            Component("DYJetsToLL_M50",bkgSkimTreeDir+"DYJetsToLL_M50.root","passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#DYJetsToLL_M50 = Dataset(
#        "DYJetsToLL_M50",
#        DYJetsToLL_M50_cmpList,
#        isMC = True,
#        xs = 6104, 
#        )
#handleSumWeight(
#        DYJetsToLL_M50,
#        system,
#        bkgTreeDir_2lskim+"DYJetsToLL_M50.root",
#        sumWeightHist,
#        True,
#        saveSumWeightTxt,
#        bkgSkimTreeDir+"DYJetsToLL_M50.txt",
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#DYJetsToLL_M10To50_cmpList = ComponentList(
#        [
#            Component("DYJetsToLL_M10To50",bkgSkimTreeDir+"DYJetsToLL_M10To50.root","passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#DYJetsToLL_M10To50 = Dataset(
#        "DYJetsToLL_M10To50",
#        DYJetsToLL_M10To50_cmpList,
#        isMC = True,
#        xs = 6104, 
#        )
#handleSumWeight(
#        DYJetsToLL_M10To50,
#        system,
#        bkgTreeDir_2lskim+"DYJetsToLL_M10To50.root",
#        sumWeightHist,
#        True,
#        saveSumWeightTxt,
#        bkgSkimTreeDir+"DYJetsToLL_M10To50.txt",
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#TTJets_cmpList = ComponentList(
#        [
#            Component("TTJets",bkgSkimTreeDir+"TTJets.root","passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#TTJets = Dataset(
#        "TTJets",
#        TTJets_cmpList,
#        isMC = True,
#        xs = 87.31, 
#        )
#handleSumWeight(
#        TTJets,
#        system,
#        bkgTreeDir_2lskim+"TTJets.root",
#        sumWeightHist,
#        True,
#        saveSumWeightTxt,
#        bkgSkimTreeDir+"TTJets.txt",
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#WZTo3LNu_cmpList = ComponentList(
#        [
#            Component("WZTo3LNu",bkgSkimTreeDir+"WZTo3LNu.root","passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#WZTo3LNu = Dataset(
#        "WZTo3LNu",
#        WZTo3LNu_cmpList,
#        isMC = True,
#        xs = 0.04430, 
#        )
#handleSumWeight(
#        WZTo3LNu,
#        system,
#        bkgTreeDir_2lskim+"WZTo3LNu.root",
#        sumWeightHist,
#        True,
#        saveSumWeightTxt,
#        bkgSkimTreeDir+"WZTo3LNu.txt",
#        )
