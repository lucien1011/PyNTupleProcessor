from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgSkimTreeDir2      = system.getStoragePath()+"/lucien/Higgs/Zprime-NTuple/20190605/SkimTree_Zprime_Run2017Data_m4l70/"
bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20200212_Zto4l/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir2      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/test/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir2      = system.getStoragePath()+"/Zprime/20200212_Zto4l/test/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir2     = system.getStoragePath()+"/Zprime/20200212_Zto4l/unskim/SkimTree_Run2017_MMM_MC/"
bkgSkimTreeDir2      = system.getStoragePath()+"/Zprime/20200212_Zto4l/test_4GeV/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir2      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/unskim/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir2     = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/M1To4/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir3     = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/M4ToInf/SkimTree_Run2017_MMM_MC/"
bkgTreeDir          = "/cmsuf/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/BkgMC_Run2017/"
bkgTreeDir2         = "/cmsuf/data/store/user/t2/users/klo/Higgs/Zprime/94X_MCProd_191127/"
#dataTreeDir         = bkgSkimTreeDir
#dataTreeDir         = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/SkimTree_Run2017_MMM_Data/"
#dataTreeDir         = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2017_MMM_Data/"
#dataTreeDir         = system.getStoragePath()+"/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2017_MMM_Data/"
dataTreeDir         = system.getStoragePath()+"/Zprime/20200212_Zto4l/test_4GeV/SkimTree_Run2017_MMM_Data/"
#dataTreeDir2        = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/promptCR/SkimTree_Run2017_MMM_Data/"
dataTreeDir2        = system.getStoragePath()+"/Zprime/20200212_Zto4l/promptCR/SkimTree_Run2017_MMM_Data/"
inUFTier2           = True
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = True

# ____________________________________________________________________________________________________________________________________________ ||
# Data2017
data2017_cmpList = ComponentList(
        [ 
            #Component("Data2017",dataTreeDir+"/MuonEG-DoubleEG-SingleElectron_Run2017-17Nov2017-v1.root","passedEvents",inUFTier2=inUFTier2),
            #Component("Data2017",dataTreeDir+"/DoubleMuon_Run2017-17Nov2017-v1.root","passedEvents",inUFTier2=inUFTier2),
            #Component("Data2017",dataTreeDir+"/SingleMuon_Run2017-17Nov2017-v1.root","passedEvents",inUFTier2=inUFTier2),
            Component("Data2017",dataTreeDir+"Data_Run2017_DoubleMuon-SingleMuon_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
            #Component("Data2017",dataTreeDir+"Data_Run2017_DoubleMuon-SingleMuon.root","passedEvents",inUFTier2=inUFTier2),

        ]
        )

Data2017 = Dataset(
        "Data2017",
        data2017_cmpList,
        isMC                = False,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ZPlusX
ZPlusX_cmpList = ComponentList(
        [
            Component("ZPlusX",dataTreeDir2+"Data_Run2017-17Nov2017_noDuplicates_FRWeightFromVukasinWZRemoved.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ZPlusX = Dataset(
        "ZPlusX",
        ZPlusX_cmpList,
        isMC                = True,
        skipWeight          = True,
        )


# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "qqZZTo4L",
        qqZZ_cmpList,
        isMC                = False,#True,
        #xs                  = 1.256,
        )
handleSumWeight(
        qqZZTo4L,
        system,
        bkgTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.txt",
        #bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ_M1To4
qqZZ_M1To4_cmpList = ComponentList(
        [ 
            Component("qqZZTo4L_M1To4",bkgSkimTreeDir2+"ZZTo4L_M-1toInf_13TeV_powheg_pythia8_Fall17.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L_M1To4 = Dataset(
        "qqZZTo4L_M1To4",
        qqZZ_M1To4_cmpList,
        isMC                = True,
        xs                  = 13.9, #13.74,
        )
handleSumWeight(
        qqZZTo4L_M1To4,
        system,
        bkgTreeDir2+"ZZTo4L_M-1toInf_13TeV_powheg_pythia8_Fall17.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir2+"ZZTo4L_M-1toInf_13TeV_powheg_pythia8_Fall17.txt",
        #bkgSkimTreeDir2+"ZZTo4L_M-1toInf_13TeV_powheg_pythia8_Fall17.txt",
        )


# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4tau",bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4tau = Dataset(
        "ggZZTo4tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
handleSumWeight(
        ggZZTo4tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.txt",
        #bkgSkimTreeDir+"GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4e
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4e",bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4e = Dataset(
        "ggZZTo4e",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
handleSumWeight(
        ggZZTo4e,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.txt",
        #bkgSkimTreeDir+"GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo4mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo4mu",bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo4mu = Dataset(
        "ggZZTo4mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.001586,
        )
handleSumWeight(
        ggZZTo4mu,
        system,
        bkgTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
        #bkgSkimTreeDir+"GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2mu2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2mu2tau",bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2mu2tau = Dataset(
        "ggZZTo2mu2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
handleSumWeight(
        ggZZTo2mu2tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.txt",
        #bkgSkimTreeDir+"GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2mu
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2mu",bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2mu = Dataset(
        "ggZZTo2e2mu",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
handleSumWeight(
        ggZZTo2e2mu,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.txt",
        #bkgSkimTreeDir+"GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggZZTo2e2tau
ggZZTo4L_cmpList = ComponentList(
        [ 
            Component("ggZZTo2e2tau",bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggZZTo2e2tau = Dataset(
        "ggZZTo2e2tau",
        ggZZTo4L_cmpList,
        isMC                = True,
        xs                  = 0.00319,
        )
handleSumWeight(
        ggZZTo2e2tau,
        system,
        bkgTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.txt",
        #bkgSkimTreeDir+"GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
ggH_cmpList = ComponentList(
        [ 
             Component("ggH",bkgSkimTreeDir2+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ggH = Dataset(
        "ggH",
        ggH_cmpList,
        isMC                = True,
        #xs                  = 0.01218,
        xs                  = 48.52*0.0002768,
        )
handleSumWeight(
        ggH,
        system,
        bkgTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir2+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        #bkgSkimTreeDir+"GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# VBF
VBF_cmpList = ComponentList(
        [ 
            Component("VBF",bkgSkimTreeDir2+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

VBF = Dataset(
        "VBF",
        VBF_cmpList,
        isMC                = True,
        xs                  = 0.001044,
        )
handleSumWeight(
        VBF,
        system,
        bkgTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir2+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        #bkgSkimTreeDir+"VBF_HToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHplus
WHplus_cmpList = ComponentList(
        [ 
            Component("WHplus",bkgSkimTreeDir2+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHplus = Dataset(
        "WHplus",
        WHplus_cmpList,
        isMC                = True,
        xs                  = 0.000232,
        )
handleSumWeight(
        WHplus,
        system,
        bkgTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir2+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
        #bkgSkimTreeDir+"WplusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# WHminus
WHminus_cmpList = ComponentList(
        [ 
            Component("WHminus",bkgSkimTreeDir2+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

WHminus = Dataset(
        "WHminus",
        WHminus_cmpList,
        isMC                = True,
        xs                  = 0.000147,
        )
handleSumWeight(
        WHminus,
        system,
        bkgTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir2+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
        #bkgSkimTreeDir+"WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ZH
ZH_cmpList = ComponentList(
        [ 
            Component("ZH",bkgSkimTreeDir2+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ZH = Dataset(
        "ZH",
        ZH_cmpList,
        isMC                = True,
        xs                  = 0.000668,
        )
handleSumWeight(
        ZH,
        system,
        bkgTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir2+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.txt",
        #bkgSkimTreeDir+"ZH_HToZZ_4LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||
# ttH
ttH_cmpList = ComponentList(
        [ 
            Component("ttH",bkgSkimTreeDir2+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUGenV7011_pythia8.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

ttH = Dataset(
        "ttH",
        ttH_cmpList,
        isMC                = True,
        xs                  = 0.000337,
        )
handleSumWeight(
        ttH,
        system,
        bkgTreeDir+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUGenV7011_pythia8.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        bkgSkimTreeDir2+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        #bkgSkimTreeDir+"ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUGenV7011_pythia8.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||

bkgSamples = [
        #ggH,
        #VBF,
        #WHplus,
        #WHminus,
        #ZH,
        #ttH,
        qqZZTo4L,
        #ggZZTo2e2mu,
        #ggZZTo2e2tau,
        #ggZZTo2mu2tau,
        #ggZZTo4e,
        #ggZZTo4mu,
        #ggZZTo4tau,
        qqZZTo4L_M1To4,
        #ZPlusX,
        ]
dataSamples = [
        Data2017,
        ]
