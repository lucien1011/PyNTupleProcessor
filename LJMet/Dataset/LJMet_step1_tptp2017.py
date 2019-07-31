from Core.ComponentList import *
from Core.Dataset import Dataset

from LJMet.Dataset.weights_step1_tptp2017 import *
from LJMet.Dataset.samples_step1_tptp2017 import *

import os

# ____________________________________________________________________________________________________________________________________________ ||
#dir_prefix	        = "root://cmseos.fnal.gov//store/user/yiting11/lpcljm_step1test/"
#dir_prefix	        = "~/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/2017/Feb/nominal/"
#dir_prefix_TTInc	= "~/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/2017/Feb_addNumCounter/nominal/"
#dir_prefix          = "root://cmseos.fnal.gov//store/user/lpcljm/yiting/2017/Feb_addNumCounter/nominal/"
#dir_prefix_TTInc    = "root://cmseos.fnal.gov//store/user/lpcljm/yiting/2017/Feb/nominal/"
dir_prefix          = "/raid/raid7/lucien/LJMet/B2G/Step1NTuple/lpcljm_yiting_2017_Feb_addNumCounter/nominal/"
dir_prefix_TTInc    = "/raid/raid7/lucien/LJMet/B2G/Step1NTuple/lpcljm_yiting_2017_Feb_addNumCounter/nominal/"
treeName	        = "ljmet"

#ntupleWhere         = '/eos/uscms/store/user/lpcljm/2018/LJMet94X_1lep_013019/nominal/'
ntupleWhere         = 'root://cmseos.fnal.gov//store/user/lpcljm/2018/LJMet94X_1lep_013019/nominal/'
#txtWhere            = '/uscms/home/yiting11/nobackup/UF-PyNTupleRunner/LJMet/Dataset/txt/'
txtWhere            = os.environ['BASE_PATH']+'/LJMet/Dataset/txt/'

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
        'TT_M1100_BW-BW',
        'TT_M1200_BW-BW',
        'TT_M1300_BW-BW',
        'TT_M1400_BW-BW',
        'TT_M1500_BW-BW',
        'TT_M1600_BW-BW',
        'TT_M1700_BW-BW',
        'TT_M1800_BW-BW',

        'TT_M1100_TH-BW',
        'TT_M1200_TH-BW',
        'TT_M1300_TH-BW',
        'TT_M1400_TH-BW',
        'TT_M1500_TH-BW',
        'TT_M1600_TH-BW',
        'TT_M1700_TH-BW',
        'TT_M1800_TH-BW',

        'TT_M1100_TH-TH',
        'TT_M1200_TH-TH',
        'TT_M1300_TH-TH',
        'TT_M1400_TH-TH',
        'TT_M1500_TH-TH',
        'TT_M1600_TH-TH',
        'TT_M1700_TH-TH',
        'TT_M1800_TH-TH',

        'TT_M1100_TZ-BW',
        'TT_M1200_TZ-BW',
        'TT_M1300_TZ-BW',
        'TT_M1400_TZ-BW',
        'TT_M1500_TZ-BW',
        'TT_M1600_TZ-BW',
        'TT_M1700_TZ-BW',
        'TT_M1800_TZ-BW',

        'TT_M1100_TZ-TH',
        'TT_M1200_TZ-TH',
        'TT_M1300_TZ-TH',
        'TT_M1400_TZ-TH',
        'TT_M1500_TZ-TH',
        'TT_M1600_TZ-TH',
        'TT_M1700_TZ-TH',
        'TT_M1800_TZ-TH',

        'TT_M1100_TZ-TZ',
        'TT_M1200_TZ-TZ',
        'TT_M1300_TZ-TZ',
        'TT_M1400_TZ-TZ',
        'TT_M1500_TZ-TZ',
        'TT_M1600_TZ-TZ',
        'TT_M1700_TZ-TZ',
        'TT_M1800_TZ-TZ',

        ]

br_Tprime = 1./3.
sigSamples = []
sigDict = {}
for sigName in sigList:
    prodType,massStr,decayType = sigName.split("_")
    decay1,decay2 = decayType.split("-")
    if decay1 == decay2:
        br = br_Tprime**2
    else:
        br = br_Tprime**2*2
    ljmetSigName = "".join([prodType,massStr,decay1,decay2])
    tmpDataset = Dataset(
            sigName,
            ComponentList(
                [
                    Component(sigName,
                        dir_prefix+samples[ljmetSigName]+".root",
                        treeName,
                        False,
                        ),
                    ]
                ),
            isMC		= True,
            xs			= xsec[prodType+massStr],
            #sumw		= nRun[sigName],
            isSignal    = True,
            )
    tmpDataset.setSumWeight(
                        dir_prefix+samples[ljmetSigName]+".root",
                        "nevents",
                        )
    tmpDataset.sumw *= br
    sigSamples.append(tmpDataset)
    sigDict[sigName] = tmpDataset

