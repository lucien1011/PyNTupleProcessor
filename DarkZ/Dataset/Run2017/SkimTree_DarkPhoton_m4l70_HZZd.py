from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
from Physics.HZZd import HZZd_xs_dict
from Physics.HZZ import Higgs_prod_xs
import os

# ____________________________________________________________________________________________________________________________________________ ||
sigSkimTreeDir          = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20191201/SkimTree_DarkPhoton_Run2017Data_m4l70/"
sigTreeDir              = "/cms/data/store/user/t2/users/klo/Higgs/HToZZd/94X_MCProd_191127/"
inUFTier2               = False
sumWeightHist           = "Ana/sumWeights"
xsBoost                 = 100
epsilon                 = 0.05
saveSumWeightTxt        = False
fileNameTemplate        = "HToZZdTo4L_M125_MZd%s_eps1e-2_13TeV_madgraph_pythia8.root"
datasetName             = "HZZd_M%s"
skimTreePath            = "passedEvents"
mass_points             = [1,2,3,4,7,10,15,20,25,30,35,]

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
            xs = Higgs_prod_xs*epsilon**2*HZZd_xs_dict[m],
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
