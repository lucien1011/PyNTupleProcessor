from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.UFTier2Utils import listdir_uberftp
import os
from Physics.SMS_XS import xs_dict

dir_path        = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/Oct18_v1/"
inUFTier2       = False
treeName        = "tree"

componentDict = {}
if inUFTier2:
    fileNames = [ n for n in listdir_uberftp(dir_path) if n.endswith(".root") ]
else:
    fileNames = [ n for n in os.listdir(dir_path) if n.endswith(".root") ]

for fileName in fileNames:
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
            xs = xs_dict[sampleName].value if sampleName in xs_dict else None,
            )
    tmpDataset.setSumWeight(os.path.join(dir_path,fileName),"SumGenWeights",inUFTier2)
    if sampleName not in componentDict:
        componentDict[sampleName] = tmpDataset
    else:
        componentDict[sampleName].add(tmpDataset)

sigComponentDict = componentDict
sigComponentList_plot = [
        sigComponentDict["SMS-T1qqqqL_2500"],
        sigComponentDict["SMS-T1qqqqL_2000"],
        sigComponentDict["SMS-T1qqqqL_1500"],

        sigComponentDict["SMS-T1tbs_1000"],
        sigComponentDict["SMS-T1tbs_1500"],
        ]
