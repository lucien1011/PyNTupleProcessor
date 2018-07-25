from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents
from DataMC.Heppy.Run2016.HaddMC import TT_pow

sampleName      = "T1qqqqL"
fileName        = "SkimTree.root"
treeName        = "tree"
treeDir         = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/SMS-T1qqqqL_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_SMS-T1qqqqL/"
inUFTier2       = True

# _______________________________________________________________________________________________________________ ||
# T1qqqqL 1000
comp_1000       = Component("SMS-T1qqqqL",treeDir+"SMS-T1qqqqL_mGluino1000/"+fileName,treeName,inUFTier2=inUFTier2)
cmpList_1000    = ComponentList([comp_1000])
T1qqqqL_1000 = Dataset(
        "SMS-T1qqqqL_mGluino1000",
        cmpList_1000,
        isSignal = True,
        )
T1qqqqL_1000.setSumWeight(sumweight_path+"mGluino1000/"+fileName,sumWeight,inUFTier2=inUFTier2)

# _______________________________________________________________________________________________________________ ||
# T1qqqqL 1500
comp_1500       = Component("SMS-T1qqqqL",treeDir+"SMS-T1qqqqL_mGluino1000/"+fileName,treeName,inUFTier2=inUFTier2)
cmpList_1500    = ComponentList([comp_1500])
T1qqqqL_1500 = Dataset(
        "SMS-T1qqqqL_mGluino1500",
        cmpList_1500,
        isSignal = True,
        )
T1qqqqL_1500.setSumWeight(sumweight_path+"mGluino1500/"+fileName,sumWeight,inUFTier2=inUFTier2)


