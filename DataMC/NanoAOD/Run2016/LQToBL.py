from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "LQToBL_mLQ500"
dir_path    = common_path_sig+"LQToBL_mLQ500_GEN-SIM/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/180709_203940/0000/"
inUFTier2   = True
#dir_path    = "/raid/raid7/lucien/SUSY/RA5/NanoAOD/2016/MC/InclusiveSelection_v1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/InclusiveSelection_v1/180509_134315/0000/"
#inUFTier2   = False 

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

LQToBL_mLQ500 = Dataset(
        "LQToBL_mLQ500",
        cmpList,
        xs                  = 1., #pb,
        isMC                = True,
        isSignal            = True,
        )
LQToBL_mLQ500.setSumWeight("/raid/raid7/lucien/SUSY/RPV/SumGenWeight/NanoAOD_InclusiveSelection_v2/LQToBL_mLQ500/EventWeight.root")
