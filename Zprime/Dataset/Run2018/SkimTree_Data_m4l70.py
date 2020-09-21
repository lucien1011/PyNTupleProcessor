from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

dataSkimTreeDir     = "/cmsuf/data/store/user/t2/users/klo/Zprime/EXO-18-008/102X_Data_DarkZNTuple/"
inUFTier2           = True

# ____________________________________________________________________________________________________________________________________________ ||
# Data2018
data2018_cmpList = ComponentList(
        [ 
            Component("Data2018",dataSkimTreeDir+"/Data_Run2018-17Sep2018_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2018 = Dataset(
        "Data2018",
        data2018_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
dataSamples = [
        data2018,
        ]
