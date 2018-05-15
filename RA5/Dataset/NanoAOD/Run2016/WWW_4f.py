from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "WWW_4f",
        #"/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_151248/0000/",
        "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_151248/0000/",
        "Events",
        keyword="tree",
        #inUFTier2=True,
        inUFTier2=False,
        )

cmpList = ComponentList(
        [cmp,],
        )

WWW_4f = Dataset(
        "WWW_4f",
        cmpList,
        xs                  = 0.2086, #pb
        )
WWW_4f.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WWW_4f/EventWeight.root")
