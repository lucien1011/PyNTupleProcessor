# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Dataset.NanoAOD.Run2016 import * 

from RA5.Weighter.XSWeighter import XSWeighter

from RA5.Producer.PhysObjProducer import mediumMuonProducer,looseMuonProducer,mediumElectronProducer,looseElectronProducer,jetProducer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from RA5.Config.Plotter.PlotDefinition import allPlots

nCores = 4 
outputDir = "/raid/raid7/lucien/SUSY/RA5/Log/MCDistributions/2018-05-14/AllMCSamples_v1/"
nEvents = -1
disableProgressBar = False 
justEndSequence = False 
componentList = [WZTo3LNu] 
#componentList = allMCSamples
for dataset in componentList:
    dataset.lumi = 35.9

sequence = Sequence()
xsWeighter = XSWeighter("XSWeighter")
sequence.add(xsWeighter)
sequence.add(mediumMuonProducer)
sequence.add(looseMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(looseElectronProducer)
sequence.add(jetProducer)
sequence.add(Plotter("Plotter",allPlots))

endSequence = EndSequence()
endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/Log/MCDistributions/2018-05-14/AllMCSamples_v1/"
endSequence.add(PlotEndModule(endModuleOutputDir,allPlots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "MCDistributions.root"
