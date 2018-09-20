from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents
from DataMC.Heppy.Run2016.HaddMC import TT_pow

sampleName   = "TT_pow"
fileName     = "treeProducerSusyRA5.root"
#TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v2_LeptonJetRecleaner_TT_pow/"
TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v2_LeptonJetRecleaner/"
#sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
inUFTier2    = True
#filePath = os.path.join(sumweight_path,sampleName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

cmpList = ComponentList(
                      # [ Component("TT_pow",TreeDir + sampleName + "/"+"TT_pow_%s_SkimTree.root"%i,"tree",inUFTier2) for i in range(0,414)]
                       [ Component("TT_pow",TreeDir + sampleName + "/"+"SkimTree.root","tree",inUFTier2)]
                      )

TT_pow.componentList = cmpList

#TT_pow= Dataset(
#        "TT_pow",
#        cmpList,
#        isMC                = True,
#        xs                  = 1,
#        )
#TT_pow.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        TT_pow
        ]
