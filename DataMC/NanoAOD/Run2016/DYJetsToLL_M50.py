from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "DYJetsToLL_M50"
dir_path    = common_path+"CRAB_UserFiles/InclusiveSelection_v1/180509_134315/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_134315/0000/"
#inUFTier2   = False 

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        cmpList,
        xs                  = 5765.0 #pb,
        )
DYJetsToLL_M50.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/DYJetsToLL_M50/EventWeight.root")
#DYJetsToLL_M50.setSumWeight("/raid/raid7/kshi/SUSY/RPV/sum_weight/DYJetsToLL_M50_LO/EventWeight.root")
