from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2018_MMM_MC/"
#bkgSkimTreeDir      = "/cms/data/store/user/t2/users/kshi/Zprime_signal/2018/"
#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/unskim/SkimTree_Run2018_MMM_MC/"
bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20200212_Zto4l/SkimTree_Run2018_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/unskim_rmGENMomIdcut/SkimTree_Run2018_MMM_MC/"
bkgSkimTreeDir2     = bkgSkimTreeDir
bkgTreeDir          = "/cmsuf/data/store/user/t2/users/kshi/Zprime_signal/2018/"
#bkgTreeDir          = "/cms/data/store/user/t2/users/kshi/Zprime_signal/test/"
dataTreeDir         = bkgSkimTreeDir
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = False

# ____________________________________________________________________________________________________________________________________________ ||
# zpToMuMu
sigSampleDict = {}
zp_mass_points = [
        #1,
        #2,
        #3,
        #4,
        5,
        10,
        15,
        #20,
        #40,
        #70,
        90,
        ] + range(20,90,5)

zpToMuMuXS_dict = {
        1: 5.715,
        2: 2.311,
        3: 1.403,
        4: 0.7584,
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
        75: 0.0001406, 
        80: 0.0001018,
        85: 0.00008061,
        90: 0.0000666,
        }

# ____________________________________________________________________________________________________________________________________________ ||
for m in zp_mass_points:
    sigSampleDict[m] = Dataset(
        "zpToMuMu_M"+str(m),
        ComponentList([ 
            Component("zpToMuMu_M"+str(m),bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8_muahmad-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-MINIAOD.root","passedEvents",inUFTier2=inUFTier2),
        ],
        ),
        isMC                = True,
        xs                  = zpToMuMuXS_dict[m],
        isSignal            = True,
        )
    handleSumWeight(
        sigSampleDict[m],
        system,
        bkgTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8_muahmad-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-MINIAOD.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8_muahmad-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-MINIAOD.txt",
        #bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8_muahmad-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-MINIAOD.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||

sigSamples = sigSampleDict.values()

