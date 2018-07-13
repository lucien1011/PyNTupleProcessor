from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents
from Core.Utils.UFTier2Utils import *
import os

common_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
fileName    = "treeProducerSusyRA5.root"
inUFTier2   = True
treeName    = "tree"
sumWeight   = "SumGenWeights"
postfixs    = [
        "ext1",
        "ext2",
        "ext",
        "part1",
        "part2",
        "part3",
        ]

#componentList = []
sampleDict = {}
sampleFileNames = listdir_uberftp(common_path,selection=lambda x: "acosta" in x)
for sampleName in sampleFileNames:
    if "TT_pow" in sampleName: continue
    parentName = sampleName
    for postfix in postfixs:
        if postfix in sampleName: parentName = parentName.replace("_"+postfix,"")
    filePath = os.path.join(common_path,sampleName,fileName)
    cmpList = ComponentList(
            [Component(parentName,filePath,treeName,inUFTier2,)]
            )
    tmpDataset = Dataset(parentName,cmpList,)
    tmpDataset.setSumWeight(filePath,sumWeight,inUFTier2)
    #componentList.append(tmpDataset)
    if parentName not in sampleDict:
        sampleDict[parentName] = tmpDataset
    else:
        sampleDict[parentName].add(tmpDataset)
componentList = sampleDict.values()

#print sampleFileNames 
#for component in componentList:
#    print component.name
#    print component.sumw
