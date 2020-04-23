from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgSkimTreeDir2      = system.getStoragePath()+"/lucien/Higgs/Zprime-NTuple/20190605/SkimTree_Zprime_Run2017Data_m4l70/"
bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/fakerate/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"
#dataTreeDir         = bkgSkimTreeDir
#dataTreeDir         = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/SkimTree_Run2017_MMM_Data/"
dataTreeDir         = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/fakerate/SkimTree_Run2017_MMM_Data/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = True

# ____________________________________________________________________________________________________________________________________________ ||
# Data2017
data2017_cmpList = ComponentList(
        [ 
            Component("Data2017",dataTreeDir+"Data_Run2017_DoubleMuon-SingleMuon_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),        
        ]
        )

data2017 = Dataset(
        "Data2017",
        data2017_cmpList,
        isMC                = False,
        )

# _________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M50",bkgSkimTreeDir+"DYJetsToLL_M50.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        DYJetsToLL_M50_cmpList,
        isMC = True,
        xs = 6104, 
        )
handleSumWeight(
        DYJetsToLL_M50,
        system,
        bkgTreeDir+"DYJetsToLL_M50.root",
        #bkgTreeDir+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"DYJetsToLL_M50.txt",
        bkgSkimTreeDir+"DYJetsToLL_M50.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M10To50",bkgSkimTreeDir+"DYJetsToLL_M10To50.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M10To50 = Dataset(
        "DYJetsToLL_M10To50",
        DYJetsToLL_M10To50_cmpList,
        isMC = True,
        xs = 6104, 
        )
handleSumWeight(
        DYJetsToLL_M10To50,
        system,
        bkgTreeDir+"DYJetsToLL_M10To50.root",
        #bkgTreeDir+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"DYJetsToLL_M10To50.txt",
        bkgSkimTreeDir+"DYJetsToLL_M10To50.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
TTJets_cmpList = ComponentList(
        [
            Component("TTJets",bkgSkimTreeDir+"TTJets.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets = Dataset(
        "TTJets",
        TTJets_cmpList,
        isMC = True,
        xs = 87.31, 
        )
handleSumWeight(
        TTJets,
        system,
        bkgTreeDir+"TTJets.root",
        #bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"TTJets.txt",
        bkgSkimTreeDir+"TTJets.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_cmpList = ComponentList(
        [
            Component("WZTo3LNu",bkgSkimTreeDir+"WZTo3LNu.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WZTo3LNu = Dataset(
        "WZTo3LNu",
        WZTo3LNu_cmpList,
        isMC = True,
        xs = 0.04430, 
        )
handleSumWeight(
        WZTo3LNu,
        system,
        bkgTreeDir+"WZTo3LNu.root",
        #bkgTreeDir+"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WZTo3LNu.txt",
        bkgSkimTreeDir+"WZTo3LNu.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples = [
        DYJetsToLL_M50,
        DYJetsToLL_M10To50,
        TTJets,
        WZTo3LNu,
        ]
dataSamples = [
        data2017,
        ]
frdataSamples = [
        data2017,
        ]
