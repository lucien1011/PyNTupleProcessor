from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgSkimTreeDir2      = system.getStoragePath()+"/lucien/Higgs/Zprime-NTuple/20190605/SkimTree_Zprime_Run2016Data_m4l70/"
#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/SkimTree_Run2016_MMM_MC/"
bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2016_MMM_MC/"
#bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_4l_Feb21/"
#dataTreeDir         = bkgSkimTreeDir
dataTreeDir         = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/SkimTree_Run2016_MMM_Data/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = True

# ____________________________________________________________________________________________________________________________________________ ||
# Data2016
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
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
handleSumWeight(
        qqZZTo4L,
        system,
        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.txt",
        bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.txt",
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

# ____________________________________________________________________________________________________________________________________________ ||

# ttH
ttH_cmpList = ComponentList(
        [ 
            Component("ttH",bkgSkimTreeDir+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUgenV6_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ttH = Dataset(
        "ttH",
        ttH_cmpList,
        isMC                = True,
        xs                  = 0.000337,
        )
handleSumWeight(
        ttH,
        system,
        bkgTreeDir+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUgenV6_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        bkgSkimTreeDir+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUgenV6_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||

bkgSamples = [
        ggH,
        VBF,
        WHplus,
        WHminus,
        ZH,
        ttH,
        qqZZTo4L,
        ggZZTo2e2mu,
        ggZZTo2e2tau,
        ggZZTo2mu2tau,
        ggZZTo4e,
        ggZZTo4mu,
        ggZZTo4tau,
        ]
dataSamples = [
        data2016,
        ]
