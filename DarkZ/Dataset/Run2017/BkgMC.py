from Core.ComponentList import *
from Core.Dataset import Dataset

bkgTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180702/Tree_BkgMC/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            Component("ggH",bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggH = Dataset(
        "ggH",
        ggH_cmpList,
        isMC                = True,
        xs                  = 0.01218,
        )
ggH.setSumWeight(bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# VBF
VBF_cmpList = ComponentList(
        [ 
            Component("VBF",bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

VBF = Dataset(
        "VBF",
        VBF_cmpList,
        isMC                = True,
        xs                  = 0.001044,
        )
VBF.setSumWeight(bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# WHplus
WHplus_cmpList = ComponentList(
        [ 
            Component("WHplus",bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHplus = Dataset(
        "WHplus",
        WHplus_cmpList,
        isMC                = True,
        xs                  = 0.000232,
        )
WHplus.setSumWeight(bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# WHminus
WHminus_cmpList = ComponentList(
        [ 
            Component("WHminus",bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHminus = Dataset(
        "WHminus",
        WHminus_cmpList,
        isMC                = True,
        xs                  = 0.000147,
        )
WHminus.setSumWeight(bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ZH
ZH_cmpList = ComponentList(
        [ 
            Component("ZH",bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8/ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root","Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

ZH = Dataset(
        "ZH",
        ZH_cmpList,
        isMC                = True,
        xs                  = 0.000668,
        )
ZH.setSumWeight(bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8/ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# 
ggToZZ_cmpList = ComponentList(
        [ 
            Component("ggToZZ",
                "/raid/raid9/ahmad/RUN2_Analyzer/v2/CMSSW_8_0_26_patch1/src/liteUFHZZ4LAnalyzer/Ntuples_Input/2017/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root","Ana/passedEvents",inUFTier2=False),
        ]
        )

ggToZZ = Dataset(
        "ggToZZ",
        ggToZZ_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggToZZ.setSumWeight("/raid/raid9/ahmad/RUN2_Analyzer/v2/CMSSW_8_0_26_patch1/src/liteUFHZZ4LAnalyzer/Ntuples_Input/2017/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# 
qqToZZ_cmpList = ComponentList(
        [ 
            Component("qqToZZ","/raid/raid9/ahmad/RUN2_Analyzer/v2/CMSSW_8_0_26_patch1/src/liteUFHZZ4LAnalyzer/Ntuples_Input/2017/ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root" ,"Ana/passedEvents",inUFTier2=False),
        ]
        )

qqToZZ = Dataset(
        "qqToZZ",
        qqToZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
qqToZZ.setSumWeight("/raid/raid9/ahmad/RUN2_Analyzer/v2/CMSSW_8_0_26_patch1/src/liteUFHZZ4LAnalyzer/Ntuples_Input/2017/ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root","Ana/sumWeights",False)


bkgSamples = [
        ggH,
        VBF,
        WHplus,
        WHminus,
        ZH,
        #ggToZZ,
        #qqToZZ,
        ]
