from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

# ____________________________________________________________________________________________________________________________________________ ||
#HToZdZd_SkimTreeDir        = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190205/SkimTree_HToZdZd_Run2017Data_m4l70/"
#HToZdZd_SkimTreeDir        = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190207/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
#HToZdZd_SkimTreeDir        = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190218/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
HToZdZd_SkimTreeDir        = system.getStoragePath()+"/rosedj1/Higgs/DarkZ-NTuple/20190227/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/" # correct
HToZdZd_SumWeightDir       = "/cms/data/store/user/t2/users/rosedj1/Higgs/HToZdZd/HToZdZd_NTuple/" # correct
#HToZdZd_SumWeightDir       = "/cms/data/store/user/t2/users/klo/Higgs/HToZdZd/HToZdZd_Run2017/"
skimTreeName                = "passedEvents"
sumWeightHist               = "Ana/sumWeights"
kappa                       = 0.001
saveSumWeightTxt            = True

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD4_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD4_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD4.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD4 = Dataset(
            "HToZdZd_MZD4",
            HToZdZd_MZD4_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*139.6979988681,
        )
handleSumWeight(
        HToZdZd_MZD4,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD4.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD4.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD5_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD5_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD5.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD5 = Dataset(
            "HToZdZd_MZD5",
            HToZdZd_MZD5_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*116.344056810798,
        )
handleSumWeight(
        HToZdZd_MZD5,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD5.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD5.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD6_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD6_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD6.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD6 = Dataset(
            "HToZdZd_MZD6",
            HToZdZd_MZD6_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*114.597532012221,
        )
handleSumWeight(
        HToZdZd_MZD6,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD6.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD6.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD7_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD7_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD7.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD7 = Dataset(
            "HToZdZd_MZD7",
            HToZdZd_MZD7_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*104.179322296929,
        )
handleSumWeight(
        HToZdZd_MZD7,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD7.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD7.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD8_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD8_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD8.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD8 = Dataset(
            "HToZdZd_MZD8",
            HToZdZd_MZD8_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*104.468186168107,
        )
handleSumWeight(
        HToZdZd_MZD8,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD9_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD9_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD9.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD9 = Dataset(
            "HToZdZd_MZD9",
            HToZdZd_MZD9_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*103.60243300267,
        )
handleSumWeight(
        HToZdZd_MZD9,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD9.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD9.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD10_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD10_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD10.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD10 = Dataset(
            "HToZdZd_MZD10",
            HToZdZd_MZD10_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*102.438053362877,
        )
handleSumWeight(
        HToZdZd_MZD10,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD10.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD10.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD15_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD15_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD15.root",
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
            xs = 48.58*kappa**2*90.2249218877198,
        )
handleSumWeight(
        HToZdZd_MZD15,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD15.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD15.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD20_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD20_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD20.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD20 = Dataset(
            "HToZdZd_MZD20",
            HToZdZd_MZD20_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*83.4164181430647,
        )
handleSumWeight(
        HToZdZd_MZD20,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD20.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD20.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD25_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD25_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD25.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD25 = Dataset(
            "HToZdZd_MZD25",
            HToZdZd_MZD25_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*75.0753462796701,
        )
handleSumWeight(
        HToZdZd_MZD25,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD25.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD25.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD30_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD30_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD30.root",
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
            xs = 48.58*kappa**2*65.8037628468827,
        )
handleSumWeight(
        HToZdZd_MZD30,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD30.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD30.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD35_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD35_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD35.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD35 = Dataset(
            "HToZdZd_MZD35",
            HToZdZd_MZD35_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*56.0744652388090,
        )
handleSumWeight(
        HToZdZd_MZD35,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD35.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD35.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD40_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD40_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD40.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD40 = Dataset(
            "HToZdZd_MZD40",
            HToZdZd_MZD40_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*46.378435893888,
        )
handleSumWeight(
        HToZdZd_MZD40,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD40.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD40.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD45_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD45_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD45.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD45 = Dataset(
            "HToZdZd_MZD45",
            HToZdZd_MZD45_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*37.0703510401361,
        )
handleSumWeight(
        HToZdZd_MZD45,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD45.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD45.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD50_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD50_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD50.root",
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
            xs = 48.58*kappa**2*28.2300329469609,
        )
handleSumWeight(
        HToZdZd_MZD50,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD50.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD50.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD55_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD55_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD55.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
HToZdZd_MZD55 = Dataset(
            "HToZdZd_MZD55",
            HToZdZd_MZD55_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*19.6174575765711,
        )
handleSumWeight(
        HToZdZd_MZD55,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD55.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD55.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
HToZdZd_MZD60_cmpList = ComponentList(
        [
            Component(
                        "HToZdZd_MZD60_cmpList",
                        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD60.root",
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
handleSumWeight(
        HToZdZd_MZD60,
        system,
        HToZdZd_SumWeightDir+"HToZdZd_UpTo0j_Eps1e-2_MZD60.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        HToZdZd_SkimTreeDir+"HToZdZd_UpTo0j_Eps1e-2_MZD60.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
sigSamples2017 = [
        HToZdZd_MZD4,
        HToZdZd_MZD5,
        HToZdZd_MZD6,
        HToZdZd_MZD7,
        HToZdZd_MZD8,
        HToZdZd_MZD9,
        HToZdZd_MZD10,
        HToZdZd_MZD15,
        HToZdZd_MZD20,
        HToZdZd_MZD25,
        HToZdZd_MZD30,
        HToZdZd_MZD35,
        HToZdZd_MZD40,
        HToZdZd_MZD45,
        HToZdZd_MZD50,
        HToZdZd_MZD55,
        HToZdZd_MZD60,
        ]
