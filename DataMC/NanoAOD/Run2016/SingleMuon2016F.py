import os
from DataMC.NanoAOD.Run2016.common import *

sampleName  = "SingleMuon2016F"
#dir_path    = common_path_data+"SingleMuon/InclusiveSelection_v1/180618_121916/0000/"
dir_path    = "/raid/raid7/kshi/SUSY/RPV/UnSkimTree/data/SingleMuonF/"
inUFTier2   = False

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

SingleMuon2016F = Dataset(
        "SingleMuon2016F",
        cmpList,
        isMC = False,
        json = os.environ['BASE_PATH']+"/DataMC/JSON/13TeV/Run2016/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
        )
