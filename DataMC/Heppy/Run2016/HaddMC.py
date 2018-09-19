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
dataSamples = [
        "MuonEG",
        "DoubleEG",
        "DoubleMuon",
        "SingleMuon",
        "SingleElectron",
        "Tau",
        ]

#componentList = []
sampleDict = {}
sampleFileNames = listdir_uberftp(common_path,selection=lambda x: True)
for sampleName in sampleFileNames:
    if "TT_pow" in sampleName: continue
    if any([dataSample in sampleName for dataSample in dataSamples]): continue
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

# Exceptionally handling TT Powheg sample
TT_pow_comps = makeComponents("TT_pow","/cms/data/store/user/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/TT_pow/180712_162135/0000/",treeName,inUFTier2)
TT_pow = Dataset("TT_pow",ComponentList([]),xs=1.)
TT_pow.sumw = 0.
for comp in TT_pow_comps:
    temp_comp_list = ComponentList([comp])
    tmpDataset = Dataset("TT_pow",temp_comp_list,xs=1.)
    tmpDataset.setSumWeight(comp.path,sumWeight,inUFTier2)
    TT_pow.add(tmpDataset)

TT_pow_ext3_comps = makeComponents("TT_pow","/cms/data/store/user/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/TT_pow/180712_162135/0000/",treeName,inUFTier2)
TT_pow_ext3 = Dataset("TT_pow_ext3",ComponentList([]),xs=1.)
TT_pow_ext3.sumw = 0.
for comp in TT_pow_ext3_comps:
    temp_comp_list = ComponentList([comp])
    tmpDataset = Dataset("TT_pow_ext3",temp_comp_list,xs=1.)
    tmpDataset.setSumWeight(comp.path,sumWeight,inUFTier2)
    TT_pow_ext3.add(tmpDataset)
TT_pow.add(TT_pow_ext3)

componentList = sampleDict.values() + [TT_pow]

#print sampleFileNames 
#for component in componentList:
#    print component.name
#    print component.sumw
