from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "TTWToLNu"
sumweightName= "TTWToLNu_ext"
sumweightName2= "TTWToLNu_ext2"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath1 = os.path.join(sumweight_path,sumweightName,fileName)
filePath2 = os.path.join(sumweight_path,sumweightName2,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       [ Component("TTWToLNu",TreeDir + sampleName +"/"+ "TTWToLNu_%s_SkimTree.root"%i,"tree",inUFTier2) for i in range(0,2)]
          )

TTWToLNu_ext= Dataset(
        "TTWToLNu_ext",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )

TTWToLNu_ext2= Dataset(
        "TTWToLNu_ext2",
        ComponentList([]),
        isMC                = True,
        xs                  = 1,
        )

TTWToLNu_ext.setSumWeight(filePath1,"SumGenWeights",inUFTier2)
TTWToLNu_ext2.setSumWeight(filePath2,"SumGenWeights",inUFTier2)

TTWToLNu_ext.add(TTWToLNu_ext2)

Samples = [
        TTWToLNu_ext
        ]
