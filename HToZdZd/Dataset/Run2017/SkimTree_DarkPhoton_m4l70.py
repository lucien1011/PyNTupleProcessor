from Core.ComponentList import *
from Core.Dataset import Dataset

bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190218/SkimTree_HToZdZd_Run2017Data_m4l70_noZCandRatioCut/"
bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/BkgMC_Run2017/"
dataTreeDir         = bkgSkimTreeDir
zxSkimTreeDir       = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190218/SkimTree_HToZdZd_ZX_Run2017Data_m4l70_noZCandRatioCut/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
sumWeightFromT2     = True

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
ZPlusX_cmpList = ComponentList(
        [
            Component("ZPlusX",
                zxSkimTreeDir+"Data_Run2017-17Nov2017_noDuplicates_FRWeight.root",
                "passedEvents",False)
        ]
        )
ZPlusX = Dataset(
        "ZPlusX",
        ZPlusX_cmpList,
        isMC                = True,
        skipWeight          = True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# Data2017
data2017_cmpList = ComponentList(
        [ 
            Component("Data2017",dataTreeDir+"Data_Run2017-17Nov2017-v1_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2017 = Dataset(
        "Data2017",
        data2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
if sumWeightFromT2:
    qqZZTo4L.setSumWeight(
        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            Component("ggH",bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggH = Dataset(
        "ggH",
        ggH_cmpList,
        isMC                = True,
        #xs                  = 0.01218,
        xs                  = 48.52*0.0002768,
        )
if sumWeightFromT2:
    ggH.setSumWeight(
        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# VBF
VBF_cmpList = ComponentList(
        [ 
            Component("VBF",bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

VBF = Dataset(
        "VBF",
        VBF_cmpList,
        isMC                = True,
        xs                  = 0.001044,
        )
if sumWeightFromT2:
    VBF.setSumWeight(
        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHplus
WHplus_cmpList = ComponentList(
        [ 
            Component("WHplus",bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHplus = Dataset(
        "WHplus",
        WHplus_cmpList,
        isMC                = True,
        xs                  = 0.000232,
        )
if sumWeightFromT2:
    WHplus.setSumWeight(
        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHminus
WHminus_cmpList = ComponentList(
        [ 
            Component("WHminus",bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHminus = Dataset(
        "WHminus",
        WHminus_cmpList,
        isMC                = True,
        xs                  = 0.000147,
        )
if sumWeightFromT2:
    WHminus.setSumWeight(
        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ZH
ZH_cmpList = ComponentList(
        [ 
            Component("ZH",bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ZH = Dataset(
        "ZH",
        ZH_cmpList,
        isMC                = True,
        xs                  = 0.000668,
        )
if sumWeightFromT2:
    ZH.setSumWeight(
        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4tau",bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4tau = Dataset(
        "ggZZTo4tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
if sumWeightFromT2:
    ggZZTo4tau.setSumWeight(
            bkgTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root",
            sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4e
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4e",bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4e = Dataset(
        "ggZZTo4e",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
if sumWeightFromT2:
    ggZZTo4e.setSumWeight(
            bkgTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root",
            sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu",bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
if sumWeightFromT2:
    ggZZTo4mu.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2mu2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2mu2tau",bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2mu2tau = Dataset(
        "ggZZTo2mu2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
if sumWeightFromT2:
    ggZZTo2mu2tau.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2mu",bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2mu = Dataset(
        "ggZZTo2e2mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
if sumWeightFromT2:
    ggZZTo2e2mu.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2tau",bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2tau = Dataset(
        "ggZZTo2e2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
if sumWeightFromT2:
    ggZZTo2e2tau.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples = [
        ggH,
        VBF,
        WHplus,
        WHminus,
        ZH,
        qqZZTo4L,
        ggZZTo2e2mu,
        ggZZTo2e2tau,
        ggZZTo2mu2tau,
        ggZZTo4e,
        ggZZTo4mu,
        ggZZTo4tau,
        ZPlusX,
        ]
