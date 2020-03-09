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
        #bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8.txt",
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
        #bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.txt",
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
        #bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.txt",
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
        #bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
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
        #bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.txt",
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
        #bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.txt",
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
        #bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples = [
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
