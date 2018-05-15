from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "ZZZ",
        #"/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_150353/0000/",
        "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_150353/0000/",
        "Events",
        keyword="tree",
        #inUFTier2=True,
        inUFTier2=False,
        )

cmpList = ComponentList(
        [cmp,],
        )

ZZZ = Dataset(
        "ZZZ",
        cmpList,
        xs                  = 0.01398, #pb
        )
ZZZ.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/ZZZ/EventWeight.root")
