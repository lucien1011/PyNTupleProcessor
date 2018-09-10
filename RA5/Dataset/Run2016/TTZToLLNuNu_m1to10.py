from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "TTZToLLNuNu_m1to10"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v2_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath = os.path.join(sumweight_path,sampleName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       [ Component("TTZToLLNuNu_m1to10",TreeDir + sampleName +"/"+ "TTZToLLNuNu_m1to10_%s_SkimTree.root"%i,"tree",inUFTier2) for i in range(0,1)]
          )

TTZToLLNuNu_m1to10= Dataset(
        "TTZToLLNuNu_m1to10",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )
TTZToLLNuNu_m1to10.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        TTZToLLNuNu_m1to10
        ]
