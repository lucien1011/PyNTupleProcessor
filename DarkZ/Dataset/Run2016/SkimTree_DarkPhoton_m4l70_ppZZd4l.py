from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

sigSkimTreeDir      = system.getStoragePath()+"/rosedj1/Higgs/DarkZ-NTuple/20190403/SkimTree_DarkPhoton_Run2017MC_ppToZZdTo4l/"
sigTreeDir          = "/cms/data/store/user/t2/users/rosedj1/Higgs/DarkZ/NTuples/ppToZZdTo4l/"
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
epsilon             = 0.05
epsilon_init        = 0.05
saveSumWeightTxt    = False
qqZZXs              = 0.04
zTollBr             = 0.033632*2

# ____________________________________________________________________________________________________________________________________________ ||
# ppZZd4l_M4
#ppZZd4l_M4_cmpList = ComponentList(
#        [ Component("ppZZd4l_M4",sigSkimTreeDir+"ppToZZdTo4l_mZd4GeV.root","passedEvents",inUFTier2=inUFTier2) ]
#        )
#ppZZd4l_M4 = Dataset(
#        "ppZZd4l_M4",
#        ppZZd4l_M4_cmpList,
#        isMC                = True,
#        isSignal            = True,
#        xs                  = 1.256*epsilon**4*10913.03556293004, # xs(qqZZ4l)*eps^4*avg(MG_ratio/eps^4) Take avg from spreadsheet
#        )
#handleSumWeight(
#        ppZZd4l_M4,
#        system,
#        sigTreeDir+"ppToZZdTo4l_mZd4GeV.root",
#        sumWeightHist,
#        True,
#        saveSumWeightTxt,
#        sigSkimTreeDir+"ppToZZdTo4l_mZd4GeV.txt",
#        )

# ____________________________________________________________________________________________________________________________________________ ||
# ppZZd4l_M5
ppZZd4l_M5_cmpList = ComponentList(
        [ Component("ppZZd4l_M5",sigSkimTreeDir+"ppToZZdTo4l_mZd5GeV.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ppZZd4l_M5 = Dataset(
        "ppZZd4l_M5",
        ppZZd4l_M5_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 0.5889/epsilon_init**2*epsilon**2*0.28*zTollBr, 
        )
handleSumWeight(
        ppZZd4l_M5,
        system,
        sigTreeDir+"ppToZZdTo4l_mZd5GeV.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ppToZZdTo4l_mZd5GeV.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ppZZd4l_M15
ppZZd4l_M15_cmpList = ComponentList(
        [ Component("ppZZd4l_M15",sigSkimTreeDir+"ppToZZdTo4l_mZd15GeV.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ppZZd4l_M15 = Dataset(
        "ppZZd4l_M15",
        ppZZd4l_M15_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 0.2327/epsilon_init**2*epsilon**2*0.286*zTollBr, 
        )
handleSumWeight(
        ppZZd4l_M15,
        system,
        sigTreeDir+"ppToZZdTo4l_mZd15GeV.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ppToZZdTo4l_mZd15GeV.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ppZZd4l_M30
ppZZd4l_M30_cmpList = ComponentList(
        [ Component("ppZZd4l_M30",sigSkimTreeDir+"ppToZZdTo4l_mZd30GeV.root","passedEvents",inUFTier2=inUFTier2) ]
        )
ppZZd4l_M30 = Dataset(
        "ppZZd4l_M30",
        ppZZd4l_M30_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 0.1188/epsilon_init**2*epsilon**2*0.280*zTollBr, 
        )
handleSumWeight(
        ppZZd4l_M30,
        system,
        sigTreeDir+"ppToZZdTo4l_mZd30GeV.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        sigSkimTreeDir+"ppToZZdTo4l_mZd30GeV.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||

ppZZdSamples = [
        #ppZZd4l_M4,
        ppZZd4l_M5,
        ppZZd4l_M15,
        ppZZd4l_M30,
        ]

