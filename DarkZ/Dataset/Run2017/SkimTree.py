from Core.ComponentList import *
from Core.Dataset import Dataset

bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180425/SkimTree_v1/"
bkgSkimTreeDir2     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180702/SkimTree_BkgMC/"
bkgTreeDir          = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180702/Tree_BkgMC/"
sigSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180619/"
sigTreeDir          = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180628/HZZNTuple/"
inUFTier2           = False

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZ
ggZZ_cmpList = ComponentList(
        [ Component("ggZZ",bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2) ]
        )

ggZZ = Dataset(
        "ggZZTo4L",
        ggZZ_cmpList,
        isMC                = True,
        xs                  = 0.0011586,
        sumw                = 662635.000000,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZ_ext1-v1",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root","passedEvents",inUFTier2=inUFTier2),
            Component("qqZZ-v2",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZ = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        sumw                = 91818480.000000 + 6757228.000000,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            Component("ggH",bkgSkimTreeDir2+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("VBF",bkgSkimTreeDir2+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("WHplus",bkgSkimTreeDir2+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("WHminus",bkgSkimTreeDir2+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("ZH",bkgSkimTreeDir2+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8/ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
# ggHZZd_M15
ggHZZd_M15_cmpList = ComponentList(
        [ Component("ggHZZd_M15",sigSkimTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M15 = Dataset(
        "ggHZZd_M15",
        ggHZZd_M15_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 0.0000119*100,
        #xs                  = 48.58*0.001,
        )
ggHZZd_M15.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M20
ggHZZd_M20_cmpList = ComponentList(
        [ Component("ggHZZd_M20",sigSkimTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M20 = Dataset(
        "ggHZZd_M20",
        ggHZZd_M20_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 6.285e-06*100,
        #xs                  = 48.58*0.001,
        )
ggHZZd_M20.setSumWeight("/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180628/HZZNTuple/ZD_UpTo0j_MZD20_Eps1e-2/ZD_UpTo0j_MZD20_Eps1e-2/crab_ZD_UpTo0j_MZD20_Eps1e-2_klo/180424_132813/0000/ZD_UpTo0j_MZD20_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M25
ggHZZd_M25_cmpList = ComponentList(
        [ Component("ggHZZd_M25",sigSkimTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M25 = Dataset(
        "ggHZZd_M25",
        ggHZZd_M25_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 9.857e-06*100,
        #xs                  = 48.58*0.001,
        )
ggHZZd_M25.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M30
ggHZZd_M30_cmpList = ComponentList(
        [ Component("ggHZZd_M30",sigSkimTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M30 = Dataset(
        "ggHZZd_M30",
        ggHZZd_M30_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 1.190e-05*100,
        #xs                  = 48.58*0.001,
        )
ggHZZd_M30.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M35
ggHZZd_M35_cmpList = ComponentList(
        [ Component("ggHZZd_M35",sigSkimTreeDir+"ZD_UpTo0j_MZD35_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M35 = Dataset(
        "ggHZZd_M35",
        ggHZZd_M35_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 6.285e-06*100,
        #xs                  = 48.58*0.001,
        )
ggHZZd_M35.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD35_Eps1e-2_klo.root","Ana/sumWeights",False)


# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples = [
        ggH,
        VBF,
        WHplus,
        WHminus,
        ZH,
        ggZZ,
        qqZZ,
        ]

sigSamples = [
        ggHZZd_M15,
        ggHZZd_M20,
        ggHZZd_M25,
        ggHZZd_M30,
        #ggHZZd_M35,
        ]
