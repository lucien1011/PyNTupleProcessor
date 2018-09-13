from Core.ComponentList import *
from Core.Dataset import Dataset

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
ZPlusX_cmpList = ComponentList(
        [
            #Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180910/SkimTree_Upsilon_ZX_Run2016Data_DarkPhotonReco/Data_Run2016_noDuplicates_1_FRWeight.root","passedEvents",False)
            Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180911/SkimTree_Upsilon_ZX_Run2016Data_DarkPhotonReco/Data_Run2016_noDuplicates_1_FRWeight.root","passedEvents",False)
            #Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180910/SkimTree_Upsilon_ZX_Run2016Data/Data_Run2016_noDuplicates_FRWeight.root","passedEvents",False)
        ]
        )
ZPlusX = Dataset(
        "ZPlusX",
        ZPlusX_cmpList,
        isMC                = True,
        skipWeight          = True,
        )
