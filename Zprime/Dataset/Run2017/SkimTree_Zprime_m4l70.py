from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

bkgSkimTreeDir      = system.getStoragePath()+"/lucien/Higgs/Zprime-NTuple/20190510/SkimTree_Zprime_Run2017Data_m4l70/"
bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cms/data/store/user/muahmad/rootfiles_2017/"
dataTreeDir         = bkgSkimTreeDir
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = True

# ____________________________________________________________________________________________________________________________________________ ||
# zpToMuMu_M15
zpToMuMu_M15_cmpList = ComponentList(
        [ 
            Component("zpToMuMu_M15",bkgSkimTreeDir+"ZpTomumu_M15_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

zpToMuMu_M15 = Dataset(
        "zpToMuMu_M15",
        zpToMuMu_M15_cmpList,
        isMC                = True,
        xs                  = 0.1141,
        isSignal            = True,
        )
handleSumWeight(
        zpToMuMu_M15,
        system,
        bkgTreeDir+"ZpTomumu_M15_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZpTomumu_M15_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
