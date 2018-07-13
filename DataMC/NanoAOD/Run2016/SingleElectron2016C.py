import os
from DataMC.NanoAOD.Run2016.common import *

sampleName  = "SingleElectron2016C"
dir_path    = common_path+"SingleElectron/InclusiveSelection_v1/180710_120309/0000/"
#dir_path    = "/raid/raid7/kshi/SUSY/RPV/UnSkimTree/data/SingleElectronB/"
inUFTier2   = True

cmp = makeComponents(sampleName,dir_path,"Events",inUFTier2)

cmpList = ComponentList(
        cmp,
        )

SingleElectron2016C = Dataset(
        "SingleElectron2016C",
        cmpList,
        isMC = False,
        json = os.environ['BASE_PATH']+"/DataMC/JSON/13TeV/Run2016/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",
        )
