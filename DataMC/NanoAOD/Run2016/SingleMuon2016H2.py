import os
from DataMC.NanoAOD.Run2016.common import *

sampleName  = "SingleMuon2016H2"
#dir_path    = common_path_data+"SingleMuon/InclusiveSelection_v1/180626_140110/0000/"
dir_path    = "/raid/raid7/kshi/SUSY/RPV/UnSkimTree/data/SingleMuonH2/"
inUFTier2   = False

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

SingleMuon2016H2 = Dataset(
        "SingleMuon2016H2",
        cmpList,
        isMC = False,
        json = os.environ['BASE_PATH']+"/DataMC/JSON/13TeV/Run2016/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
        )
