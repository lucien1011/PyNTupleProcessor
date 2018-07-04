from Core.ComponentList import *
from Core.Dataset import Dataset

bkgTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180702/Tree_BkgMC/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
            Component("ggH",bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggH = Dataset(
        "ggH",
        ggH_cmpList,
        isMC                = True,
        xs                  = 0.01218,
        )
ggH.setSumWeight(bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","Ana/sumWeights",False)
