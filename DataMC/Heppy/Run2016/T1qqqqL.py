from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents
from Core.Utils.UFTier2Utils import *
import os

# _______________________________________________________________________________________________________________ ||
common_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_SMS-T1qqqqL/"
fileName    = "treeProducerSusyRA5.root"
inUFTier2   = True
treeName    = "tree"
sumWeight   = "SumGenWeights"

# _______________________________________________________________________________________________________________ ||
# T1qqqqL 1000
comp_1000       = Component("SMS-T1qqqqL",common_path+"mGluino1000/"+fileName,treeName,inUFTier2=inUFTier2)
cmpList_1000    = ComponentList([comp_1000])
T1qqqqL_1000 = Dataset(
        "SMS-T1qqqqL_mGluino1000",
        cmpList_1000,
        )
T1qqqqL_1000.setSumWeight(common_path+"mGluino1000/"+fileName,sumWeight,inUFTier2=inUFTier2)

# _______________________________________________________________________________________________________________ ||
# T1qqqqL 1500
comp_1500       = Component("SMS-T1qqqqL",common_path+"mGluino1500/"+fileName,treeName,inUFTier2=inUFTier2)
cmpList_1500    = ComponentList([comp_1500])
T1qqqqL_1500 = Dataset(
        "SMS-T1qqqqL_mGluino1500",
        cmpList_1500,
        )
T1qqqqL_1500.setSumWeight(common_path+"mGluino1500/"+fileName,sumWeight,inUFTier2=inUFTier2)

# _______________________________________________________________________________________________________________ ||
