from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

bkgTreeDirT2_Feb21      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2l_Feb21/"
bkgTreeDirT2_Aug10      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2lskim_Aug10/"
#bkgTreeDir      = "/raid/raid7/kshi/Zprime/20190718/SkimTree_Run2016_MC/"
bkgTreeDir      = "/raid/raid7/kshi/Zprime/20190729/SkimTree_Run2016_mem_controlregion_MC/"
inUFTier2       = False
saveSumWeightTxt= False
sumWeightHist   = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_memCR_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M50_memCR",bkgTreeDir+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M50_memCR = Dataset(
        "DYJetsToLL_M50_memCR",
        DYJetsToLL_M50_memCR_cmpList,
        isMC = True,
        xs = 6104, 
        )
handleSumWeight(
        DYJetsToLL_M50_memCR,
        system,
        bkgTreeDirT2_Feb21+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        #bkgTreeDir+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_memCR_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M10To50_memCR",bkgTreeDir+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M10To50_memCR = Dataset(
        "DYJetsToLL_M10To50_memCR",
        DYJetsToLL_M10To50_memCR_cmpList,
        isMC = True,
        xs = 6104, 
        )
handleSumWeight(
        DYJetsToLL_M10To50_memCR,
        system,
        bkgTreeDirT2_Aug10+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        #bkgTreeDir+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
TTJets_memCR_cmpList = ComponentList(
        [
            Component("TTJets_memCR",bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets_memCR = Dataset(
        "TTJets_memCR",
        TTJets_memCR_cmpList,
        isMC = True,
        xs = 87.31, 
        )
handleSumWeight(
        TTJets_memCR,
        system,
        bkgTreeDirT2_Feb21+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root",
        #bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_memCR_cmpList = ComponentList(
        [
            Component("WZTo3LNu_memCR",bkgTreeDir+"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WZTo3LNu_memCR = Dataset(
        "WZTo3LNu_memCR",
        WZTo3LNu_memCR_cmpList,
        isMC = True,
        xs = 0.04430, 
        )
handleSumWeight(
        WZTo3LNu_memCR,
        system,
        bkgTreeDirT2_Feb21+"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        #bkgTreeDir+"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.txt",
        )

bkgSamples = [WZTo3LNu_memCR,]
'''
bkgSamples = [
            WZTo3LNu_memCR,
            TTJets_memCR,
            DYJetsToLL_M10To50_memCR,
            DYJetsToLL_M50_memCR
            ]
'''
