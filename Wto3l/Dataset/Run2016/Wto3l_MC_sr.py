from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgTreeDirT2_Feb21      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2l_Feb21/"
#bkgTreeDirT2_Aug10      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2lskim_Aug10/"
#bkgTreeDir      = "/raid/raid7/kshi/Zprime/20190718/SkimTree_Run2016_MC/"
sigTreeDirT2    = "/cms/data/store/user/t2/users/mhl/rootfiles_2017/"
sigTreeDir      = "/raid/raid7/kshi/Zprime/20190827/SkimTree_Run2016_MMM_MC/"
sigTreeDir_new_unskim = "/home/kshi/Zprime/Zp_data_Ntuple/"
sigTreeDir_new  = "/home/kshi/Zprime/Zp_data_Ntuple/Ntuple_LiteAna/"
inUFTier2       = False
saveSumWeightTxt= False
sumWeightHist   = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
'''
WmTo3munu_ZpM45_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM45",sigTreeDir+"WmTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM45 = Dataset(
        "WmTo3munu_ZpM45",
        WmTo3munu_ZpM45_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.00989203, 
        )
handleSumWeight(
        WmTo3munu_ZpM45,
        system,
        sigTreeDirT2+"WmTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WmTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.txt",
        )
'''
WmTo3munu_ZpM15_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM15",sigTreeDir+"WmTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM15 = Dataset(
        "WmTo3munu_ZpM15",
        WmTo3munu_ZpM15_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.4504013, 
        )
handleSumWeight(
        WmTo3munu_ZpM15,
        system,
        sigTreeDirT2+"WmTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WmTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.txt",
        )
'''
WpTo3munu_ZpM45_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM45",sigTreeDir+"WpTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM45 = Dataset(
        "WpTo3munu_ZpM45",
        WpTo3munu_ZpM45_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.012078543, 
        )
handleSumWeight(
        WpTo3munu_ZpM45,
        system,
        sigTreeDirT2+"WpTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WpTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.txt",
        )
'''
WpTo3munu_ZpM15_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM15",sigTreeDir+"WpTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM15 = Dataset(
        "WpTo3munu_ZpM15",
        WpTo3munu_ZpM15_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.5649641, 
        )
handleSumWeight(
        WpTo3munu_ZpM15,
        system,
        sigTreeDirT2+"WpTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigTreeDir+"WpTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.txt",
        )


WmTo3munu_ZpM20_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM20",sigTreeDir_new+"WmTo3l_ZpM20.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM20 = Dataset(
        "WmTo3munu_ZpM20",
        WmTo3munu_ZpM20_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.2425901, 
        )
handleSumWeight(
        WmTo3munu_ZpM20,
        system,
        sigTreeDir_new_unskim+"WmTo3l_ZpM20.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WmTo3l_ZpM20.txt",
        )

WmTo3munu_ZpM30_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM30",sigTreeDir_new+"WmTo3l_ZpM30.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM30 = Dataset(
        "WmTo3munu_ZpM30",
        WmTo3munu_ZpM30_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.07259808, 
        )
handleSumWeight(
        WmTo3munu_ZpM30,
        system,
        sigTreeDir_new_unskim+"WmTo3l_ZpM30.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WmTo3l_ZpM30.txt",
        )

WmTo3munu_ZpM45_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM45",sigTreeDir_new+"WmTo3l_ZpM45.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM45 = Dataset(
        "WmTo3munu_ZpM45",
        WmTo3munu_ZpM45_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.00989203, 
        )
handleSumWeight(
        WmTo3munu_ZpM45,
        system,
        sigTreeDir_new_unskim+"WmTo3l_ZpM45.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WmTo3l_ZpM45.txt",
        )

WmTo3munu_ZpM60_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM60",sigTreeDir_new+"WmTo3l_ZpM60.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM60 = Dataset(
        "WmTo3munu_ZpM60",
        WmTo3munu_ZpM60_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.0008656826, 
        )
handleSumWeight(
        WmTo3munu_ZpM60,
        system,
        sigTreeDir_new_unskim+"WmTo3l_ZpM60.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WmTo3l_ZpM60.txt",
        )

WpTo3munu_ZpM20_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM20",sigTreeDir_new+"WpTo3l_ZpM20.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM20 = Dataset(
        "WpTo3munu_ZpM20",
        WpTo3munu_ZpM20_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.3004604, 
        )
handleSumWeight(
        WpTo3munu_ZpM20,
        system,
        sigTreeDir_new_unskim+"WpTo3l_ZpM20.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WpTo3l_ZpM20.txt",
        )

WpTo3munu_ZpM30_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM30",sigTreeDir_new+"WpTo3l_ZpM30.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM30 = Dataset(
        "WpTo3munu_ZpM30",
        WpTo3munu_ZpM30_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.08894534, 
        )
handleSumWeight(
        WpTo3munu_ZpM30,
        system,
        sigTreeDir_new_unskim+"WpTo3l_ZpM30.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WpTo3l_ZpM30.txt",
        )

WpTo3munu_ZpM45_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM45",sigTreeDir_new+"WpTo3l_ZpM45.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM45 = Dataset(
        "WpTo3munu_ZpM45",
        WpTo3munu_ZpM45_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.012078543, 
        )
handleSumWeight(
        WpTo3munu_ZpM45,
        system,
        sigTreeDir_new_unskim+"WpTo3l_ZpM45.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WpTo3l_ZpM45.txt",
        )

WpTo3munu_ZpM60_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM60",sigTreeDir_new+"WpTo3l_ZpM60.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM60 = Dataset(
        "WpTo3munu_ZpM60",
        WpTo3munu_ZpM60_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.0011469974, 
        )
handleSumWeight(
        WpTo3munu_ZpM60,
        system,
        sigTreeDir_new_unskim+"WpTo3l_ZpM60.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WpTo3l_ZpM60.txt",
        )

WmTo3munu_ZpM15_30_60_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM15_30_60",sigTreeDir_new+"WmTo3l_ZpM15_30_60.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM15_30_60 = Dataset(
        "WmTo3munu_ZpM15_30_60",
        WmTo3munu_ZpM15_30_60_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.5238650626, 
        )
handleSumWeight(
        WmTo3munu_ZpM15_30_60,
        system,
        sigTreeDir_new_unskim+"WmTo3l_ZpM15_30_60.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WmTo3l_ZpM15_30_60.txt",
        )

WpTo3munu_ZpM15_30_60_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM15_30_60",sigTreeDir_new+"WpTo3l_ZpM15_30_60.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM15_30_60 = Dataset(
        "WpTo3munu_ZpM15_30_60",
        WpTo3munu_ZpM15_30_60_cmpList,
        isMC = True,
        isSignal = True,
        xs = 0.6550564374, 
        )
handleSumWeight(
        WpTo3munu_ZpM15_30_60,
        system,
        sigTreeDir_new_unskim+"WpTo3l_ZpM15_30_60.root",
        sumWeightHist,
        False,
        saveSumWeightTxt,
        sigTreeDir_new+"WpTo3l_ZpM15_30_60.txt",
        )


sigSamples = [
            WpTo3munu_ZpM15,
            WpTo3munu_ZpM20,
            WpTo3munu_ZpM30,
            WpTo3munu_ZpM45,
            WpTo3munu_ZpM60,
            WmTo3munu_ZpM15,
            WmTo3munu_ZpM20,
            WmTo3munu_ZpM30,
            WmTo3munu_ZpM45,
            WmTo3munu_ZpM60,
            ]

WTo3mu_ZpM15 = [
            WpTo3munu_ZpM15,
            WmTo3munu_ZpM15,
            ]

