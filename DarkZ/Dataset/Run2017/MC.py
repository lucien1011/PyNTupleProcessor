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
