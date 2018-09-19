from Core.ComponentList import *
from Core.Dataset import Dataset

bkgSkimTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180808/SkimTree_DarkPhoton_Run2016Data_v1/"
bkgTreeDir          = "/cms/data/store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_4lskim_M17_Feb21/"
sumWeightHist       = "Ana/sumWeights"
inUFTier2           = False

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            #Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
            #Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=inUFTier2),
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
# ggZZTo4tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4tau","GluGluToContinToZZTo4tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4tau = Dataset(
        "ggZZTo4tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4tau.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4e
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4e","GluGluToContinToZZTo4e/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4e = Dataset(
        "ggZZTo4e",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4e.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu","GluGluToContinToZZTo4mu/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
ggZZTo4mu.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2mu2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2mu2tau","GluGluToContinToZZTo2mu2tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2mu2tau = Dataset(
        "ggZZTo2mu2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2mu2tau.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2mu","GluGluToContinToZZTo2e2mu/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2mu = Dataset(
        "ggZZTo2e2mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2e2mu.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2tau","GluGluToContinToZZTo2e2tau/HaddTree.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2tau = Dataset(
        "ggZZTo2e2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
ggZZTo2e2tau.setSumWeight(bkgTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2.root",sumWeightHist,True)

