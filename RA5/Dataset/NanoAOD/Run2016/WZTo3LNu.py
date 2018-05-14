from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "WZTo3LNu",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/InclusiveSelection_v1/180509_145452/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

WZTo3LNu = Dataset(
        "WZTo3LNu",
        cmpList,
        xs                  = 4.4297, #pb
        )
