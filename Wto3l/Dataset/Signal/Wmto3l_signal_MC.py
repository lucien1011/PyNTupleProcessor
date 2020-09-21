from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

bkgTreeDirT2            = "/cmsuf/data/store/user/t2/users/nikmenendez/2018_MC_bkg/"
bkgTreeDir_2018		= "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/2018/"
sigTreeDirT2		= "/cmsuf/data/store/user/t2/users/nikmenendez/signal/"
sigTreeDir		= "/cmsuf/data/store/user/t2/users/nikmenendez/skimmed/signal/"
inUFTier2       = False
saveSumWeightTxt= False
sumWeightHist   = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
WmTo3l_ZpM15_cmpList = ComponentList(
        [
            Component("WmTo3l_ZpM15",sigTreeDir+"WmTo3l_ZpM15.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3l_ZpM15 = Dataset(
        "WmTo3l_ZpM15",
        WmTo3l_ZpM15_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.4504013, 
        )
handleSumWeight(
        WmTo3l_ZpM15,
        system,
        sigTreeDirT2+"WmTo3l_ZpM15.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WmTo3l_ZpM15.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WmTo3l_ZpM20_cmpList = ComponentList(
        [
            Component("WmTo3l_ZpM20",sigTreeDir+"WmTo3l_ZpM20.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3l_ZpM20 = Dataset(
        "WmTo3l_ZpM20",
        WmTo3l_ZpM20_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.2425901,
        )
handleSumWeight(
        WmTo3l_ZpM20,
        system,
        sigTreeDirT2+"WmTo3l_ZpM20.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WmTo3l_ZpM20.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WmTo3l_ZpM30_cmpList = ComponentList(
        [
            Component("WmTo3l_ZpM30",sigTreeDir+"WmTo3l_ZpM30.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3l_ZpM30 = Dataset(
        "WmTo3l_ZpM30",
        WmTo3l_ZpM30_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.07259808,
        )
handleSumWeight(
        WmTo3l_ZpM30,
        system,
        sigTreeDirT2+"WmTo3l_ZpM30.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WmTo3l_ZpM30.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WmTo3l_ZpM45_cmpList = ComponentList(
        [   
            Component("WmTo3l_ZpM45",sigTreeDir+"WmTo3l_ZpM45.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3l_ZpM45 = Dataset(
        "WmTo3l_ZpM45",
        WmTo3l_ZpM45_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.00989203,
        )
handleSumWeight(
        WmTo3l_ZpM45,
        system,
        sigTreeDirT2+"WmTo3l_ZpM45.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WmTo3l_ZpM45.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WmTo3l_ZpM60_cmpList = ComponentList(
        [
            Component("WmTo3l_ZpM60",sigTreeDir+"WmTo3l_ZpM60.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3l_ZpM60 = Dataset(
        "WmTo3l_ZpM60",
        WmTo3l_ZpM60_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.0008656826,
        )
handleSumWeight(
        WmTo3l_ZpM60,
        system,
        sigTreeDirT2+"WmTo3l_ZpM60.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WmTo3l_ZpM60.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
sigmSamples = [WmTo3l_ZpM15,WmTo3l_ZpM20,WmTo3l_ZpM30,WmTo3l_ZpM45,WmTo3l_ZpM60]
