# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 

from Core.NanoAODResult.Component import Component

from RPV.Producer.PhysObjProducer import mediumMuonProducer,looseMuonProducer,mediumElectronProducer,looseElectronProducer,jetProducer

nCores = 1 
outputDir = "/raid/raid7/lucien/SUSY/RPV/Log/Test_UF-PyNTupleRunner/2018-02-27/test1/"
nEvents = -1
disableProgressBar = False

sequence = Sequence()
sequence.add(mediumMuonProducer)
sequence.add(looseMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(looseElectronProducer)
sequence.add(jetProducer)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"

TTJetsDiLep_cmp = Component(
        "/cms/data/store/user/klo/RPV-Moriond17v10/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Moriond17v10/180226_210416/0000/",
        "TTJetsDiLep",
        )

TTJetsSingleLepFromT_cmp = Component(
        "/cms/data/store/user/klo/RPV-Moriond17v10/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Moriond17v10/180226_210717/0000/",
        "TTJetsSingleLepFromT",
        )

TTJetsSingleLepFromTbar_cmp = Component(
        "/cms/data/store/user/klo/RPV-Moriond17v10/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Moriond17v10/180226_211033/0000/",
        "TTJetsSingleLepFromTbar",
        )

WJetsToLNu_cmp = Component(
        "/cms/data/store/user/klo/RPV-Moriond17v10/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Moriond17v10/180226_212215/0000/",
        "TTJetsDiLep",
        )

T1tbs2000_cmp = Component(
        "/cms/data/store/user/klo/RPV-Moriond17v10/SMS-T1tbs_RPV_mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/Moriond17v10/180226_215452/0000/",
        "T1tbs-mGluino2000",     
        )

componentList = [
        TTJetsDiLep_cmp,
        TTJetsSingleLepFromT_cmp,
        TTJetsSingleLepFromTbar_cmp,
        WJetsToLNu_cmp,
        T1tbs2000_cmp,
        ]

