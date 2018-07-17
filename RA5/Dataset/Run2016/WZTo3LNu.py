from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "WZTo3LNu"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath = os.path.join(sumweight_path,sampleName,fileName)

cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       cmp,
          )

WZTo3LNu= Dataset(
        "WZTo3LNu",
        cmpList,
        isMC                = True,
        xs                  = 16270.0,
        )
WZTo3LNu.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        WZTo3LNu
        ]
