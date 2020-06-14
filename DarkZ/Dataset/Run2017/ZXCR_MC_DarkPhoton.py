from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgTreeDir             = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_MC80X_ZXCRSelection/"
#bkgTreeDir             = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_MC80X_HIG-16-041-ZXCRSelection_v2/"
bkgTreeDir              = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20181116/SkimTree_DarkPhoton_ZX_Run2017Data_m4l70/"
bkgTreeDirT2            = "/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"
predCRTreeDir           = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20181116/SkimTree_DarkPhoton_ZX_Run2017Data_m4l70/"
inUFTier2               = False
saveSumWeightTxt        = True
sumWeightHist           = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
# Z+X
predCR_cmpList = ComponentList(
        [
            #Component("PredCR",predCRTreeDir+"/Data_Run2017-17Nov2017_noDuplicates_FRWeight.root","passedEvents",False),
            #Component("PredCR",predCRTreeDir+"/Data_Run2017-17Nov2017_noDuplicates_FRWeightv2.root","passedEvents",False),
            #Component("PredCR",predCRTreeDir+"/Data_Run2017-17Nov2017_noDuplicates_FRWeightFromVukasin.root","passedEvents",False),
            Component("PredCR",predCRTreeDir+"/Data_Run2017-17Nov2017_noDuplicates_FRWeightFromVukasinWZRemoved.root","passedEvents",False),
            #Component("PredCR",predCRTreeDir+"/Data_Run2017-17Nov2017_noDuplicates_FRWeightFromVukasinV2.root","passedEvents",False),
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
#DYJetsToLL_M50.setSumWeight(bkgTreeDirT2+"DYJetsToLL_M50.root","Ana/sumWeights",True)
handleSumWeight(
        DYJetsToLL_M50,
        system,
        bkgTreeDirT2+"DYJetsToLL_M50.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"DYJetsToLL_M50.txt",
        )

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
#DYJetsToLL_M10To50.setSumWeight(bkgTreeDirT2+"DYJetsToLL_M10To50.root","Ana/sumWeights",True)
handleSumWeight(
        DYJetsToLL_M10To50,
        system,
        bkgTreeDirT2+"DYJetsToLL_M10To50.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"DYJetsToLL_M10To50.txt",
        )

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
#TTJets.setSumWeight(bkgTreeDirT2+"TTJets.root","Ana/sumWeights",True)
handleSumWeight(
        TTJets,
        system,
        bkgTreeDirT2+"TTJets.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"TTJets.txt",
        )

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
#WZTo3LNu.setSumWeight(bkgTreeDirT2+"WZTo3LNu.root","Ana/sumWeights",True)
handleSumWeight(
        WZTo3LNu,
        system,
        bkgTreeDirT2+"WZTo3LNu.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"WZTo3LNu.txt",
        )

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
#qqZZTo4L.setSumWeight(
#    bkgTreeDirT2+"ZZTo4L_ext1.root",
#    "Ana/sumWeights",
#    True,
#    )
handleSumWeight(
        qqZZTo4L,
        system,
        bkgTreeDirT2+"ZZTo4L_ext1.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"qqZZTo4L.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
ZGToLLG_cmpList = ComponentList(
        [
            Component("ZGToLLG",bkgTreeDir+"ZGToLLG_01J_5f_lowMLL_lowGPt_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
ZGToLLG = Dataset(
        "ZGToLLG",
        ZGToLLG_cmpList,
        isMC = True,
        xs = 164.2, 
        )
handleSumWeight(
        ZGToLLG,
        system,
        bkgTreeDirT2+"ZGToLLG_01J_5f_lowMLL_lowGPt_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir+"ZGToLLG_01J_5f_lowMLL_lowGPt_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17.txt",
        )
