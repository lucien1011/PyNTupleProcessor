from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system

bkgTreeDir              = system.getStoragePath()+"/lucien/Higgs/HZZ4l/NTuple/ZPlusX/ZXCR/20190313_Run2017_ZXCR-Z1LSkim_LiteHZZTree/"
bkgTreeDirT2            = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"
predCRTreeDir           = system.getStoragePath()+"/lucien/Higgs/HZZ4l/NTuple/ZPlusX/ZXCR/20190313_Run2017_ZXCR-Z1LSkim_LiteHZZTree/"
inUFTier2               = False
saveSumWeightTxt        = False
sumWeightHist           = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
predCR_cmpList = ComponentList(
        [
            Component("PredCR",predCRTreeDir+"/Data_Run2017-17Nov2017_noDuplicates_FRWeightFromVukasin.root","passedEvents",False),
        ]
        )
predCR = Dataset(
        "PredCR",
        predCR_cmpList,
        isMC                = True,
        isSignal            = True,
        skipWeight          = True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M50",bkgTreeDir+"DYJetsToLL_M50.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        DYJetsToLL_M50_cmpList,
        isMC = True,
        xs = 6104, 
        )
path_DYJetsToLL_M50 = bkgTreeDirT2+"DYJetsToLL_M50.root"
if system.getSystemModel() == system.remote_str:
    DYJetsToLL_M50.setSumWeight(path_DYJetsToLL_M50,sumWeightHist,True)
    if saveSumWeightTxt:
        DYJetsToLL_M50.saveSumWeightToPath(path_DYJetsToLL_M50.replace(".root","txt"))
else system.getSystemModel() == system.local_str:
    DYJetsToLL_M50.setSumWeightByTxt(bkgTreeDir+"DYJetsToLL_M50.txt")

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M10To50",bkgTreeDir+"DYJetsToLL_M10To50.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M10To50 = Dataset(
        "DYJetsToLL_M10To50",
        DYJetsToLL_M10To50_cmpList,
        isMC = True,
        xs = 6104, 
        )
path_DYJetsToLL_M10To50 = bkgTreeDirT2+"DYJetsToLL_M10To50.root"
if system.getSystemModel() == system.remote_str:
    DYJetsToLL_M10To50.setSumWeight(path_DYJetsToLL_M10To50,sumWeightHist,True)
    if saveSumWeightTxt:
        DYJetsToLL_M10To50.saveSumWeightToPath(path_DYJetsToLL_M10To50.replace(".root","txt"))
else system.getSystemModel() == system.local_str:
    DYJetsToLL_M10To50.setSumWeightByTxt(bkgTreeDir+"DYJetsToLL_M10To50.txt")

# ____________________________________________________________________________________________________________________________________________ ||
TTJets_cmpList = ComponentList(
        [
            Component("TTJets",bkgTreeDir+"TTJets.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets = Dataset(
        "TTJets",
        TTJets_cmpList,
        isMC = True,
        xs = 87.31, 
        )
path_TTJets = bkgTreeDirT2+"TTJets.root"
if system.getSystemModel() == system.remote_str:
    TTJets.setSumWeight(path_TTJets,sumWeightHist,True)
    if saveSumWeightTxt:
        TTJets.saveSumWeightToPath(path_TTJets.replace(".root","txt"))
else system.getSystemModel() == system.local_str:
    TTJets.setSumWeightByTxt(bkgTreeDir+"TTJets.txt")

# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_cmpList = ComponentList(
        [
            Component("WZTo3LNu",bkgTreeDir+"WZTo3LNu.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WZTo3LNu = Dataset(
        "WZTo3LNu",
        WZTo3LNu_cmpList,
        isMC = True,
        xs = 4.430, 
        )
path_WZTo3LNu = bkgTreeDirT2+"WZTo3LNu.root"
if system.getSystemModel() == system.remote_str:
    WZTo3LNu.setSumWeight(path_WZTo3LNu,sumWeightHist,True)
    if saveSumWeightTxt:
        WZTo3LNu.saveSumWeightToPath(path_WZTo3LNu.replace(".root","txt"))
else system.getSystemModel() == system.local_str:
    WZTo3LNu.setSumWeightByTxt(bkgTreeDir+"WZTo3LNu.txt")
    
# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgTreeDir+"ZZTo4L_ext1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
path_qqZZTo4L = bkgTreeDirT2+"ZZTo4L_ext1.root"
if system.getSystemModel() == system.remote_str:
    qqZZTo4L.setSumWeight(path_qqZZTo4L,sumWeightHist,True)
    if saveSumWeightTxt:
        qqZZTo4L.saveSumWeightToPath(path_qqZZTo4L.replace(".root","txt"))
else system.getSystemModel() == system.local_str:
    qqZZTo4L.setSumWeightByTxt(bkgTreeDir+"ZZTo4L_ext1.txt")
