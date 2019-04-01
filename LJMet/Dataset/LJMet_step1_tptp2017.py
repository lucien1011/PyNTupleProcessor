from Core.ComponentList import *
from Core.Dataset import Dataset

from LJMet.Dataset.weights_step1_tptp2017 import *
from LJMet.Dataset.samples_step1_tptp2017 import *

# ____________________________________________________________________________________________________________________________________________ ||
#dir_prefix	        = "root://cmseos.fnal.gov//store/user/yiting11/lpcljm_step1test/"
dir_prefix	        = "~/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/2017/Feb/nominal/"
dir_prefix_TTInc	= "~/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/2017/Feb_addNumCounter/nominal/"
treeName	        = "ljmet"

ntupleWhere         = '/eos/uscms/store/user/lpcljm/2018/LJMet94X_1lep_013019/nominal/'
txtWhere            = '/uscms/home/yiting11/nobackup/UF-PyNTupleRunner/LJMet/Dataset/txt/'
# ____________________________________________________________________________________________________________________________________________ ||
bkgList = [
        'DY',
        'WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',
        'TTJetsHad0',
        'TTJetsSemiLep0',
        'TTJets2L2nu0',
        'TTJetsPH700mtt','TTJetsPH1000mtt',
        'Ts','Tt','Tbt','TtW','TbtW',
        'QCDht200','QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
        ]

bkgSamples = []
for bkgName in bkgList:
    tmpDataset = Dataset(
            bkgName,
            ComponentList(
                [
                    Component(bkgName,
                        dir_prefix+samples[bkgName]+".root",
                        treeName,
                        False,
                        ),
                    ]
                ),
            isMC		= True,
            xs			= xsec[bkgName],
            #sumw		= nRun[bkgName],
            )

    if bkgName == "TTJetsHad0" or bkgName == "TTJetsSemiLep0" or bkgName == "TTJets2L2nu0":
        tmpDataset.componentList[0].fileName = dir_prefix_TTInc+samples[bkgName]+".root"
        txtFilePath = txtWhere+samples[bkgName].replace('_Mtt0to700','')+'.txt'
        if not os.path.isfile(txtFilePath):
            tmpDataset.setSumWeightByDir(ntupleWhere+samples[bkgName].replace('_Mtt0to700',''),verbose=True)
            tmpDataset.saveSumWeightToPath(txtFilePath)
        else:
            tmpDataset.setSumWeightByTxt(txtFilePath)
        tmpDataset.sumw *= 0.8832
    else:
        if not os.path.isfile(txtWhere+samples[bkgName]+'.txt'):
            tmpDataset.setSumWeightByDir(ntupleWhere+samples[bkgName],verbose=True)
            tmpDataset.saveSumWeightToPath(txtWhere+samples[bkgName]+'.txt')
        else:
            tmpDataset.setSumWeightByTxt(txtWhere+samples[bkgName]+'.txt')

    bkgSamples.append(tmpDataset)

# ____________________________________________________________________________________________________________________________________________ ||
dataList = [
        'Data_SingleElectron',
        'Data_SingleMuon',
        ]

dataSamples = []
for dataName in dataList:
    tmpDataset = Dataset(
            dataName,
            ComponentList(
                [
                    Component(dataName,
                        dir_prefix+samples[dataName]+".root",
                        treeName,
                        False,
                        ),
                    ]
                ),
            isMC		= False,
            )
    dataSamples.append(tmpDataset)

# ____________________________________________________________________________________________________________________________________________ ||
sigList = [
        'TTM1100BWBW',
        'TTM1200BWBW',
        'TTM1300BWBW',
        'TTM1400BWBW',
        'TTM1500BWBW',
        'TTM1600BWBW',
        'TTM1700BWBW',
        'TTM1800BWBW',

        'TTM1100THBW',
        'TTM1200THBW',
        'TTM1300THBW',
        'TTM1400THBW',
        'TTM1500THBW',
        'TTM1600THBW',
        'TTM1700THBW',
        'TTM1800THBW',

        'TTM1100THTH',
        'TTM1200THTH',
        'TTM1300THTH',
        'TTM1400THTH',
        'TTM1500THTH',
        'TTM1600THTH',
        'TTM1700THTH',
        'TTM1800THTH',

        'TTM1100TZBW',
        'TTM1200TZBW',
        'TTM1300TZBW',
        'TTM1400TZBW',
        'TTM1500TZBW',
        'TTM1600TZBW',
        'TTM1700TZBW',
        'TTM1800TZBW',

        'TTM1100TZTH',
        'TTM1200TZTH',
        'TTM1300TZTH',
        'TTM1400TZTH',
        'TTM1500TZTH',
        'TTM1600TZTH',
        'TTM1700TZTH',
        'TTM1800TZTH',

        'TTM1100TZTZ',
        'TTM1200TZTZ',
        'TTM1300TZTZ',
        'TTM1400TZTZ',
        'TTM1500TZTZ',
'TTM1600TZTZ',
            'TTM1700TZTZ',
            'TTM1800TZTZ',

        ]
sigXSDict = {
        'TTM1100BWBW': 'TTM1100',
        'TTM1100THBW': 'TTM1100',
        'TTM1100THTH': 'TTM1100',
        'TTM1100TZBW': 'TTM1100',
        'TTM1100TZTH': 'TTM1100',
        'TTM1100TZTZ': 'TTM1100',

        'TTM1200BWBW': 'TTM1200',
        'TTM1200THBW': 'TTM1200',
        'TTM1200THTH': 'TTM1200',
        'TTM1200TZBW': 'TTM1200',
        'TTM1200TZTH': 'TTM1200',
        'TTM1200TZTZ': 'TTM1200',

        'TTM1300BWBW': 'TTM1300',
        'TTM1300THBW': 'TTM1300',
        'TTM1300THTH': 'TTM1300',
        'TTM1300TZBW': 'TTM1300',
        'TTM1300TZTH': 'TTM1300',
        'TTM1300TZTZ': 'TTM1300',

        'TTM1400BWBW': 'TTM1400',
        'TTM1400THBW': 'TTM1400',
        'TTM1400THTH': 'TTM1400',
        'TTM1400TZBW': 'TTM1400',
        'TTM1400TZTH': 'TTM1400',
        'TTM1400TZTZ': 'TTM1400',

        'TTM1500BWBW': 'TTM1500',
        'TTM1500THBW': 'TTM1500',
        'TTM1500THTH': 'TTM1500',
        'TTM1500TZBW': 'TTM1500',
        'TTM1500TZTH': 'TTM1500',
        'TTM1500TZTZ': 'TTM1500',

        'TTM1600BWBW': 'TTM1600',
        'TTM1600THBW': 'TTM1600',
        'TTM1600THTH': 'TTM1600',
        'TTM1600TZBW': 'TTM1600',
        'TTM1600TZTH': 'TTM1600',
        'TTM1600TZTZ': 'TTM1600',

        'TTM1700BWBW': 'TTM1700',
        'TTM1700THBW': 'TTM1700',
        'TTM1700THTH': 'TTM1700',
        'TTM1700TZBW': 'TTM1700',
        'TTM1700TZTH': 'TTM1700',
        'TTM1700TZTZ': 'TTM1700',

        'TTM1800BWBW': 'TTM1800',
'TTM1800THBW': 'TTM1800',
        'TTM1800THTH': 'TTM1800',
        'TTM1800TZBW': 'TTM1800',
        'TTM1800TZTH': 'TTM1800',
        'TTM1800TZTZ': 'TTM1800',

        }
sigSamples = []
for sigName in sigList:
    tmpDataset = Dataset(
            sigName,
            ComponentList(
                [
                    Component(sigName,
                        dir_prefix+samples[sigName]+".root",
                        treeName,
                        False,
                        ),
                    ]
                ),
            isMC		= True,
            xs			= xsec[sigXSDict[sigName]],
            #sumw		= nRun[sigName],
            )
    sigSamples.append(tmpDataset)

