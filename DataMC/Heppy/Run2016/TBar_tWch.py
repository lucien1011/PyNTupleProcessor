from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "TBar_tWch"
dir_path    = common_path+"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/InclusiveSelection_v1/180517_135514/0000/"
inUFTier2   = True

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

TBar_tWch = Dataset(
        sampleName,
        cmpList,
        xs                  = 38.09 #pb,
        )
TBar_tWch.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/"+sampleName+"/EventWeight.root")
