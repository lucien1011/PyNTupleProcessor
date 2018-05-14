# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Dataset.NanoAOD_2016MC import *

#from RPV.Producer.PhysObjProducer import mediumMuonProducer,looseMuonProducer,mediumElectronProducer,looseElectronProducer,jetProducer
#from RPV.Analyzer.Plotter.Plotter import Plotter
#from RPV.Analyzer.Plotter.PlotDefinition import allPlots

nCores = 1 
outputDir = "/raid/raid7/lucien/SUSY/RA5/Log/Test_UF-PyNTupleRunner/2018-05-11/test1/"
nEvents = -1
disableProgressBar = False

sequence = Sequence()
#sequence.add(mediumMuonProducer)
#sequence.add(looseMuonProducer)
#sequence.add(mediumElectronProducer)
#sequence.add(looseElectronProducer)
#sequence.add(jetProducer)
#sequence.add(Plotter("Plotter",allPlots))

endSequence = EndSequence()

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"

componentList = [
        DYJetsToLL_M10to50,
        #TTJetsDiLep_cmp,
        #TTJetsSingleLepFromT_cmp,
        #TTJetsSingleLepFromTbar_cmp,
        #WJetsToLNu_cmp,
        #T1tbs2000_cmp,
        ]

