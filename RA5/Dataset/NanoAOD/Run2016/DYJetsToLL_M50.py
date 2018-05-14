from Core.ComponentList import *
from Core.Dataset import Dataset

DYJetsToLL_M50_cmp = Component(
        "DYJetsToLL_M50",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/CRAB_UserFiles/InclusiveSelection_v1/180509_134315/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [DYJetsToLL_M50_cmp,],
        )

DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        cmpList,
        xs                  = 18610. #pb,
        )
