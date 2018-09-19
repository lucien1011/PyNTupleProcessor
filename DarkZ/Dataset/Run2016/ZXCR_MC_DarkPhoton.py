from Core.ComponentList import *
from Core.Dataset import Dataset

#bkgTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_MC80X_ZXCRSelection/"
#bkgTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_MC80X_HIG-16-041-ZXCRSelection_v2/"
bkgTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
predCR_cmpList = ComponentList(
        [
            #Component("PredCR","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/Data_Run2016_noDuplicates_FRWeight_v5.root","passedEvents",False),
            Component("PredCR","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180823/SkimTree_Data80X_HIG-16-041-ZXCRSelectionWithFlag_v3_liteHZZAna/Data_Run2016_noDuplicates_1_FRWeight.root","passedEvents",False),
        ]
        )
predCR = Dataset(
        "PredCR",
        predCR_cmpList,
        isMC                = True,
        isSignal            = True,
        skipWeight          = True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M50",bkgTreeDir+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        DYJetsToLL_M50_cmpList,
        isMC = True,
        xs = 6104, 
        )
DYJetsToLL_M50.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_2lskim_M17_Mar11/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M10To50",bkgTreeDir+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M10To50 = Dataset(
        "DYJetsToLL_M10To50",
        DYJetsToLL_M10To50_cmpList,
        isMC = True,
        xs = 6104, 
        )
DYJetsToLL_M10To50.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_2lskim_M17_Mar11/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
TTJets_cmpList = ComponentList(
        [
            Component("TTJets",bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets = Dataset(
        "TTJets",
        TTJets_cmpList,
        isMC = True,
        xs = 87.31, 
        )
TTJets.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_2lskim_M17_Feb21/TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2.root","Ana/sumWeights",True)

# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_cmpList = ComponentList(
        [
            Component("WZTo3LNu",bkgTreeDir+"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WZTo3LNu = Dataset(
        "WZTo3LNu",
        WZTo3LNu_cmpList,
        isMC = True,
        xs = 0.04430, 
        )
WZTo3LNu.setSumWeight("/cms/data/store/user/t2/users/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_MC80X_2lskim_M17_Feb21/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16MiniAODv2.root","Ana/sumWeights",True)

