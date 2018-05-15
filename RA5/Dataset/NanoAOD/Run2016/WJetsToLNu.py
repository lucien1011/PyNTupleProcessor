from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "WJetsToLNu",
        #"/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132731/0000/",
        "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132731/0000/",
        "Events",
        keyword="tree",
        #inUFTier2=True,
        inUFTier2=False,
        )

cmpList = ComponentList(
        [cmp,],
        )

WJetsToLNu = Dataset(
        "WJetsToLNu",
        cmpList,
        xs                  = 61334.9, #pb
        )
WJetsToLNu.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WJetsToLNu/EventWeight.root")
