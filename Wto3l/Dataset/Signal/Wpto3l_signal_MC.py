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
WpTo3l_ZpM15_cmpList = ComponentList(
        [
            Component("WpTo3l_ZpM15",sigTreeDir+"WpTo3l_ZpM15.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3l_ZpM15 = Dataset(
        "WpTo3l_ZpM15",
        WpTo3l_ZpM15_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.5649641, 
        )
handleSumWeight(
        WpTo3l_ZpM15,
        system,
        sigTreeDirT2+"WpTo3l_ZpM15.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WpTo3l_ZpM15.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WpTo3l_ZpM20_cmpList = ComponentList(
        [
            Component("WpTo3l_ZpM20",sigTreeDir+"WpTo3l_ZpM20.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3l_ZpM20 = Dataset(
        "WpTo3l_ZpM20",
        WpTo3l_ZpM20_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.3004604,
        )
handleSumWeight(
        WpTo3l_ZpM20,
        system,
        sigTreeDirT2+"WpTo3l_ZpM20.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WpTo3l_ZpM20.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WpTo3l_ZpM30_cmpList = ComponentList(
        [
            Component("WpTo3l_ZpM30",sigTreeDir+"WpTo3l_ZpM30.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3l_ZpM30 = Dataset(
        "WpTo3l_ZpM30",
        WpTo3l_ZpM30_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.08894534,
        )
handleSumWeight(
        WpTo3l_ZpM30,
        system,
        sigTreeDirT2+"WpTo3l_ZpM30.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WpTo3l_ZpM30.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WpTo3l_ZpM45_cmpList = ComponentList(
        [   
            Component("WpTo3l_ZpM45",sigTreeDir+"WpTo3l_ZpM45.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3l_ZpM45 = Dataset(
        "WpTo3l_ZpM45",
        WpTo3l_ZpM45_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.012078543,
        )
handleSumWeight(
        WpTo3l_ZpM45,
        system,
        sigTreeDirT2+"WpTo3l_ZpM45.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WpTo3l_ZpM45.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
WpTo3l_ZpM60_cmpList = ComponentList(
        [
            Component("WpTo3l_ZpM60",sigTreeDir+"WpTo3l_ZpM60.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3l_ZpM60 = Dataset(
        "WpTo3l_ZpM60",
        WpTo3l_ZpM60_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.0011469974,
        )
handleSumWeight(
        WpTo3l_ZpM60,
        system,
        sigTreeDirT2+"WpTo3l_ZpM60.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WpTo3l_ZpM60.txt",
        )
# ____________________________________________________________________________________________________________________________________________ ||
sigpSamples = [WpTo3l_ZpM15,WpTo3l_ZpM20,WpTo3l_ZpM30,WpTo3l_ZpM45,WpTo3l_ZpM60]
