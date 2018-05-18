from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "ZGTo2LG",
dir_path    = common_path+"ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/InclusiveSelection_v1/180509_145232/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/InclusiveSelection_v1/180509_145232/0000/"
#inUFTier2  = False

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

ZGTo2LG = Dataset(
        "ZGTo2LG",
        cmpList,
        xs                  = 123.9, #pb
        )
ZGTo2LG.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/ZGTo2LG/EventWeight.root")
