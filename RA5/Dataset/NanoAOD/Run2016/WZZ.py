from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "WZZ",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_151015/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

WZZ = Dataset(
        "WZZ",
        cmpList,
        xs                  = 0.05565, #pb
        )
WZZ.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WZZ/EventWeight.root")
