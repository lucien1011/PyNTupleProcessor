from Core.ComponentList import *
from Core.Dataset import Dataset

DYJetsToLL_M10to50_cmp = Component(
        "DYJetsToLL_M10to50",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132404/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [DYJetsToLL_M10to50_cmp,],
        )

DYJetsToLL_M10to50 = Dataset(
        "DYJetsToLL_M10to50",
        cmpList,
        xs                  = 18610. #pb,
        )
