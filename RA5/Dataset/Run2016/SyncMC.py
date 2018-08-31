from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName      = "SyncMC"
filePath        = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/SyncMC2016/TTW_RA5_sync/treeProducerSusyRA5/tree.root"
inUFTier2       = True

cmpList = ComponentList(
                       [ Component(
                            sampleName,
                            filePath,
                            "tree",
                            inUFTier2,
                           )
                        ]
                        )

SyncMC = Dataset(
        "SyncMC",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )
SyncMC.setSumWeight(filePath,"SumGenWeights",inUFTier2)
