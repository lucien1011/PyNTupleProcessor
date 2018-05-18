from RA5.Dataset.NanoAOD.Run2016.common import * 

sampleName  = "T_tch"
dir_path    = common_path+"ST_t-channel_top_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV-powhegV2-madspin/InclusiveSelection_v1/180517_143340/0000/"
inUFTier2   = True

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

T_tch = Dataset(
        sampleName,
        cmpList,
        xs                  = 126.5 #pb #FIXME,
        )
