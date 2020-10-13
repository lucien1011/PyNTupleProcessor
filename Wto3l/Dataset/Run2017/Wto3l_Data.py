from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

dataTreeDir	= "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/data2017/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2017_cmpList = ComponentList(
        [
            Component("Data_Run2017_totaldata",dataTreeDir+"total_Data_no_dupe.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2017 = Dataset(
        "Data_Run2017",
        Data_Run2017_cmpList,
        isMC = False,
        )

dataSamples_2017 = [
            Data_Run2017,
        ]

