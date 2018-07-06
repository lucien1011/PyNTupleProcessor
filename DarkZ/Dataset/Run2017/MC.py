from Core.ComponentList import *
from Core.Dataset import Dataset

sigTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180628/HZZNTuple/"
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
        xs                  = 0.01218,
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
        xs                  = 0.01218,
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
        xs                  = 0.01218,
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
        xs                  = 0.01218,
        )
ZH.setSumWeight(bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8/ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root","Ana/sumWeights",False)

bkgSamples = [
        ggH,
        VBF,
        WHplus,
        WHminus,
        #ZH,
        ]

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M15

sigTreeDirV2 = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180702/BkgMC_Run2017/"
sigTreeDirV3 = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180706/"

ggHZZd_M15_cmpList = ComponentList(
        [ Component("ggHZZd_M15",sigTreeDirV2+"ZD_UpTo0j_MZD15_Eps1e-2_klo/ZD_UpTo0j_MZD15_Eps1e-2_klo.root","Ana/passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M15 = Dataset(
        "ggHZZd_M15",
        ggHZZd_M15_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 0.0000119*100,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 15",
        )
ggHZZd_M15.setSumWeight(sigTreeDirV2+"ZD_UpTo0j_MZD15_Eps1e-2_klo/ZD_UpTo0j_MZD15_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M20
ggHZZd_M20_cmpList = ComponentList(
        [ Component("ggHZZd_M20",sigTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.root","Ana/passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M20 = Dataset(
        "ggHZZd_M20",
        ggHZZd_M20_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 6.285e-06*100,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 20",
        )
ggHZZd_M20.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M25
ggHZZd_M25_cmpList = ComponentList(
        [ Component("ggHZZd_M25",sigTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root","Ana/passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M25 = Dataset(
        "ggHZZd_M25",
        ggHZZd_M25_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 9.857e-06*100,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 25",
        )
ggHZZd_M25.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M30
ggHZZd_M30_cmpList = ComponentList(
        [ Component("ggHZZd_M30",sigTreeDirV3+"ZD_UpTo0j_MZD30_Eps1e-2_klo/ZD_UpTo0j_MZD30_Eps1e-2_klo.root","Ana/passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M30 = Dataset(
        "ggHZZd_M30",
        ggHZZd_M30_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 1.190e-05*100,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 30",
        )
ggHZZd_M30.setSumWeight(sigTreeDirV3+"ZD_UpTo0j_MZD30_Eps1e-2_klo/ZD_UpTo0j_MZD30_Eps1e-2_klo.root","Ana/sumWeights",False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M35
ggHZZd_M35_cmpList = ComponentList(
        [ Component("ggHZZd_M35",sigTreeDir+"ZD_UpTo0j_MZD35_Eps1e-2_klo.root","Ana/passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M35 = Dataset(
        "ggHZZd_M35",
        ggHZZd_M35_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 6.285e-06*100,
        #xs                  = 48.58*0.001,
        plotLabel           = "mZd = 35",
        )
ggHZZd_M35.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD35_Eps1e-2_klo.root","Ana/sumWeights",False)

sigSamples = [
        #ggHZZd_M15,
        #ggHZZd_M20,
        #ggHZZd_M25,
        ggHZZd_M30,
        #ggHZZd_M35,
        ]
