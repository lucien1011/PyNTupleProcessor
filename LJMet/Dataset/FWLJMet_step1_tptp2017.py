from Core.ComponentList import *
from Core.Dataset import Dataset

from LJMet.Dataset.FWLJMet_weights_step1_tptp2017 import *
from LJMet.Dataset.FWLJMet_samples_step1_tptp2017 import *

import os

# ____________________________________________________________________________________________________________________________________________ ||
#dir_prefix	        = "root://cmseos.fnal.gov//store/user/yiting11/lpcljm_step1test/"
#dir_prefix	        = "~/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/2017/Feb/nominal/"
#dir_prefix_TTInc	= "~/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/2017/Feb_addNumCounter/nominal/"
#dir_prefix          = "root://cmseos.fnal.gov//store/user/lpcljm/yiting/2017/Feb_addNumCounter/nominal/"
#dir_prefix_TTInc    = "root://cmseos.fnal.gov//store/user/lpcljm/yiting/2017/Feb/nominal/"
dir_prefix          = "/uscms/home/yiting11/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/singleLep2017/FWLJMET/nominal/"
dir_prefix_TTInc    = "/uscms/home/yiting11/nobackup/CMSSW_9_4_6_patch1/src/LJMet-Slimmer/results/singleLep2017/FWLJMET/nominal/"
treeName	        = "ljmet"

#ntupleWhere         = '/eos/uscms/store/user/lpcljm/2018/LJMet94X_1lep_013019/nominal/'
ntupleWhere         = '/eos/uscms/store/user/lpcljm/FWLJMET102X_1lep2017_052219/'
#'root://cmseos.fnal.gov//store/user/lpcljm/2018/LJMet94X_1lep_013019/nominal/'
#txtWhere            = '/uscms/home/yiting11/nobackup/UF-PyNTupleRunner/LJMet/Dataset/txt/'
txtWhere            = os.environ['BASE_PATH']+'/LJMet/Dataset/FWLJMet_step1_tptp2017_txt/'

# ____________________________________________________________________________________________________________________________________________ ||
bkgList = [
        'DYMG200','DYMG400','DYMG600','DYMG800','DYMG1200','DYMG2500',
        #'DYMG200','DYMG400','DYMG600','DYMG800','DYMG2500',
        'WJetsMG200','WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',
        'TTJetsHad0',
        'TTJetsSemiLep0',
        'TTJets2L2nu0',
        'TTJetsPH700mtt','TTJetsPH1000mtt',
        'Ts','Tbs','Tt','Tbt','TtW','TbtW',
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
            tmpDataset.setSumWeightByDir(ntupleWhere+samples[bkgName].replace('_Mtt0to700','')+"*/*/*/*/",histPath="mcweightanalyzer/weightHist",verbose=True)
            tmpDataset.saveSumWeightToPath(txtFilePath)
        else:
            tmpDataset.setSumWeightByTxt(txtFilePath)
        tmpDataset.sumw *= 0.8832
    else:
        if not os.path.isfile(txtWhere+samples[bkgName]+'.txt'):
            tmpDataset.setSumWeightByDir(ntupleWhere+samples[bkgName]+"*/*/*/*/",histPath="mcweightanalyzer/weightHist",verbose=True)
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

