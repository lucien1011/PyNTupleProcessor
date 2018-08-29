from Core.ComponentList import *
from Core.Dataset import Dataset

pathApr16       = "/cms/data/store/user/t2/users/dsperka/Run2/Zprime/2017/rootfiles_Data_Apr16/"
pathApr6        = "/cms/data/store/user/t2/users/dsperka/Run2/Zprime/2017/rootfiles_Data_Apr6/"
inUFTier2       = True

# ____________________________________________________________________________________________________________________________________________ ||
# SingleMuon
SingleMuon2017_cmpList = ComponentList(
        [ 
            Component("SingleMuon2017",
                pathApr16+"SingleMuon_Run2017.root",
                "Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

SingleMuon2017 = Dataset(
        "SingleMuon2017",
        SingleMuon2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# SingleElectron
SingleElectron2017_cmpList = ComponentList(
        [ 
            Component("SingleElectron2017",
                pathApr16+"SingleElectron_Run2017.root",
                "Ana/passedEvents",inUFTier2=inUFTier2),
        ]
        )

SingleElectron2017 = Dataset(
        "SingleElectron2017",
        SingleElectron2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# DoubleEG
DoubleEG2017_cmpList = ComponentList(
        [ 
            Component("DoubleEG2017",
                pathApr6+"DoubleEG_Run2017%s-17Nov2017-v1.root"%era,
                "Ana/passedEvents",inUFTier2=inUFTier2) for era in ["B","C","D","E","F"]
        ]
        )

DoubleEG2017 = Dataset(
        "DoubleEG2017",
        DoubleEG2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# DoubleMuon
DoubleMuon2017_cmpList = ComponentList(
        [ 
            Component("DoubleMuon2017",
                pathApr6+"DoubleMuon_Run2017-17Nov2017-v1.root",
                "Ana/passedEvents",inUFTier2=inUFTier2)
        ]
        )

DoubleMuon2017 = Dataset(
        "DoubleEG2017",
        DoubleMuon2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# MuonEG
MuonEG2017_cmpList = ComponentList(
        [ 
            Component("MuonEG2017",
                pathApr6+"MuonEG_Run2017%s-17Nov2017-v1.root"%era,
                "Ana/passedEvents",inUFTier2=inUFTier2) for era in ["B","C","D","E","F"]
        ]
        )

MuonEG2017 = Dataset(
        "MuonEG2017",
        MuonEG2017_cmpList,
        isMC                = False,
        )
