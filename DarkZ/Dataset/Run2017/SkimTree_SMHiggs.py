from Core.ComponentList import *
from Core.Dataset import Dataset

bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180730/SkimTree_BkgMC/SMHiggs/"
bkgTreeDir          = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180702/Tree_BkgMC/"
sigSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180619/"
sigTreeDir          = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180628/HZZNTuple/"
dataTreeDir         = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180730/SkimTree_Run2017Data/SMHiggs/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
ZPlusX_cmpList = ComponentList(
        [
            Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/Data_Run2016_noDuplicates_FRWeight.root","passedEvents",False)
            #Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/Data_Run2016_noDuplicates_FRWeight_v2.root","passedEvents",False)
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
            Component("Data2017",dataTreeDir+"/Data_Run2017.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2017 = Dataset(
        "Data2017",
        data2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4tau",bkgSkimTreeDir+"GluGluToContinToZZTo4tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4tau = Dataset(
        "ggZZTo4tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4tau.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4e
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4e",bkgSkimTreeDir+"GluGluToContinToZZTo4e/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4e = Dataset(
        "ggZZTo4e",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4e.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu",bkgSkimTreeDir+"GluGluToContinToZZTo4mu/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4mu.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2mu2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2mu2tau",bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2mu2tau = Dataset(
        "ggZZTo2mu2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2mu2tau.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2mu",bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2mu = Dataset(
        "ggZZTo2e2mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2e2mu.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2tau",bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2tau = Dataset(
        "ggZZTo2e2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2e2tau.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
qqZZTo4L.setSumWeight("/raid/raid9/ahmad/RUN2_Analyzer/v2/CMSSW_8_0_26_patch1/src/liteUFHZZ4LAnalyzer/Ntuples_Input/2017/ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root",sumWeightHist,False)

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            #Component("ggH",bkgSkimTreeDir+"GluGluHToZZ/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
            Component("ggH",bkgSkimTreeDir+"GluGluHToZZ/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("VBF",bkgSkimTreeDir+"VBF/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

VBF = Dataset(
        "VBF",
        VBF_cmpList,
        isMC                = True,
        xs                  = 0.001044,
        )
VBF.setSumWeight("/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/BkgMC_Early2017_v1/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
# WHplus
WHplus_cmpList = ComponentList(
        [ 
            Component("WHplus",bkgSkimTreeDir+"WplusH/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("WHminus",bkgSkimTreeDir+"WminusH/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("ZH",bkgSkimTreeDir+"ZH/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ZH = Dataset(
        "ZH",
        ZH_cmpList,
        isMC                = True,
        xs                  = 0.000668,
        )
ZH.setSumWeight(bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8/ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root","Ana/sumWeights",False)

## ____________________________________________________________________________________________________________________________________________ ||
## WZ
#WZ_cmpList = ComponentList(
#        [ 
#            Component("WZ",bkgSkimTreeDir+"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_1.root","passedEvents",inUFTier2=inUFTier2),
#        ]
#        )
#
#WZ = Dataset(
#        "WZ",
#        WZ_cmpList,
#        isMC                = True,
#        xs                  = 4.430,
#        )
#WZ.setSumWeight("/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/BkgMC_Early2017_v1/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root","Ana/sumWeights",True)

## ____________________________________________________________________________________________________________________________________________ ||
## ggHZZd_M15
#ggHZZd_M15_cmpList = ComponentList(
#        [ Component("ggHZZd_M15",sigSkimTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
#        )
#ggHZZd_M15 = Dataset(
#        "ggHZZd_M15",
#        ggHZZd_M15_cmpList,
#        isMC                = True,
#        isSignal            = True,
#        xs                  = 0.0000119*100,
#        #xs                  = 48.58*0.001,
#        )
#ggHZZd_M15.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root","Ana/sumWeights",False)
#
## ____________________________________________________________________________________________________________________________________________ ||
## ggHZZd_M20
#ggHZZd_M20_cmpList = ComponentList(
#        [ Component("ggHZZd_M20",sigSkimTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
#        )
#ggHZZd_M20 = Dataset(
#        "ggHZZd_M20",
#        ggHZZd_M20_cmpList,
#        isMC                = True,
#        isSignal            = True,
#        xs                  = 6.285e-06*100,
#        #xs                  = 48.58*0.001,
#        )
#ggHZZd_M20.setSumWeight("/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180628/HZZNTuple/ZD_UpTo0j_MZD20_Eps1e-2/ZD_UpTo0j_MZD20_Eps1e-2/crab_ZD_UpTo0j_MZD20_Eps1e-2_klo/180424_132813/0000/ZD_UpTo0j_MZD20_Eps1e-2_klo.root","Ana/sumWeights",False)
#
## ____________________________________________________________________________________________________________________________________________ ||
## ggHZZd_M25
#ggHZZd_M25_cmpList = ComponentList(
#        [ Component("ggHZZd_M25",sigSkimTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
#        )
#ggHZZd_M25 = Dataset(
#        "ggHZZd_M25",
#        ggHZZd_M25_cmpList,
#        isMC                = True,
#        isSignal            = True,
#        xs                  = 9.857e-06*100,
#        #xs                  = 48.58*0.001,
#        )
#ggHZZd_M25.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root","Ana/sumWeights",False)
#
## ____________________________________________________________________________________________________________________________________________ ||
## ggHZZd_M30
#ggHZZd_M30_cmpList = ComponentList(
#        [ Component("ggHZZd_M30",sigSkimTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
#        )
#ggHZZd_M30 = Dataset(
#        "ggHZZd_M30",
#        ggHZZd_M30_cmpList,
#        isMC                = True,
#        isSignal            = True,
#        xs                  = 1.190e-05*100,
#        #xs                  = 48.58*0.001,
#        )
#ggHZZd_M30.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.root","Ana/sumWeights",False)
#
## ____________________________________________________________________________________________________________________________________________ ||
## ggHZZd_M35
#ggHZZd_M35_cmpList = ComponentList(
#        [ Component("ggHZZd_M35",sigSkimTreeDir+"ZD_UpTo0j_MZD35_Eps1e-2_klo.root","passedEvents",inUFTier2=inUFTier2) ]
#        )
#ggHZZd_M35 = Dataset(
#        "ggHZZd_M35",
#        ggHZZd_M35_cmpList,
#        isMC                = True,
#        isSignal            = True,
#        xs                  = 6.285e-06*100,
#        #xs                  = 48.58*0.001,
#        )
#ggHZZd_M35.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD35_Eps1e-2_klo.root","Ana/sumWeights",False)


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

sigSamples = [
        #ggHZZd_M15,
        #ggHZZd_M20,
        #ggHZZd_M25,
        #ggHZZd_M30,
        #ggHZZd_M35,
        ]
