from Core.ComponentList import *
from Core.Dataset import Dataset

sampleName  = "WZTo3LNu"
dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/InclusiveSelection_v1/180509_145452/0000/"

cmp = [ Component(sampleName,dir_path+"tree_"+str(i)+".root","Events",inUFTier2=False) 
        for i in range(1,6) 
        ]

#cmp = Component(
#        "WZTo3LNu",
#        #"/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/InclusiveSelection_v1/180509_145452/0000/",
#        ,
#        "Events",
#        keyword="tree",
#        #inUFTier2=True,
#        inUFTier2=False,
#        ).makeComponentFromEachFile(prefix="WZTo3LNu")

cmpList = ComponentList(
        #[cmp,],
        cmp,
        )

WZTo3LNu = Dataset(
        "WZTo3LNu",
        cmpList,
        xs                  = 4.4297, #pb
        )
WZTo3LNu.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WZTo3LNu/EventWeight.root")
