from Core.ComponentList import *
from Core.Dataset import Dataset

bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180802/SkimTree_Z1LSelection_test/"
bkgTreeDir          = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"
#dataTreeDir         = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180730/SkimTree_Run2017Data/DarkZ/"
#dataTreeDir         = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180802/Sync_Run2017Data_v1/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
# DYJetsToLL_M50
DYJetsToLL_M50_cmpList = ComponentList(
        [ 
            Component("DYJetsToLL_M50",bkgSkimTreeDir+"DYJetsToLL_M50_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        DYJetsToLL_M50_cmpList,
        isMC                = True,
        xs                  = 6104,
        )
DYJetsToLL_M50.setSumWeight(bkgTreeDir+"DYJetsToLL_M50.root",sumWeightHist,True)

