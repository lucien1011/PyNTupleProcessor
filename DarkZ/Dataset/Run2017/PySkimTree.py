from DarkZ.Dataset.Run2017.BkgMC import *
from DarkZ.Dataset.Run2017.Data import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
import copy,os

inputDir = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180728/"

for sample in bkgSamples+sigSamples+[data2017]:
    sample.componentList = ComponentList(
            [
                Component(sample.name,os.path.join(inputDir,sample.name,"SkimTree.root"),"passedEvents",inUFTier2=False)
            ]
            )
