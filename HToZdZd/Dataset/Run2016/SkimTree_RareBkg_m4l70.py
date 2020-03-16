from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

bkgSkimTreeDir      = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190218/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
bkgTreeDir          = "/cms/data/store/user/t2/users/klo/Higgs/HToZdZd/80X_MCProd_191127/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
sumWeightFromT2     = True
saveSumWeightTxt    = False 

# ____________________________________________________________________________________________________________________________________________ ||
# ttZ
ttZ_cmpList = ComponentList(
        [ 
            Component("ttZ",bkgSkimTreeDir+"ttZJets_13TeV_madgraphMLM.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ttZ = Dataset(
        "ttZ",
        ttZ_cmpList,
        isMC                = True,
        xs                  = 0.6529,
        )
handleSumWeight(
        ttZ,
        system,
        bkgTreeDir+"ttZJets_13TeV_madgraphMLM.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ttZJets_13TeV_madgraphMLM.txt",
        bkgSkimTreeDir+"ttZJets_13TeV_madgraphMLM.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WWZ
WWZ_cmpList = ComponentList(
        [ 
            Component("WWZ",bkgSkimTreeDir+"WWZJetsTo4L2Nu_4f_TuneCUETP8M1_13TeV_aMCatNLOFxFx_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WWZ = Dataset(
        "WWZ",
        WWZ_cmpList,
        isMC                = True,
        xs                  = 0.0005972,
        )
handleSumWeight(
        WWZ,
        system,
        bkgTreeDir+"WWZJetsTo4L2Nu_4f_TuneCUETP8M1_13TeV_aMCatNLOFxFx_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"WWZJetsTo4L2Nu_4f_TuneCUETP8M1_13TeV_aMCatNLOFxFx_pythia8.txt",
        bkgSkimTreeDir+"WWZJetsTo4L2Nu_4f_TuneCUETP8M1_13TeV_aMCatNLOFxFx_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ____________________________________________________________________________________________________________________________________________ ||
rareBkgSamples = [
        ttZ,
        WWZ,
        ]
