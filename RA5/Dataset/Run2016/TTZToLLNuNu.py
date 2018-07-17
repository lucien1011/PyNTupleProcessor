from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "TTZToLLNuNu"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath = os.path.join(sumweight_path,sampleName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       [ Component("TTZToLLNuNu",TreeDir + sampleName +"/"+ "TTZToLLNuNu_%s_SkimTree.root",inUFTier2) for i in range(0,1)]
          )

TTZToLLNuNu= Dataset(
        "TTZToLLNuNu",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )
TTZToLLNuNu.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        TTZToLLNuNu
        ]
