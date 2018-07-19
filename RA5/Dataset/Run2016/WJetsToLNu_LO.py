from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "WJetsToLNu_LO"
sumweightName= "WJetsToLNu_LO_ext"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath1 = os.path.join(sumweight_path,sampleName,fileName)
filePath2 = os.path.join(sumweight_path,sumweightName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       [ Component("WJetsToLNu_LO",TreeDir + sampleName +"/"+ "WJetsToLNu_LO_%s_SkimTree.root","tree",inUFTier2) for i in range(0,2)]
          )

WJetsToLNu_LO= Dataset(
        "WJetsToLNu_LO",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )

WJetsToLNu_LO_ext= Dataset(
        "WJetsToLNu_LO_ext",
        ComponentList([]),
        isMC                = True,
        xs                  = 1,
        )


WJetsToLNu_LO.setSumWeight(filePath1,"SumGenWeights",inUFTier2)
WJetsToLNu_LO_ext.setSumWeight(filePath2,"SumGenWeights",inUFTier2)

WJetsToLNu_LO.add(WJetsToLNu_LO_ext)

Samples = [
        WJetsToLNu_LO
        ]
