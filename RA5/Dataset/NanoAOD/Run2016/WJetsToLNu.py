from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "WJetsToLNu",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132731/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

WJetsToLNu = Dataset(
        "WJetsToLNu",
        cmpList,
        xs                  = 61334.9, #pb
        )
