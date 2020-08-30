from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

dataSkimTreeDir     = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/94X_Data_DarkZNTuple/"
inUFTier2           = True

# ____________________________________________________________________________________________________________________________________________ ||
# Data2017
data2017_cmpList = ComponentList(
        [ 
            Component("Data2017",dataSkimTreeDir+"/Data_Run2017-17Nov2017-v1_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2017 = Dataset(
        "Data2017",
        data2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
dataSamples = [
        data2017,
        ]
