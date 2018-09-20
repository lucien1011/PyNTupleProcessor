from Core.ComponentList import *
from Core.Dataset import Dataset

treeDir_RunB    = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Data_Run2016B_July18_v1_nJet2TightLep1_LeptonJetRecleaner/"
fileName        = "SkimTree.root"
treeName        = "tree"
inUFTier2       = True

Data_Run2016B       = Dataset(
                    "Data_Run2016B",
                    ComponentList([
                        Component("MuonEG_Run2016B",treeDir_RunB+"MuonEG/"+fileName,treeName,inUFTier2=inUFTier2),
                        Component("DoubleMuon_Run2016B",treeDir_RunB+"DoubleMuon/"+fileName,treeName,inUFTier2=inUFTier2),
                        Component("DoubleEG_Run2016B",treeDir_RunB+"DoubleEG/"+fileName,treeName,inUFTier2=inUFTier2),
                        ]),
                    isMC = False,
                    )
