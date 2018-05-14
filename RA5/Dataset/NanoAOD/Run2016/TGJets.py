from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "TGJets",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/InclusiveSelection_v1/180509_144401/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

TGJets = Dataset(
        "TGJets",
        cmpList,
        xs                  = 2.967, #pb
        )
