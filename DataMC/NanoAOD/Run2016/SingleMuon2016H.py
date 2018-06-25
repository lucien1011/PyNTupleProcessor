import os
from DataMC.NanoAOD.Run2016.common import *

sampleName  = "SingleMuon2016H"
dir_path    = common_path_data+"SingleMuon/InclusiveSelection_v1/180619_103854/0000/"
inUFTier2   = True

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

SingleMuon2016H = Dataset(
        "SingleMuon2016H",
        cmpList,
        isMC = False,
        json = os.environ['BASE_PATH']+"/DataMC/JSON/13TeV/Run2016/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
        )
