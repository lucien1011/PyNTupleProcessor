from Core.ComponentList import *
from Core.Dataset import Dataset

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
PedjaPredCR_cmpList = ComponentList(
        [
            Component("PedjaPredCR","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180924/PedjaInput_rootfiles_MC80X_2lskim_M17_Feb21/Data_ZX_Run2017-03Feb2017_slimmedZX_FRWeight.root","selectedEvents",inUFTier2=False),
        ]
        )
PedjaPredCR = Dataset(
        "PredCR",
        PedjaPredCR_cmpList,
        isMC                = True,
        isSignal            = True,
        skipWeight          = True,
        )
