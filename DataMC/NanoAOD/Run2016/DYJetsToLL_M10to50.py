from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "DYJetsToLL_M10to50"
dir_path    = common_path+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132404/0000/"
inUFTier2   = True

#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_132404/0000/"
#inUFTier2   = False

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

DYJetsToLL_M10to50 = Dataset(
        "DYJetsToLL_M10to50",
        cmpList,
        xs                  = 16270.0 #pb,
        )
DYJetsToLL_M10to50.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/DYJetsToLL_M10to50/EventWeight.root")
