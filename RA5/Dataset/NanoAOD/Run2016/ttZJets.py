from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "ttZJets",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/ttZJets_13TeV_madgraphMLM-pythia8/InclusiveSelection_v1/180509_143510/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

ttZJets = Dataset(
        "ttZJets",
        cmpList,
        xs                  = 0.7826, #pb
        )
