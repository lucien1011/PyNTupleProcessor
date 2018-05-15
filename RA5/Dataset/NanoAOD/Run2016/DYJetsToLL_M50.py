from Core.ComponentList import *
from Core.Dataset import Dataset

DYJetsToLL_M50_cmp = Component(
        "DYJetsToLL_M50",
        #"/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/CRAB_UserFiles/InclusiveSelection_v1/180509_134315/0000/",
        "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_134315/0000/",
        "Events",
        keyword="tree",
        #inUFTier2=True,
        inUFTier2=False,
        )

cmpList = ComponentList(
        [DYJetsToLL_M50_cmp,],
        )

DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        cmpList,
        xs                  = 18610. #pb,
        )
DYJetsToLL_M50.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/DYJetsToLL_M50/EventWeight.root")
