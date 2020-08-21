from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgSkimTreeDir      = system.getStoragePath()+"/lucien/Higgs/Zprime-NTuple/20190605/SkimTree_Zprime_Run2017Data_m4l70/"
#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/SkimTree_Run2017_MMM_MC/"
bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/unskim/SkimTree_Run2017_MMM_MC/"
bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cms/data/store/user/muahmad/rootfiles_2017/"
dataTreeDir         = bkgSkimTreeDir
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = False

# ____________________________________________________________________________________________________________________________________________ ||
# zpToMuMu
sigSampleDict = {}
zp_mass_points = [
        #1,
        #5,
        10,
        #15,
        40,
        70,
        ]# + range(20,80,10)

zpToMuMuXS_dict = {
        1: 5.715,
        5: 0.5555,
        10: 0.2173,
        15: 0.1141,
        20: 0.0650,
        25: 0.0382,
        30: 0.0226,
        35: 0.0134,
        40: 0.0079,
        45: 0.0045,
        50: 0.0025,
        55: 0.0014,
        60: 0.0007,
        65: 0.0004,
        70: 0.0002,
        }

# ____________________________________________________________________________________________________________________________________________ ||
for m in zp_mass_points:
    sigSampleDict[m] = Dataset(
        "zpToMuMu_M"+str(m),
        ComponentList([ 
            Component("zpToMuMu_M"+str(m),bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ],
        ),
        isMC                = True,
        xs                  = zpToMuMuXS_dict[m],
        isSignal            = True,
        )
    handleSumWeight(
        sigSampleDict[m],
        system,
        bkgTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.txt",
        #bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||

sigSamples = sigSampleDict.values()

