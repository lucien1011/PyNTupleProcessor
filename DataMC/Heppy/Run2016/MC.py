from DataMC.Heppy.Run2016.common import * 
from Core.Utils.UFTier2Utils import *
import os

inUFTier2   = True
treeName    = "tree"
fdTreeName  = "sf/t"
sumWeight   = "Count"
postfixs    = [
        "ext",
        "ext1",
        "ext2",
        "part1",
        "part2",
        "part3",
        ]

#componentList = []
sampleDict = {}
sampleFileNames = listdir_uberftp(bkg_dir)
sampleFdFilesNames = os.listdir(bkg_fd_dir)
for sampleFileName in sampleFileNames:
    if "evVarFriend_"+sampleFileName not in sampleFdFilesNames: continue
    if not sampleFileName.endswith(".root"): continue
    if "LO" in sampleFileName: continue
    dir_path    = bkg_dir+sampleFileName
    sampleName  = sampleFileName.replace(".root","")
    parentName  = sampleFileName.replace(".root","")
    for postfix in postfixs:
        if postfix in sampleName: parentName = parentName.replace("_"+postfix,"")
    fdFileName = "evVarFriend_"+sampleName+".root"
    cmpList = ComponentList(
            [Component(parentName,dir_path,treeName,inUFTier2,fdConfigs=[FriendTreeConfig(bkg_fd_dir+fdFileName,fdTreeName,False),])]
            #[Component(parentName,dir_path,treeName,inUFTier2,fdConfigs=[])]
            )
    tmpDataset = Dataset(parentName,cmpList,)
    tmpDataset.setSumWeightFromHeppySkimReport(skimReport_dir+sampleName+"/skimAnalyzerCount/SkimReport.txt")
    #componentList.append(tmpDataset)
    if parentName not in sampleDict:
        sampleDict[parentName] = tmpDataset
    else:
        sampleDict[parentName].add(tmpDataset)
componentList = sampleDict.values()

#for sample,dataset in sampleDict.iteritems():
#    print sample,dataset.sumw
