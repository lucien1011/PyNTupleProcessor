import os
from Core.ComponentList import *
from Core.Dataset import Dataset

fileName        = "SkimTree.root"
common_path     = "/raid/raid7/lucien/SUSY/RPV/SkimTree/StopToBLep/2018-06-18/SingleMuon2016B_BaselineSelection_v1/"
inUFTier2       = False

sampleNames = [n for n in os.listdir(common_path) if os.path.isdir(os.path.join(common_path, n))]
allDataSamples = []
for sampleName in sampleNames:
    tmpList = ComponentList([Component(sampleName,"/".join([common_path,sampleName,fileName]),"Events",inUFTier2,maxEvents=-1)],)
    tmpDataset = Dataset(sampleName,tmpList,isMC=False,json=os.environ['BASE_PATH']+"/DataMC/JSON/13TeV/Run2016/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt",)
    allDataSamples.append(tmpDataset)
