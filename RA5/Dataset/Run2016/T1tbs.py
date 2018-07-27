from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents

sampleName      = "T1tbs"
fileName        = "SkimTree.root"
treeName        = "tree"
treeDir         = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/SMS-T1tbs_LeptonJetRecleaner/"
sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_SMS-T1tbs/"
sumweight_file  = "treeProducerSusyRA5.root"
sumWeight       = "SumGenWeights"
inUFTier2       = True

# _______________________________________________________________________________________________________________ ||
# T1tbs 1000
comp_1000       = Component("SMS-T1tbs",treeDir+"SMS-T1tbs_mGluino1000/"+fileName,treeName,inUFTier2=inUFTier2)
cmpList_1000    = ComponentList([comp_1000])
T1tbs_1000 = Dataset(
        "SMS-T1tbs_mGluino1000",
        cmpList_1000,
        isSignal = True,
        isMC = True,
        xsFactor = 0.09,
        plotLabel = "T1tbs, m_{Gluino} = 1000",
        )
T1tbs_1000.setSumWeight(sumweight_path+"mGluino1000/"+sumweight_file,sumWeight,inUFTier2=inUFTier2)

# _______________________________________________________________________________________________________________ ||
# T1tbs 1500
comp_1500       = Component("SMS-T1tbs",treeDir+"SMS-T1tbs_mGluino1500/"+fileName,treeName,inUFTier2=inUFTier2)
cmpList_1500    = ComponentList([comp_1500])
T1tbs_1500 = Dataset(
        "SMS-T1tbs_mGluino1500",
        cmpList_1500,
        isSignal = True,
        isMC = True,
        xsFactor = 0.09,
        plotLabel = "T1tbs, m_{Gluino} = 1500",
        )
T1tbs_1500.setSumWeight(sumweight_path+"mGluino1500/"+sumweight_file,sumWeight,inUFTier2=inUFTier2)


