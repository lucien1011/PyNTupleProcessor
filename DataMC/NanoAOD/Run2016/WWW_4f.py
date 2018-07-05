from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "WWW_4f",
dir_path    = common_path+"WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_151248/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/InclusiveSelection_v1/180509_151248/0000/"
#inUFTier2=False,

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

WWW_4f = Dataset(
        "WWW_4f",
        cmpList,
        xs                  = 0.2086, #pb
        )
#WWW_4f.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WWW_4f/EventWeight.root")
WWW_4f.setSumWeight("/raid/raid7/kshi/SUSY/RPV/sum_weight/WWW_4f/EventWeight.root")
