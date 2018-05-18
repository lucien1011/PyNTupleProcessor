from DataMC.NanoAOD.Run2016.common import * 

sampleName  = "TToLeptons_sch"
dir_path    = common_path+"ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/InclusiveSelection_v1/180517_130903/0000/"
inUFTier2   = True

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

TToLeptons_sch = Dataset(
        sampleName,
        cmpList,
        xs                  = (7.20+4.16)*0.108*3 #pb,
        )
TToLeptons_sch.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/"+sampleName+"/EventWeight.root")
