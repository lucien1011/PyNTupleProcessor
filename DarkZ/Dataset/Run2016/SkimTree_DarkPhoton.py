from Core.ComponentList import *
from Core.Dataset import Dataset

bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180808/SkimTree_DarkPhoton_Run2016Data_v1/"
bkgSkimTreeDir2     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180808/SkimTree_DarkPhoton_Run2016Data_v1/"
sigSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180808/SkimTree_DarkPhoton_Run2017Sig_v1/"
sigTreeDir          = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/SigMC_Run2016_v1/"
bkgTreeDir          = "/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/"
dataTreeDir         = bkgSkimTreeDir 
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
xsBoost             = 100
epsilon             = 0.03

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
ZPlusX_cmpList = ComponentList(
        [
            #Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/Data_Run2016_noDuplicates_FRWeight.root","passedEvents",False)
            #Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/Data_Run2016_noDuplicates_FRWeight_v2.root","passedEvents",False)
            #Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/Data_Run2016_noDuplicates_FRWeight_v4.root","passedEvents",False)
            Component("ZPlusX","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180820/SkimTree_DarkPhoton_ZX_Run2016Data_v1/Data_Run2016_noDuplicates_FRWeight.root","passedEvents",False)
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
data2016_cmpList = ComponentList(
        [ 
            Component("Data2016",dataTreeDir+"/Data_Run2016_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
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
            Component("ggZZTo4tau",bkgSkimTreeDir2+"GluGluToContinToZZTo4tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4tau = Dataset(
        "ggZZTo4tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4tau.setSumWeight("/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4e
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4e",bkgSkimTreeDir2+"GluGluToContinToZZTo4e/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4e = Dataset(
        "ggZZTo4e",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4e.setSumWeight("/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu",bkgSkimTreeDir2+"GluGluToContinToZZTo4mu/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4mu.setSumWeight("/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2mu2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2mu2tau",bkgSkimTreeDir2+"GluGluToContinToZZTo2mu2tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2mu2tau = Dataset(
        "ggZZTo2mu2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2mu2tau.setSumWeight("/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2mu",bkgSkimTreeDir2+"GluGluToContinToZZTo2e2mu/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2mu = Dataset(
        "ggZZTo2e2mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2e2mu.setSumWeight("/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2tau",bkgSkimTreeDir2+"GluGluToContinToZZTo2e2tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2tau = Dataset(
        "ggZZTo2e2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2e2tau.setSumWeight("/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            #Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
qqZZTo4L.setSumWeight(
        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            Component("ggH",bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggH = Dataset(
        "ggH",
        ggH_cmpList,
        isMC                = True,
        #xs                  = 0.01218,
        xs                  = 48.52*0.0002768,
        )
ggH.setSumWeight(
        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# VBF
VBF_cmpList = ComponentList(
        [ 
            Component("VBF",bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

VBF = Dataset(
        "VBF",
        VBF_cmpList,
        isMC                = True,
        xs                  = 0.001044,
        )
VBF.setSumWeight(
        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHplus
WHplus_cmpList = ComponentList(
        [ 
            Component("WHplus",bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHplus = Dataset(
        "WHplus",
        WHplus_cmpList,
        isMC                = True,
        xs                  = 0.000232,
        )
WHplus.setSumWeight(
        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHminus
WHminus_cmpList = ComponentList(
        [ 
            Component("WHminus",bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHminus = Dataset(
        "WHminus",
        WHminus_cmpList,
        isMC                = True,
        xs                  = 0.000147,
        )
WHminus.setSumWeight(
        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ZH
ZH_cmpList = ComponentList(
        [ 
            Component("ZH",bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ZH = Dataset(
        "ZH",
        ZH_cmpList,
        isMC                = True,
        xs                  = 0.000668,
        )
ZH.setSumWeight(
        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUgenV6_pythia8_RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M4
ggHZZd_M4_cmpList = ComponentList(
        [ Component("HZZd_M4",sigSkimTreeDir+"ZD_UpTo0j_MZD4_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M4 = Dataset(
        "HZZd_M4",
        ggHZZd_M4_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*0.000219, # Take Br(h->ZZd->4l from paper
        )
ggHZZd_M4.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD4_Eps1e-2_klo.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M7
ggHZZd_M7_cmpList = ComponentList(
        [ Component("HZZd_M7",sigSkimTreeDir+"ZD_UpTo0j_MZD7_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M7 = Dataset(
        "HZZd_M7",
        ggHZZd_M7_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*0.000597, # Take Br(h->ZZd->4l from paper
        )
ggHZZd_M7.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD7_Eps1e-2_klo.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M10
ggHZZd_M10_cmpList = ComponentList(
        [ Component("HZZd_M10",sigSkimTreeDir+"ZD_UpTo0j_MZD10_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M10 = Dataset(
        "HZZd_M10",
        ggHZZd_M10_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*0.00126, # Take Br(h->ZZd->4l from paper
        )
ggHZZd_M10.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M15
ggHZZd_M15_cmpList = ComponentList(
        [ Component("HZZd_M15",sigSkimTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M15 = Dataset(
        "HZZd_M15",
        ggHZZd_M15_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 3.396e-6*xsBoost, # Madgraph xs
        #xs                  = 48.58*0.288*epsilon**2*0.06729, # Assume h->ZZd br to be 100%
        xs                  = 48.58*epsilon**2*(0.00252+0.00338)/2., # Take Br(h->ZZd->4l from paper
        )
ggHZZd_M15.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD15_Eps1e-2_klo.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M20
ggHZZd_M20_cmpList = ComponentList(
        [ Component("ggHZZd_M20",sigSkimTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M20 = Dataset(
        "HZZd_M20",
        ggHZZd_M20_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 6.34e-06*xsBoost,
        #xs                  = 48.58*0.286*epsilon**2*0.06729,
        xs                  = 48.58*epsilon**2*0.00555, # Take Br(h->ZZd->4l) from paper
        )
ggHZZd_M20.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD20_Eps1e-2_klo.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M25
ggHZZd_M25_cmpList = ComponentList(
        [ Component("ggHZZd_M25",sigSkimTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M25 = Dataset(
        "HZZd_M25",
        ggHZZd_M25_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 9.956e-06*xsBoost,
        #xs                  = 48.58*0.283*epsilon**2*0.06729,
        xs                  = 48.58*epsilon**2*(0.00814+0.00940)/2., # Take Br(h->ZZd->4l from paper
        )
ggHZZd_M25.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD25_Eps1e-2_klo.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggHZZd_M30
ggHZZd_M30_cmpList = ComponentList(
        [ Component("ggHZZd_M30",sigSkimTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo_1.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ggHZZd_M30 = Dataset(
        "HZZd_M30",
        ggHZZd_M30_cmpList,
        isMC                = True,
        isSignal            = True,
        #xs                  = 1.196e-05*xsBoost,
        #xs                  = 48.58*0.280*epsilon**2*0.06729,
        xs                  = 48.58*epsilon**2*0.0108, # Take Br(h->ZZd->4l from paper
        )
ggHZZd_M30.setSumWeight(sigTreeDir+"ZD_UpTo0j_MZD30_Eps1e-2_klo.root","Ana/sumWeights",True)

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
        #data2016,
        ]

sigSamples = [
        ggHZZd_M4,
        ggHZZd_M7,
        ggHZZd_M10,
        ggHZZd_M15,
        ggHZZd_M20,
        ggHZZd_M25,
        ggHZZd_M30,
        #ggHZZd_M35,
        ]
