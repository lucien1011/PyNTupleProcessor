from DataMC.Heppy.Run2016.common import * 
from Core.Utils.UFTier2Utils import *

inUFTier2   = True
treeName    = "tree"
fdTreeName  = "sf/t"
sumWeight   = "Count"

componentList = []
sampleFileNames = listdir_uberftp(bkg_dir)
sampleFdFilesNames = listdir_uberftp(bkg_fd_dir)
for sampleFileName in sampleFileNames:
    if not sampleFileName.endswith(".root"): continue
    dir_path    = bkg_dir+sampleFileName
    sampleName  = sampleFileName.replace(".root","") 
    fdFileName = "evVarFriend_"+sampleName+".root"
    cmpList = ComponentList(
            [Component(sampleName,dir_path,treeName,inUFTier2,fdPaths=[(bkg_fd_dir+fdFileName,fdTreeName),])]
            )
    tmpDataset = Dataset(sampleName,cmpList,)
    tmpDataset.setSumWeight(dir_path,sumWeight,inUFTier2=True)
    componentList.append(tmpDataset)
