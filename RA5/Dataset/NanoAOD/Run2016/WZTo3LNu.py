from RA5.Dataset.NanoAOD.Run2016.common import * 

sampleName  = "WZTo3LNu"
dir_path    = common_path+"WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/InclusiveSelection_v1/180509_145452/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/InclusiveSelection_v1/180509_145452/0000/"
#inUFTier2   = False 

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

WZTo3LNu = Dataset(
        sampleName,
        cmpList,
        xs                  = 4.4297, #pb
        )
WZTo3LNu.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WZTo3LNu/EventWeight.root")
