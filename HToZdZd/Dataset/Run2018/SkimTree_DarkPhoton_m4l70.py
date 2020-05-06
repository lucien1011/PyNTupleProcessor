from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

bkgSkimTreeDir      = system.getStoragePath()+"/"+os.environ["USER"]+"/Higgs/DarkZ-NTuple/20190408/SkimTree_HToZdZd_Run2018Data_m4l70/"
bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cmsuf/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC2018_M19_Feb19_fixGENjet_bestCandLegacy/"
dataTreeDir         = bkgSkimTreeDir
zxSkimTreeDir       = system.getStoragePath()+"/"+os.environ["USER"]+"/Higgs/DarkZ-NTuple/20190408/SkimTree_HToZdZd_Run2018Data_m4l70/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
sumWeightFromT2     = False
saveSumWeightTxt    = False

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
ZPlusX_cmpList = ComponentList(
        [
            Component("ZPlusX",
                zxSkimTreeDir+"Data_Run2018_noDuplicates_FRWeightFromVukasinWZRemoved.root",
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
data2018_cmpList = ComponentList(
        [ 
            Component("Data2018",dataTreeDir+"Data_Run2018_UFHZZNTuple_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2018 = Dataset(
        "Data2018",
        data2018_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
#if sumWeightFromT2:
#    qqZZTo4L.setSumWeight(
#        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root",
#        sumWeightHist,
#        True,
#        )
handleSumWeight(
        qqZZTo4L,
        system,
        bkgTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.txt",
        bkgSkimTreeDir+"ZZTo4L_TuneCP5_13TeV_powheg_pythia8.txt",
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
#if sumWeightFromT2:
#    ggH.setSumWeight(
#        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
#        sumWeightHist,
#        True,
#        )
handleSumWeight(
        ggH,
        system,
        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
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
#if sumWeightFromT2:
#    VBF.setSumWeight(
#        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
#        sumWeightHist,
#        True,
#        )
handleSumWeight(
        VBF,
        system,
        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
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
#if sumWeightFromT2:
#    WHplus.setSumWeight(
#        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
#        sumWeightHist,
#        True,
#        )
handleSumWeight(
        WHplus,
        system,
        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
        bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
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
#if sumWeightFromT2:
#    WHminus.setSumWeight(
#        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
#        sumWeightHist,
#        True,
#        )
handleSumWeight(
        WHminus,
        system,
        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
        bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
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
#if sumWeightFromT2:
#    ZH.setSumWeight(
#        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root",
#        sumWeightHist,
#        True,
#        )
handleSumWeight(
        ZH,
        system,
        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.txt",
        bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.txt",
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
#if sumWeightFromT2:
#    ggZZTo4tau.setSumWeight(
#            bkgTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root",
#            sumWeightHist,True)
handleSumWeight(
        ggZZTo4tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.txt",
        bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.txt",
        )

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
#if sumWeightFromT2:
#    ggZZTo4e.setSumWeight(
#            bkgTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root",
#            sumWeightHist,True)
handleSumWeight(
        ggZZTo4e,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.txt",
        bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.txt",
        )

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
#if sumWeightFromT2:
#    ggZZTo4mu.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",sumWeightHist,True)
handleSumWeight(
        ggZZTo4mu,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
        bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
        )

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
#if sumWeightFromT2:
#    ggZZTo2mu2tau.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",sumWeightHist,True)
handleSumWeight(
        ggZZTo2mu2tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.txt",
        bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.txt",
        )

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
#if sumWeightFromT2:
#    ggZZTo2e2mu.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",sumWeightHist,True)
handleSumWeight(
        ggZZTo2e2mu,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.txt",
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.txt",
        )

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
#if sumWeightFromT2:
#    ggZZTo2e2tau.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",sumWeightHist,True)
handleSumWeight(
        ggZZTo2e2tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.txt",
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.txt",
        )

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
