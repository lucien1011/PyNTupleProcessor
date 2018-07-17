from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "TTGJets"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath = os.path.join(sumweight_path,sampleName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       [ Component("TTGJets",TreeDir + sampleName +"/"+ "TTGJets_%s_SkimTree.root",inUFTier2) for i in range(0,1)]
          )

TTGJets= Dataset(
        "TTGJets",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )
TTGJets.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        TTGJets
        ]
