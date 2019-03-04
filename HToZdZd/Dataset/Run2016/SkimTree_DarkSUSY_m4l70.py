from Core.ComponentList import *
from Core.Dataset import Dataset

# ____________________________________________________________________________________________________________________________________________ ||
darkSUSY_SkimTreeDir        = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190131/SkimTree_DarkSUSY_Run2016Data_m4l70/"
darkSUSY_SumWeightDir       = "/cms/data/store/user/t2/users/klo/Higgs/HToZdZd/DarkSUSY_Run2016/"
skimTreeName                = "passedEvents"
sumWeightHist               = "Ana/sumWeights"
kappa                       = 0.005

# ____________________________________________________________________________________________________________________________________________ ||
DarkSUSY_mN1_10_mGammaD_8p5_cT_0_cmpList = ComponentList(
        [
            Component(
                        "DarkSUSY_mN1_10_mGammaD_8p5_cT_0_cmpList",
                        darkSUSY_SkimTreeDir+"DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_0_13TeV-pythia8.root",
                        skimTreeName,
                        False,
                    ),
        ]
        )
DarkSUSY_mN1_10_mGammaD_8p5_cT_0 = Dataset(
            "DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_0",
            DarkSUSY_mN1_10_mGammaD_8p5_cT_0_cmpList,
            isMC = True,
            isSignal = True,
            xs = 48.58*kappa**2*108.21481671424391,
        )
DarkSUSY_mN1_10_mGammaD_8p5_cT_0.setSumWeight(
        darkSUSY_SumWeightDir+"DarkSUSY_mH_125_mN1_10_mGammaD_8p5_cT_0_13TeV-pythia8.root",
        sumWeightHist,
        True,
        )
