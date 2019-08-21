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
# ____________________________________________________________________________________________________________________________________________ ||
TTJets_fromT_cmpList = ComponentList(
        [
            Component("TTJets_fromT",bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets_fromT = Dataset(
        "TTJets_fromT",
        TTJets_fromT_cmpList,
        isMC = True,
        xs = 87.31, 
        )
handleSumWeight(
        TTJets_fromT,
        system,
        bkgTreeDirT2_Feb21+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root",
        #bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.txt",
        )

TTJets_notfromT_cmpList = ComponentList(
        [
            Component("TTJets_notfromT",bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets_notfromT = Dataset(
        "TTJets_notfromT",
        TTJets_notfromT_cmpList,
        isMC = False,
        #xs = 87.31, 
        )


