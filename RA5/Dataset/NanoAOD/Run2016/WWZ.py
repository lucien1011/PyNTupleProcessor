from RA5.Dataset.NanoAOD.Run2016.common import * 

sampleName  = "WWZ"
dir_path    = common_path+"WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_150942/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_150942/0000/"
#inUFTier2  =False 

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

WWZ = Dataset(
        "WWZ",
        cmpList,
        xs                  = 0.1651, #pb
        )
WWZ.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WWZ/EventWeight.root")
