from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "TT_Powheg",
        #"/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/CRAB_UserFiles/InclusiveSelection_v1/180509_144936/0000/",
        "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/InclusiveSelection_v1/180509_144936/0000/",
        "Events",
        keyword="tree",
        #inUFTier2=True,
        inUFTier2=False,
        )

cmpList = ComponentList(
        [cmp,],
        )

TT_Powheg = Dataset(
        "TT_Powheg",
        cmpList,
        xs                  = 831.762, #pb
        )
TT_Powheg.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/TT_Powheg/EventWeight.root")
