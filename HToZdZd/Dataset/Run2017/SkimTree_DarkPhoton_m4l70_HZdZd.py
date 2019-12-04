from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
from Physics.HZdZd import HZdZd_xs_dict
from Physics.HZZ import Higgs_prod_xs
import os

# ____________________________________________________________________________________________________________________________________________ ||
sigSkimTreeDir          = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20191201/SkimTree_HToZdZd_Run2017Data_m4l70_noZCandRatioCut/"
sigTreeDir              = "/cms/data/store/user/t2/users/klo/Higgs/HToZdZd/94X_MCProd_191127/"
inUFTier2               = False
sumWeightHist           = "Ana/sumWeights"
kappa                   = 0.0001
saveSumWeightTxt        = False
fileNameTemplate        = "HToZdZdTo4L_M125_MZd%s_eps2e-2_kap1e-4_TuneCP5_13TeV_madgraph_pythia8.root"
datasetName             = "HToZdZd_M%s"
skimTreePath            = "passedEvents"
#mass_points             = [4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60,]
mass_points             = [4,5,6,7,8,9,15,20,25,30,35,40,45,50,55,60,]

# ____________________________________________________________________________________________________________________________________________ ||
sigSampleDict = {}
for m in mass_points:
    tmpDataset = Dataset(
            datasetName%m,
            ComponentList(
                [ Component(datasetName%m,os.path.join(sigSkimTreeDir,fileNameTemplate%m),skimTreePath,inUFTier2=inUFTier2) ]
                ),
            isMC = True,
            isSignal = True,
            xs = Higgs_prod_xs*kappa**2*HZdZd_xs_dict[m],
            )
    handleSumWeight(
            tmpDataset,
            system,
            os.path.join(sigTreeDir,fileNameTemplate%m),
            sumWeightHist,
            True,
            saveSumWeightTxt,
            os.path.join(sigSkimTreeDir,(fileNameTemplate%m).replace(".root",".txt")),
            )
    sigSampleDict[m] = tmpDataset
sigSamples = sigSampleDict.values()
