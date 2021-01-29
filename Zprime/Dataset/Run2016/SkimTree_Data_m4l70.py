from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

dataSkimTreeDir     = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/80X_Data_DarkZNTuple/"
inUFTier2           = True

# ____________________________________________________________________________________________________________________________________________ ||
# Data2016
data2016_cmpList = ComponentList(
        [ 
            Component("Data2016",dataSkimTreeDir+"/Data_Run2016-03Feb2017_4l.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2016 = Dataset(
        "Data2016",
        data2016_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
dataSamples = [
        data2016,
        ]
