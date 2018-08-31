from Core.ComponentList import *
from Core.Dataset import Dataset

bkgTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_MC80X_ZXCRSelection/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M50",bkgTreeDir+"DYJetsToLL_M50_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        DYJetsToLL_M50_cmpList,
        isMC = True,
        xs = 6104, 
        )
DYJetsToLL_M50.setSumWeight("/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/DYJetsToLL_M50.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M10To50",bkgTreeDir+"DYJetsToLL_M10To50_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M10To50 = Dataset(
        "DYJetsToLL_M10To50",
        DYJetsToLL_M10To50_cmpList,
        isMC = True,
        xs = 18610, 
        )
DYJetsToLL_M10To50.setSumWeight("/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/DYJetsToLL_M10To50.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
TTJets_cmpList = ComponentList(
        [
            Component("TTJets",bkgTreeDir+"TTJets_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets = Dataset(
        "TTJets",
        TTJets_cmpList,
        isMC = True,
        xs = 815.96, 
        )
TTJets.setSumWeight("/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/TTJets.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_cmpList = ComponentList(
        [
            Component("WZTo3LNu",bkgTreeDir+"WZTo3LNu_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WZTo3LNu = Dataset(
        "WZTo3LNu",
        WZTo3LNu_cmpList,
        isMC = True,
        xs = 0.04430, 
        )
WZTo3LNu.setSumWeight("/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/WZTo3LNu.root","Ana/sumWeights",True)
