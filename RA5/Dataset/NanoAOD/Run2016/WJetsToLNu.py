from RA5.Dataset.NanoAOD.Run2016.common import * 

sampleName  = "WJetsToLNu"
dir_path    = common_path+"WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132731/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132731/0000/"
#inUFTier2   = False

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

WJetsToLNu = Dataset(
        "WJetsToLNu",
        cmpList,
        xs                  = 61334.9, #pb
        )
WJetsToLNu.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/WJetsToLNu/EventWeight.root")
