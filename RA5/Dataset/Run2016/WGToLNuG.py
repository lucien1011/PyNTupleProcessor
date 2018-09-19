from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName   = "WGToLNuG"
fileName     = "treeProducerSusyRA5.root"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v2_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
filePath = os.path.join(sumweight_path,sampleName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                       [ Component("WGToLNuG",TreeDir + sampleName +"/"+ "WGToLNuG_%s_SkimTree.root"%i,"tree",inUFTier2) for i in range(0,1)]
          )

WGToLNuG= Dataset(
        "WGToLNuG",
        cmpList,
        isMC                = True,
        xs                  = 1,
        )
WGToLNuG.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        WGToLNuG
        ]
