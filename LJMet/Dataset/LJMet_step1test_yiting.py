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
			sumw		= nRun[sigName],
			)
	sigSamples.append(tmpDataset)

