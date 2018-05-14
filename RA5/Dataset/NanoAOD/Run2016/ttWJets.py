from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "ttWJets",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/ttWJets_13TeV_madgraphMLM/InclusiveSelection_v1/180509_142516/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

ttWJets = Dataset(
        "ttWJets",
        cmpList,
        xs                  = 0.6105, #pb
        )
