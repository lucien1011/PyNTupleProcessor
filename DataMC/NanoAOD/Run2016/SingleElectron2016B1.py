import os
from DataMC.NanoAOD.Run2016.common import *

sampleName  = "SingleElectron2016B1"
dir_path    = common_path+"SingleElectron/InclusiveSelection_v1/180710_114624/0000/"
#dir_path    = "/raid/raid7/kshi/SUSY/RPV/UnSkimTree/data/SingleElectronB/"
inUFTier2   = True

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

SingleElectron2016B1 = Dataset(
        "SingleElectron2016B1",
        cmpList,
        isMC = False,
        json = os.environ['BASE_PATH']+"/DataMC/JSON/13TeV/Run2016/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
        )
