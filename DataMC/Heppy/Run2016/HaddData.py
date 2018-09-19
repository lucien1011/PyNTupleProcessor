from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents
from Core.Utils.UFTier2Utils import *
import os

common_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Data2016_July18_v1/"
fileName    = "treeProducerSusyRA5.root"
inUFTier2   = True
treeName    = "tree"
pdNames     = [
                "MuonEG",
                "DoubleMuon",
                "DoubleEG",
              ]
selection   = lambda x: "Run2016B" not in x

#componentList = []
sampleDict = {}
sampleFileNames = listdir_uberftp(common_path,selection=lambda x: True)
for pdName in pdNames:
    sampleNameList = [k for k in sampleFileNames if pdName in k and selection(k)]
    cmp_list = []
    for sampleName in sampleNameList:
        cmp_list.append(Component(sampleName,os.path.join(common_path,sampleName,fileName),treeName,inUFTier2,))
    cmpList = ComponentList(cmp_list)
    tmpDataset = Dataset(pdName,cmpList,isMC=False)
    if pdName not in sampleDict:
        sampleDict[pdName] = tmpDataset
    else:
        sampleDict[pdName].add(tmpDataset)

componentList = sampleDict.values()
