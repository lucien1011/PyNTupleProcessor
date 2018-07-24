# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 
#from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
#from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc

import os

#from DataMC.Heppy.Run2016.SampleDefinition import * 
from RA5.Dataset.Run2016 import *

from NanoAOD.Producer.GenWeightCounter import *

#out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/MCDistribution/2018-07-20/"

nCores = 1 
#outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
outputDir = "./test_plot/"
nEvents = -1
disableProgressBar = False
justEndSequence = False
verbose = True
componentList = allMCSamples
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = [
        Plot("nJet40",      ["TH1D","nJet40","",10,-0.5,9.5],       LambdaFunc('x: x.nJetSel[0]')),
        Plot("nBJet40",     ["TH1D","nBJet40","",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMedium40[0]')),
        Plot("htJet",        ["TH1D","htJet","",10,0.,1000.],         LambdaFunc('x: x.htJet40[0]')),
        Plot("met_pt",         ["TH1D","met_pt","",10,0., 500.],          LambdaFunc('x: x.met_pt[0]')),
        Plot("met_phi",         ["TH1D","met_phi","",5,0., 5.],          LambdaFunc('x: x.met_phi[0]')),
        Plot("mht",         ["TH1D","mht","",10,0., 500.],          LambdaFunc('x: x.mhtJet40[0]')),
        ]
plotter                 = Plotter("Plotter",plots)
leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
xsWeighter              = XSWeighter("XSWeighter")
#baselineSkimmer         = BaselineSkimmer("BaselineSkimmer")
#signalRegionSkimmer     = SignalRegionSkimmer("SignalRegionSkimmer")

sequence = Sequence()
#sequence.add(leptonJetProducer)
sequence.add(xsWeighter)
#sequence.add(baselineSkimmer)
sequence.add(plotter)

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = "/home/kshi/public_html/RA5/mcPlot/"
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "MCDistributions.root"
