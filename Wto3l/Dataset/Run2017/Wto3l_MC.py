from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgTreeDirT2_Feb21      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2l_Feb21/"
#bkgTreeDirT2_Aug10      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2lskim_Aug10/"
bkgTreeDirT2            = "/cmsuf/data/store/user/t2/users/nikmenendez/2017_MC_bkg/"
#bkgTreeDir      = "/raid/raid7/kshi/Zprime/20190718/SkimTree_Run2016_MC/"
#bkgTreeDir      = "/raid/raid7/kshi/Zprime/20190827/SkimTree_Run2016_MMM_MC/"
bkgTreeDir_2017      = "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/2017/"
inUFTier2       = False
saveSumWeightTxt= False
sumWeightHist   = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_2017_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M50",bkgTreeDir_2017+"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M50_2017 = Dataset(
        "DYJetsToLL_M50",
        DYJetsToLL_M50_2017_cmpList,
        isMC = True,
        xs = 5343, 
        )
handleSumWeight(
        DYJetsToLL_M50_2017,
        system,
        bkgTreeDirT2+"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root",
        #bkgTreeDir+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir_2017+"DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.txt",
        )
print "DYJetsToLL_M50_2017 sumw = " + str(DYJetsToLL_M50_2017.sumw)
# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_2017_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M10To50",bkgTreeDir_2017+"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M10To50_2017 = Dataset(
        "DYJetsToLL_M10To50",
        DYJetsToLL_M10To50_2017_cmpList,
        isMC = True,
        xs = 15810, 
        )
handleSumWeight(
        DYJetsToLL_M10To50_2017,
        system,
        bkgTreeDirT2+"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8.root",
        #bkgTreeDir+"DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir_2017+"DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8.txt",
        )
print "DYJetsToLL_M10To50_2017 sumw = " + str(DYJetsToLL_M10To50_2017.sumw)
# ____________________________________________________________________________________________________________________________________________ ||
TTJets_2017_cmpList = ComponentList(
        [
            Component("TTJets",bkgTreeDir_2017+"TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets_2017 = Dataset(
        "TTJets",
        TTJets_2017_cmpList,
        isMC = True,
        xs = 54.23, 
        )
handleSumWeight(
        TTJets_2017,
        system,
        bkgTreeDirT2+"TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8.root",
        #bkgTreeDir+"TTJets_Dilept_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir_2017+"TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8.txt",
        )
print "TTJets_2017 sumw = " + str(TTJets_2017.sumw)
# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_2017_cmpList = ComponentList(
        [
            Component("WZTo3LNu",bkgTreeDir_2017+"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WZTo3LNu_2017 = Dataset(
        "WZTo3LNu",
        WZTo3LNu_2017_cmpList,
        isMC = True,
        xs = 5.052, 
        )
handleSumWeight(
        WZTo3LNu_2017,
        system,
        bkgTreeDirT2+"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.root",
        #bkgTreeDir+"WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgTreeDir_2017+"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8.txt",
        )
print "WZTo3LNu_2017 sumw = " + str(WZTo3LNu_2017.sumw)

bkgSamples_2017 = [WZTo3LNu_2017,TTJets_2017,DYJetsToLL_M10To50_2017,DYJetsToLL_M50_2017]

