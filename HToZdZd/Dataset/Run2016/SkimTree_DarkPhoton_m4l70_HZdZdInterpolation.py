from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
from Physics.HZdZd import HZdZd_xs_dict
from Physics.HZZ import Higgs_prod_xs
import os

# ____________________________________________________________________________________________________________________________________________ ||
sigSkimTreeDir          = system.getStoragePath()+"/"+os.environ["USER"]+"/Higgs/DarkZ-NTuple/20191201/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
sigSkimTreeDir2         = system.getStoragePath()+"/"+os.environ["USER"]+"/Higgs/DarkZ-NTuple/20191204/SkimTree_HToZdZd_Run2016Data_m4l70_noZCandRatioCut/"
sigTreeDir              = "/cmsuf/data/store/user/t2/users/klo/Higgs/HToZdZd/80X_MCProd_191127/"
inUFTier2               = False
sumWeightHist           = "Ana/sumWeights"
kappa                   = 0.0001
saveSumWeightTxt        = False
fileNameTemplate        = "HToZdZdTo4L_M125_MZd%s_eps2e-2_kap1e-4_TuneCP5_13TeV_madgraph_pythia8.root"
datasetName             = "HToZdZd_M%s"
skimTreePath            = "passedEvents"
mass_points             = [4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60,]

# ____________________________________________________________________________________________________________________________________________ ||
sigSampleDict = {}
for m in mass_points:
    inputFilePath = os.path.join(sigSkimTreeDir,fileNameTemplate%m) if m not in [4,5,] else os.path.join(sigSkimTreeDir2,fileNameTemplate%m)
    tmpDataset = Dataset(
            datasetName%m,
            ComponentList(
                [ Component(datasetName%m,inputFilePath,skimTreePath,inUFTier2=inUFTier2) ]
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
            inputFilePath.replace(".root",".txt"),
            inputFilePath.replace(".root",".txt"),
            )
    sigSampleDict[m] = tmpDataset
sigSamples = sigSampleDict.values()
