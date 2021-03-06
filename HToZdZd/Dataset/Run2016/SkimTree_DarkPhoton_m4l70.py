from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

# ____________________________________________________________________________________________________________________________________________
# User parameters
#bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190205/SkimTree_HToZdZd_Run2016Data_m4l70/"
#bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190207/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
bkgSkimTreeDir      = system.getStoragePath()+"/"+os.environ["USER"]+"/Higgs/DarkZ-NTuple/20190218/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
bkgTreeDir          = "/cmsuf/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_4l_Feb21/"
bkgTreeDirFeb02     = "/cmsuf/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2l_Feb21/"
bkgTreeDirAug10     = "/cmsuf/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2lskim_Aug10/"
bkgTreeDirLucien    = "/cmsuf/data/store/user/t2/users/klo/Higgs/HToZdZd/BkgMC_Run2016/"
dataTreeDir         = bkgSkimTreeDir
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = False
xsBoost             = 100
epsilon             = 0.02 # not used below!
sumWeightFromT2     = False

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
ZPlusX_cmpList = ComponentList(
        [
            Component("ZPlusX",
                system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190218/SkimTree_HToZdZd_ZX_Run2016Data_m4l70_noZCandRatioCut/Data_Run2016-2l_noDuplicates_FRWeight.root",
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
# Data2016
# NTuple list
data2016_cmpList = ComponentList(
        [ 
            Component("Data2016",dataTreeDir+"Data_Run2016-03Feb2017_4l.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2016 = Dataset(
        "Data2016",
        data2016_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4tau",
                bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
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
#else:
#    ggZZTo4tau.sumw = 495800.000000
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
            Component("ggZZTo4e",
                bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
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
#else:
#    ggZZTo4e.sumw = 965000.0
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
            Component("ggZZTo4mu",
                bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
#if sumWeightFromT2:
#    ggZZTo4mu.setSumWeight(
#            bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",
#            sumWeightHist,True)
#else:
#    ggZZTo4mu.sumw = 995200.0
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
            Component("ggZZTo2mu2tau",
                bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2mu2tau = Dataset(
        "ggZZTo2mu2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
#if sumWeightFromT2:
#    ggZZTo2mu2tau.setSumWeight(
#            bkgTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",
#            sumWeightHist,True)
#else:
#    ggZZTo2mu2tau.sumw = 499800.0
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
            Component("ggZZTo2e2mu",
                bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2mu = Dataset(
        "ggZZTo2e2mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
#if sumWeightFromT2:
#    ggZZTo2e2mu.setSumWeight(
#            bkgTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",sumWeightHist,True)
#else:
#    ggZZTo2e2mu.sumw = 1386000.0
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
            Component("ggZZTo2e2tau",
                bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",
                "passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2tau = Dataset(
        "ggZZTo2e2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
#if sumWeightFromT2:
#    ggZZTo2e2tau.setSumWeight(
#            bkgTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",sumWeightHist,True)
#else:
#    ggZZTo2e2tau.sumw = 500000.0
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
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            #Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV-amcatnloFXFX-pythia8_1.root","passedEvents",inUFTier2=inUFTier2),
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
#        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8.root",
#        sumWeightHist,
#        True,
#        )
#else:
#    qqZZTo4L.sumw = 6669988.0
handleSumWeight(
        qqZZTo4L,
        system,
        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            Component("ggH",bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
#        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root",
#        sumWeightHist,
#        True,
#        )
#else:
#    ggH.sumw = 999800.0
handleSumWeight(
        ggH,
        system,
        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# VBF
VBF_cmpList = ComponentList(
        [ 
            Component("VBF",bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
#        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root",
#        sumWeightHist,
#        True,
#        )
#else:
#    VBF.sumw = 499312.0
handleSumWeight(
        VBF,
        system,
        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHplus
WHplus_cmpList = ComponentList(
        [ 
            Component("WHplus",bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
#        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root",
#        sumWeightHist,
#        True,
#        )
#else:
#    WHplus.sumw = 279824.0
handleSumWeight(
        WHplus,
        system,
        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.txt",
        bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHminus
WHminus_cmpList = ComponentList(
        [ 
            Component("WHminus",bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
#        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root",
#        sumWeightHist,
#        True,
#        )
#else:
#    WHminus.sumw = 186036.0
handleSumWeight(
        WHminus,
        system,
        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.txt",
        bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ZH
ZH_cmpList = ComponentList(
        [ 
            Component("ZH",bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
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
#        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.root",
#        sumWeightHist,
#        True,
#        )
#else:
#    ZH.sumw = 470416.0
handleSumWeight(
        ZH,
        system,
        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.txt",
        bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8.txt",
        )

## ____________________________________________________________________________________________________________________________________________ ||
#WWW_4F_cmpList = ComponentList(
#        [ 
#            Component(
#                "WWW_4F",
#                bkgSkimTreeDir+"WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#                "passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#
#WWW_4F = Dataset(
#        "WWW_4F",
#        WWW_4F_cmpList,
#        isMC                = True,
#        xs                  = 0.2086,
#        )
#WWW_4F.setSumWeight(
#        bkgTreeDirLucien+"WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#        sumWeightHist,
#        True,
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#WWZ_cmpList = ComponentList(
#        [ 
#            Component(
#                "WWZ",
#                bkgSkimTreeDir+
#                "WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#                "passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#
#WWZ = Dataset(
#        "WWZ",
#        WWZ_cmpList,
#        isMC                = True,
#        xs                  = 0.1651,
#        )
#WWZ.setSumWeight(
#        bkgTreeDirLucien+"WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#        sumWeightHist,
#        True,
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#WZZ_cmpList = ComponentList(
#        [ 
#            Component(
#                "WZZ",
#                bkgSkimTreeDir+
#                "WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#                "passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#
#WZZ = Dataset(
#        "WZZ",
#        WZZ_cmpList,
#        isMC                = True,
#        xs                  = 0.05565,
#        )
#WZZ.setSumWeight(
#        bkgTreeDirLucien+
#        "WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#        sumWeightHist,
#        True,
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#ZZZ_cmpList = ComponentList(
#        [ 
#            Component(
#                "ZZZ",
#                bkgSkimTreeDir+
#                "ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#                "passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#
#ZZZ = Dataset(
#        "ZZZ",
#        ZZZ_cmpList,
#        isMC                = True,
#        xs                  = 0.01398,
#        )
#ZZZ.setSumWeight(
#        bkgTreeDirLucien+
#        "ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16MiniAODv2.root",
#        sumWeightHist,
#        True,
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#WpWpJJ_cmpList = ComponentList(
#        [ 
#            Component(
#                "WpWpJJ",
#                bkgSkimTreeDir+
#                "WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8_RunIISummer16MiniAODv2.root",
#                "passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#
#WpWpJJ = Dataset(
#        "WpWpJJ",
#        WpWpJJ_cmpList,
#        isMC                = True,
#        xs                  = 0.03711,
#        )
#WpWpJJ.setSumWeight(
#        bkgTreeDirLucien+
#        "WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8_RunIISummer16MiniAODv2.root",
#        sumWeightHist,
#        True,
#        )
#
## ____________________________________________________________________________________________________________________________________________ ||
#WWTo2L2Nu_cmpList = ComponentList(
#        [ 
#            Component(
#                "WWTo2L2Nu",
#                bkgSkimTreeDir+
#                "WWTo2L2Nu_DoubleScattering_13TeV-pythia8_RunIISummer16MiniAODv2.root",
#                "passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#
#WWTo2L2Nu = Dataset(
#        "WWTo2L2Nu",
#        WWTo2L2Nu_cmpList,
#        isMC                = True,
#        xs                  = 0.1729,
#        )
#WWTo2L2Nu.setSumWeight(
#        bkgTreeDirLucien+
#        "WWTo2L2Nu_DoubleScattering_13TeV-pythia8_RunIISummer16MiniAODv2.root",
#        sumWeightHist,
#        True,
#        )

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
        #WWW_4F,
        #WWZ,
        #WZZ,
        #ZZZ,
        #WpWpJJ,
        #WWTo2L2Nu,
        ZPlusX,
        #DYJetsToLL_M50,
        #DYJetsToLL_M10To50,
        ]

sigSamples = [
        #HZZd_M4,
        #HZZd_M7,
        #HZZd_M10,
        #HZZd_M15,
        #HZZd_M20,
        #HZZd_M25,
        #HZZd_M30,
        #HZZd_M35,
        ]
