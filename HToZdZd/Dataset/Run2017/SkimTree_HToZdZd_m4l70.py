from Core.ComponentList import *
from Core.Dataset import Dataset

# ____________________________________________________________________________________________________________________________________________ ||
#HToZdZd_SkimTreeDir        = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190205/SkimTree_HToZdZd_Run2017Data_m4l70/"
HToZdZd_SkimTreeDir        = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190207/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
HToZdZd_SumWeightDir       = "/cms/data/store/user/t2/users/klo/Higgs/HToZdZd/HToZdZd_Run2017/"
skimTreeName                = "passedEvents"
sumWeightHist               = "Ana/sumWeights"
kappa                       = 0.001

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD15_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD15_cmpList",
                        HToZdZd_SkimTreeDir+"ZD_UpTo0j_MZD15_Eps1e-4.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD15 = Dataset(
            "HToZdZd_MZD15",
            HToZdZd_MZD15_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*(91.42083455037466+89.0290092250651)/2,
        )
HToZdZd_MZD15.setSumWeight(
        HToZdZd_SumWeightDir+"ZD_UpTo0j_MZD15_Eps1e-4.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD30_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD30_cmpList",
                        HToZdZd_SkimTreeDir+"ZD_UpTo0j_MZD30_Eps1e-4.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD30 = Dataset(
            "HToZdZd_MZD30",
            HToZdZd_MZD30_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*65.80376284688273,
        )
HToZdZd_MZD30.setSumWeight(
        HToZdZd_SumWeightDir+"ZD_UpTo0j_MZD30_Eps1e-4.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD50_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD50_cmpList",
                        HToZdZd_SkimTreeDir+"ZD_UpTo0j_MZD50_Eps1e-4.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD50 = Dataset(
            "HToZdZd_MZD50",
            HToZdZd_MZD50_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*28.230032946960957,
        )
HToZdZd_MZD50.setSumWeight(
        HToZdZd_SumWeightDir+"ZD_UpTo0j_MZD50_Eps1e-4.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD60_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD60_cmpList",
                        HToZdZd_SkimTreeDir+"ZD_UpTo0j_MZD60_Eps1e-4.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD60 = Dataset(
            "HToZdZd_MZD60",
            HToZdZd_MZD60_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*10.079694787684147,
        )
HToZdZd_MZD60.setSumWeight(
        HToZdZd_SumWeightDir+"ZD_UpTo0j_MZD60_Eps1e-4.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
