from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

import os

# ____________________________________________________________________________________________________________________________________________ ||
treePathInFile          = "Events"
inUFTier2               = True

# ____________________________________________________________________________________________________________________________________________ ||
# ZGGToLLGG
bkgSkimTreeDir_ZGGToLLGG_1 = "/cms/data/store/mc/RunIIFall17NanoAOD/ZGGToLLGG_5f_TuneCP5_13TeV-amcatnlo-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/280000/"
bkgSkimTreeDir_ZGGToLLGG_2 = "/cms/data/store/mc/RunIIFall17NanoAOD/ZGGToLLGG_5f_TuneCP5_13TeV-amcatnlo-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/"
bkgSkimTreeDir_ZGGToLLGG_3 = "/cms/data/store/mc/RunIIFall17NanoAOD/ZGGToLLGG_5f_TuneCP5_13TeV-amcatnlo-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/1110000/"

ZGGToLLGG_cmpList = ComponentList(
        [ 
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"0A4048FC-5346-E911-9C77-90E2BA0FAFB4.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"0A4048FC-5346-E911-9C77-90E2BA0FAFB4.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"1480F919-5446-E911-9C89-AC1F6B1AF002.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"1C0D01F1-5346-E911-BD93-B496910A9A7C.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"1EA89820-5446-E911-9078-FA163ED94A2A.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"2AADC42E-5446-E911-A705-0025905B85DC.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"36E99F47-5446-E911-9C21-0242AC130002.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"667C3242-5446-E911-A92A-0CC47AACFCDE.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"668BF53D-5446-E911-B163-008CFA11131C.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"78144828-5446-E911-BB1A-0CC47A4D9A84.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"7C99409A-3E36-E911-9C89-AC1F6BAC7D14.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"96EC101E-5446-E911-BCF7-509A4C748016.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"9857F517-5446-E911-9CB3-0CC47AF9B1DE.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"9C8450E6-5346-E911-9272-F4E9D4A36760.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"9CD04905-5446-E911-AADA-D4856459AC30.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"A83C99E8-5346-E911-890F-AC1F6B596102.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"A8EF5DC1-A337-E911-A65C-0025905B85DA.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"BE526824-5446-E911-B7E8-001E67792448.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"C46407F0-5346-E911-8BE5-28924A33B9AA.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"D83058EC-5346-E911-A8F0-ECB1D7928EC8.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"DE46BDF7-5346-E911-A273-6C3BE5B50180.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"E8943437-5446-E911-904E-EC0D9A82260E.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"F4074601-5446-E911-8DAA-68CC6EA5BE22.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"FEC65820-5446-E911-90EA-0242AC1C0503.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_2,"0224C91A-7D4C-E911-A9E7-F4CE46B27A1A.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_2,"06A92BB4-934C-E911-80FB-1CB72C1B6C46.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_2,"06CD7B2E-7D4C-E911-A3CC-008CFAFBF2BE.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_2,"0AE75F7F-494B-E911-9C46-00259075D714.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_2,"6EF0DBC0-634C-E911-863A-405CFDFF481B.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_2,"BEA062A0-354B-E911-902F-1866DA7F936D.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_2,"FAC6FD09-9B4C-E911-AF4D-AC1F6B0DE3A4.root"),treePathInFile,inUFTier2=inUFTier2),
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_3,"D4E5C496-274B-E911-81A3-00259029E670.root"),treePathInFile,inUFTier2=inUFTier2),
        ]
        )

ZGGToLLGG = Dataset(
        "ZGGToLLGG",
        ZGGToLLGG_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )

ZGGToLLGG.sumw = 0.
for cmp in ZGGToLLGG_cmpList:
    ZGGToLLGG.sumw += cmp.getSumWeightNanoAOD()

# ____________________________________________________________________________________________________________________________________________ ||
