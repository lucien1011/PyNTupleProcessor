from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "ttWJets"
dir_path    = common_path+"ttWJets_13TeV_madgraphMLM/InclusiveSelection_v1/180509_142516/0000/"
inUFTier2   = True
#dir_path   = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/ttWJets_13TeV_madgraphMLM/InclusiveSelection_v1/180509_142516/0000/"
#inUFTier2=False,

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

ttWJets = Dataset(
        "ttWJets",
        cmpList,
        xs                  = 0.6105, #pb
        )
ttWJets.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/ttWJets/EventWeight.root")
