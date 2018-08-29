from DarkZ.Dataset.Run2017.BkgMC import *
#from DarkZ.Dataset.Run2017.Data import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
import copy,os

inputDir = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180728/"

for sample in bkgSamples+sigSamples:
    sample.componentList = ComponentList(
            [
                Component(sample.name,os.path.join(inputDir,sample.name,"SkimTree.root"),"passedEvents",inUFTier2=False)
            ]
            )

data2017_cmpList = ComponentList(
        [ 
            Component("Data2017",
                "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180729/SkimTreeData_NoDuplicate/SkimTree.root",
                "Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2017 = Dataset(
        "Data2017",
        data2017_cmpList,
        isMC                = False,
        )
