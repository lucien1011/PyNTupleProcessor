# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 

from RPV.Dataset.Moriond17 import *
from RPV.Producer.PhysObjProducer import mediumMuonProducer,looseMuonProducer,mediumElectronProducer,looseElectronProducer,jetProducer
from RPV.Analyzer.ExampleAnalyzer import ExampleAnalyzer

nCores = 1 
outputDir = "./Log/" # Change this to the directory you want! 
nEvents = -1
disableProgressBar = False

sequence = Sequence()
sequence.add(mediumMuonProducer)
sequence.add(looseMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(looseElectronProducer)
sequence.add(jetProducer)
sequence.add(ExampleAnalyzer("ExampleAnalyzer"))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"

componentList = [
        #TTJetsDiLep_cmp,
        #TTJetsSingleLepFromT_cmp,
        #TTJetsSingleLepFromTbar_cmp,
        #WJetsToLNu_cmp,
        T1tbs2000_cmp,
        ]

