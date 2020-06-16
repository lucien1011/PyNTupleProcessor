from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os,glob

# ____________________________________________________________________________________________________________________________________________ ||
inputDir = "/cmsuf/data/store/user/t2/users/klo/CSC/"
sampleDict = {}
for f in glob.glob(inputDir+"*.root"):
    datasetName = os.path.basename(f).replace(".root","")
    sampleDict[datasetName] = Dataset(
            datasetName,
            ComponentList(
                [ 
                    Component(datasetName,f,"cscRootMaker/Events",inUFTier2=False),
                ]
            ),
            isMC = False,
            )
