import os
from Core.ComponentList import *
from Core.Dataset import Dataset
from DataMC.NanoAOD.CrossSection import xs_dict

fileName        = "SkimTree.root"
#common_path     = "/raid/raid7/lucien/SUSY/RPV/SkimTree/ZMuMu/2018-06-19/BkgMC_ZMuMuSelection_v1/"
common_path    = "/raid/raid7/kshi/SUSY/RPV/SkimTree/mc/ZToMuMu/"
inUFTier2       = False
#sumw_path       = "/raid/raid7/lucien/SUSY/RPV/SumGenWeight/NanoAOD_InclusiveSelection_v2/%s/EventWeight.root"
sumw_path       = "/raid/raid7/kshi/SUSY/RPV/sum_weight/%s/EventWeight.root"

sampleNames = [n for n in os.listdir(common_path) if os.path.isdir(os.path.join(common_path, n))]
allMCSamples = []
for sampleName in sampleNames:
    print(sampleName)
    tmpList = ComponentList([Component(sampleName,"/".join([common_path,sampleName,fileName]),"Events",inUFTier2,maxEvents=-1)],)
    tmpDataset = Dataset(sampleName,tmpList,xs=xs_dict[sampleName])
    tmpDataset.setSumWeight(sumw_path%sampleName)
    allMCSamples.append(tmpDataset)
