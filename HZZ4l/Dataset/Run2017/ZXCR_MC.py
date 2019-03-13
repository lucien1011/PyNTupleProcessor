from Core.ComponentList import *
from Core.Dataset import Dataset

#bkgTreeDir             = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_MC80X_ZXCRSelection/"
#bkgTreeDir             = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_MC80X_HIG-16-041-ZXCRSelection_v2/"
bkgTreeDir              = "/raid/raid7/lucien/Higgs/HZZ4l/NTuple/ZPlusX/ZXCR/20190313_Run2017_ZXCR-Z1LSkim_LiteHZZTree/"
bkgTreeDirT2            = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"
predCRTreeDir           = "/raid/raid7/lucien/Higgs/HZZ4l/NTuple/ZPlusX/ZXCR/20190313_Run2017_ZXCR-Z1LSkim_LiteHZZTree/"
inUFTier2               = False

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
DYJetsToLL_M50.setSumWeight(bkgTreeDirT2+"DYJetsToLL_M50.root","Ana/sumWeights",True)

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
DYJetsToLL_M10To50.setSumWeight(bkgTreeDirT2+"DYJetsToLL_M10To50.root","Ana/sumWeights",True)

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
TTJets.setSumWeight(bkgTreeDirT2+"TTJets.root","Ana/sumWeights",True)

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
WZTo3LNu.setSumWeight(bkgTreeDirT2+"WZTo3LNu.root","Ana/sumWeights",True)

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
qqZZTo4L.setSumWeight(
    bkgTreeDirT2+"ZZTo4L_ext1.root",
    "Ana/sumWeights",
    True,
    )
