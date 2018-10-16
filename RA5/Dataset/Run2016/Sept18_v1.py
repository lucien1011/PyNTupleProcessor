from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.UFTier2Utils import listdir_uberftp
import os

#dir_path        = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Sept18_v1/"
dir_path        = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/Sept18_v1/"
inUFTier2       = False
treeName        = "tree"

componentDict = {}
if inUFTier2:
    fileNames = [ n for n in listdir_uberftp(dir_path) if n.endswith(".root") ]
else:
    fileNames = [ n for n in os.listdir(dir_path) if n.endswith(".root") ]

for fileName in fileNames:
    if "SMS" in fileName: continue # New signal model ntuples in Oct18_v1
    if "ext" not in fileName:
        sampleName = fileName.replace(".root","")
    else:
        sampleName = fileName.split("_ext")[0]
    tmpDataset = Dataset(
            sampleName,
            ComponentList(
                [Component(sampleName,os.path.join(dir_path,fileName),treeName,inUFTier2,),]
                ),
            isMC = True,
            isSignal = "SMS" in fileName,
            )
    tmpDataset.setSumWeight(os.path.join(dir_path,fileName),"SumGenWeights",inUFTier2)
    if sampleName not in componentDict:
        componentDict[sampleName] = tmpDataset
    else:
        componentDict[sampleName].add(tmpDataset)
