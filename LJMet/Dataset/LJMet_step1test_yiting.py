from Core.ComponentList import *
from Core.Dataset import Dataset

from LJMet.Dataset.weights import *
from LJMet.Dataset.samples import *

# ____________________________________________________________________________________________________________________________________________ ||
dir_prefix	= "root://cmseos.fnal.gov//store/user/yiting11/lpcljm_step1test/"
treeName	= "ljmet"

# ____________________________________________________________________________________________________________________________________________ ||
bkgList = [
	'DY',
	'WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',
	'TTJetsHad0','TTJetsHad700','TTJetsHad1000',
	'TTJetsSemiLep0','TTJetsSemiLep700','TTJetsSemiLep1000',
	'TTJets2L2nu0','TTJets2L2nu700','TTJets2L2nu1000',
	'TTJetsPH700mtt','TTJetsPH1000mtt',
	'Ts','Tt','Tbt','TtW','TbtW','TTWl','TTZl',
	'QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
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
			sumw		= nRun[bkgName],
			)
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
            'TTM1200BWBW',
        ]
sigXSDict = {
        'TTM1200BWBW': 'TTM1200',
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
			sumw		= nRun[sigName],
			)
	sigSamples.append(tmpDataset)

