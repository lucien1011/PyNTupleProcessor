from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "WWDoubleTo2L"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath = os.path.join(sumweight_path,sampleName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       [ Component("WWDoubleTo2L",TreeDir + sampleName +"/"+ "WWDoubleTo2L_%s_SkimTree.root",inUFTier2) for i in range(0,1)]
          )

WWDoubleTo2L= Dataset(
        "WWDoubleTo2L",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )
WWDoubleTo2L.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        WWDoubleTo2L
        ]
