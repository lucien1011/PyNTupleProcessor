from RA5.Dataset.NanoAOD.Run2016.common import * 

sampleName  = "TT_Powheg",
dir_path    = common_path+"CRAB_UserFiles/InclusiveSelection_v1/180509_144936/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/InclusiveSelection_v1/180509_144936/0000/"
#inUFTier2   = False

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

TT_Powheg = Dataset(
        "TT_Powheg",
        cmpList,
        xs                  = 831.762, #pb
        )
TT_Powheg.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/TT_Powheg/EventWeight.root")
