from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgTreeDirT2_Feb21      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2l_Feb21/"
#bkgTreeDirT2_Aug10      = "/cms/data/store/user/t2/users/klo/Higgs/HZZ4l/NTuple/Run2/MC80X_M17_2lskim_Aug10/"
#bkgTreeDir      = "/raid/raid7/kshi/Zprime/20190718/SkimTree_Run2016_MC/"
sigTreeDirT2    = "/cms/data/store/user/t2/users/mhl/rootfiles_2017/"
sigTreeDir      = "/raid/raid7/kshi/Zprime/20190724/SkimTree_Run2016_signalregion_MC/"
inUFTier2       = False
saveSumWeightTxt= False
sumWeightHist   = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
WmTo3munu_ZpM45_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM45",sigTreeDir+"WmTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM45 = Dataset(
        "WmTo3munu_ZpM45",
        WmTo3munu_ZpM45_cmpList,
        isSignal = True,
        xs = 1, 
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

WmTo3munu_ZpM15_cmpList = ComponentList(
        [
            Component("WmTo3munu_ZpM15",sigTreeDir+"WmTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WmTo3munu_ZpM15 = Dataset(
        "WmTo3munu_ZpM15",
        WmTo3munu_ZpM15_cmpList,
        isSignal = True,
        xs = 1, 
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

WpTo3munu_ZpM45_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM45",sigTreeDir+"WpTo3munu_ZpM45_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM45 = Dataset(
        "WpTo3munu_ZpM45",
        WpTo3munu_ZpM45_cmpList,
        isSignal = True,
        xs = 1, 
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

WpTo3munu_ZpM15_cmpList = ComponentList(
        [
            Component("WpTo3munu_ZpM15",sigTreeDir+"WpTo3munu_ZpM15_13TeV_MadGraph5_pythia8-v4_hmei-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WpTo3munu_ZpM15 = Dataset(
        "WpTo3munu_ZpM15",
        WpTo3munu_ZpM15_cmpList,
        isSignal = True,
        xs = 1, 
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


