from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "DYJetsToLL_M50_LO"
sumweightName= "DYJetsToLL_M50_LO_ext"
sumweightName2= "DYJetsToLL_M50_LO_ext2"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath1 = os.path.join(sumweight_path,sumweightName,fileName)
filePath2 = os.path.join(sumweight_path,sumweightName2,fileName)

#cmp = makeComponents(sampleName, TreeDir, "tree", inUFTier2)

cmpList = ComponentList(
                       [ Component("DYJetsToLL_M50_LO",TreeDir + sampleName +"/"+ "DYJetsToLL_M50_LO_%s_SkimTree.root",inUFTier2) for i in range(0,2)]
          )

DYJetsToLL_M50_LO_ext= Dataset(
        "DYJetsToLL_M50_LO_ext",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )

DYJetsToLL_M50_LO_ext2= Dataset(
        "DYJetsToLL_M50_LO_ext2",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )

DYJetsToLL_M50_LO_ext.setSumWeight(filePath1,"SumGenWeights",inUFTier2)
DYJetsToLL_M50_LO_ext2.setSumWeight(filePath2,"SumGenWeights",inUFTier2)

DYJetsToLL_M50_LO_ext.add(DYJetsToLL_M50_LO_ext2)


Samples = [
        DYJetsToLL_M50_LO_ext
        ]
