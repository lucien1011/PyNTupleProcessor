from Core.ComponentList import *
from Core.Dataset import Dataset

mc_dir          = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Sept18_v1/"
inUFTier2       = True

# __________________________________________________________________________________________ ||
DYJetsToLL_M10to50_LO_cmpList = ComponentList(
                       [ Component(
                           "DYJetsToLL_M10to50_LO",
                           mc_dir+"DYJetsToLL_M10to50_LO.root",
                           inUFTier2),
                        ]
          )

DYJetsToLL_M10to50_LO = Dataset(
        "DYJetsToLL_M10to50_LO",
        DYJetsToLL_M10to50_LO_cmpList,
        isMC                = True,
        xs                  = 1,
        )
DYJetsToLL_M10to50_LO.setSumWeight(mc_dir+"DYJetsToLL_M10oto50_LO.root","SumGenWeights",inUFTier2)

# __________________________________________________________________________________________ ||
DYJetsToLL_M50_LO_cmpList = ComponentList(
                       [ Component(
                           "DYJetsToLL_M50_LO",
                           mc_dir+"DYJetsToLL_M50_LO_ext.root",
                           inUFTier2),
                        ]
          )

DYJetsToLL_M50_LO_ext = Dataset(
        "DYJetsToLL_M50_LO",
        DYJetsToLL_M50_LO_cmpList,
        isMC                = True,
        xs                  = 1,
        )
DYJetsToLL_M50_LO_ext.setSumWeight(mc_dir+"DYJetsToLL_M50_LO_ext.root","SumGenWeights",inUFTier2)
