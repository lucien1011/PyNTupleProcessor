from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "ttZJets"
dir_path    = common_path+"ttZJets_13TeV_madgraphMLM-pythia8/InclusiveSelection_v1/180509_143510/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/ttZJets_13TeV_madgraphMLM-pythia8/InclusiveSelection_v1/180509_143510/0000/"
#inUFTier2   = False

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

ttZJets = Dataset(
        "ttZJets",
        cmpList,
        xs                  = 0.7826, #pb
        )
ttZJets.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/ttZJets/EventWeight.root")
