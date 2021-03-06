from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

# ____________________________________________________________________________________________________________________________________________ ||
# 
HToZaTo2l2g_M1 = Dataset(
        "HToZaTo2l2g_M1",
        ComponentList(
            [ 
                #Component("HToZaTo2l2g_M1","/Users/lucien/CMS/DelphesAnalysis/HToZaTo2l2g/Data/2020-06-02_MuonTreeProducer_combined.root","LiteTree",inUFTier2=False),
                Component("HToZaTo2l2g_M1","/cmsuf/data/store/user/t2/users/klo/Delphes/ALP_HToZaTo2l2g_M1/2020-06-02/MuonTreeProducer/2020-06-02_MuonTreeProducer_combined.root","LiteTree",inUFTier2=False),
            ]
        ),
        isMC                = True,
        xs                  = 1,
        )
HToZaTo2l2g_M1.sumw = 4995000.
