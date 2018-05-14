from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "WWZ",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_150942/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

WWZ = Dataset(
        "WWZ",
        cmpList,
        xs                  = 0.1651, #pb
        )
WWZ.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WWZ/EventWeight.root")
