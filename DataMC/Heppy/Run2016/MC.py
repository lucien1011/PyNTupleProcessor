from DataMC.Heppy.Run2016.common import * 
from Core.Utils.UFTier2Utils import *

inUFTier2   = True
treeName    = "tree"

componentList = []
sampleFileNames = listdir_uberftp(bkg_dir)
for sampleFileName in sampleFileNames:
    if not sampleFileName.endswith(".root"): continue
    dir_path    = bkg_dir+sampleFileName
    sampleName  = sampleFileName.replace(".root","")
    cmpList = ComponentList(
            [Component(sampleName,dir_path,treeName,inUFTier2)]
            )
    tmpDataset = Dataset(sampleName,cmpList,)
    componentList.append(tmpDataset)
