import os
from Core.ComponentList import *
from Core.Dataset import Dataset
from DataMC.NanoAOD.CrossSection import xs_dict

fileName        = "SkimTree.root"
common_path     = "/raid/raid7/lucien/SUSY/RPV/SkimTree/StopToBLep/2018-05-18/BkgMC_BaselineSelection_v1/"
inUFTier2       = False
sumw_path       = "/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/%s/EventWeight.root"

sampleNames = [n for n in os.listdir(common_path) if os.path.isdir(os.path.join(common_path, n))]
allMCSamples = []
for sampleName in sampleNames:
    tmpList = ComponentList([Component(sampleName,"/".join([common_path,sampleName,fileName]),"Events",inUFTier2,maxEvents=-1)],)
    tmpDataset = Dataset(sampleName,tmpList,xs_dict[sampleName])
    tmpDataset.setSumWeight(sumw_path%sampleName)
    allMCSamples.append(tmpDataset)
