from RA5.Dataset.NanoAOD.Run2016.common import * 

sampleName  = "WZZ"
dir_path    = common_path+"WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_151015/0000/"
inUFTier2   = True        
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_151015/0000/"
#inUFTier2=False,

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

WZZ = Dataset(
        "WZZ",
        cmpList,
        xs                  = 0.05565, #pb
        )
WZZ.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WZZ/EventWeight.root")
