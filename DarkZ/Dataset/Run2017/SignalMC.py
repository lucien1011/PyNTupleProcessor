from Core.ComponentList import *
from Core.Dataset import Dataset

baseDir         = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180706/"
inUFTier2       = False
treeName        = "Ana/passedEvents"
sumWeightHist   = "Ana/sumWeights"
xsBoost         = 25

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M15
filePath_M15 = baseDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root"
cmpList_M15 = [ Component("ggHZZd_M15",filePath_M15,treeName,inUFTier2=inUFTier2) ]

ggHZZd_M15 = Dataset(
        "ggHZZd_M15",
        cmpList_M15,
        isMC                = True,
        isSignal            = True,
        xs                  = 3.396e-6*xsBoost,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 15",
        )
ggHZZd_M15.setSumWeight(filePath_M15,sumWeightHist,inUFTier2)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M20
filePath_M20 = baseDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.root"
cmpList_M20 = [ Component("ggHZZd_M20",filePath_M20,treeName,inUFTier2=inUFTier2) ]

ggHZZd_M20 = Dataset(
        "ggHZZd_M20",
        cmpList_M20,
        isMC                = True,
        isSignal            = True,
        xs                  = 6.34e-06*xsBoost,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 20",
        )
ggHZZd_M20.setSumWeight(filePath_M20,sumWeightHist,inUFTier2)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M25
filePath_M25 = baseDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root"
cmpList_M25 = [ Component("ggHZZd_M25",filePath_M25,treeName,inUFTier2=inUFTier2) ]

ggHZZd_M25 = Dataset(
        "ggHZZd_M25",
        cmpList_M25,
        isMC                = True,
        isSignal            = True,
        xs                  = 9.956e-06*xsBoost,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 25",
        )
ggHZZd_M25.setSumWeight(filePath_M25,sumWeightHist,inUFTier2)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M30
filePath_M30 = baseDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.root"
cmpList_M30 = [ Component("ggHZZd_M30",filePath_M30,treeName,inUFTier2=inUFTier2) ]

ggHZZd_M30 = Dataset(
        "ggHZZd_M30",
        cmpList_M30,
        isMC                = True,
        isSignal            = True,
        xs                  = 1.196e-05*xsBoost,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 30",
        )
ggHZZd_M30.setSumWeight(filePath_M30,sumWeightHist,inUFTier2)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M35
filePath_M35 = baseDir+"ZD_UpTo0j_MZD35_Eps1e-2_klo.root"
cmpList_M35 = [ Component("ggHZZd_M35",filePath_M35,treeName,inUFTier2=inUFTier2) ]

ggHZZd_M35 = Dataset(
        "ggHZZd_M35",
        cmpList_M35,
        isMC                = True,
        isSignal            = True,
        xs                  = 6.285e-06*100,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 35",
        )
ggHZZd_M35.setSumWeight(filePath_M35,sumWeightHist,inUFTier2)

sigSamples = [
        ggHZZd_M15,
        ggHZZd_M20,
        ggHZZd_M25,
        ggHZZd_M30,
        ggHZZd_M35,
        ]
