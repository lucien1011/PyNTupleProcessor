# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Weighter.XSWeighter import XSWeighter
from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc

import os

from DataMC.Heppy.Run2016.HaddMC import * 
from DataMC.Heppy.Run2016.SampleDefinition import * 

out_path = "HeppyValidation/2018-07-13/"

nCores = 2
outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
nEvents = -1
disableProgressBar = False
justEndSequence = False
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = [
        Plot("nLepGood",      ["TH1D","nLepGood","",10,-0.5,9.5],       LambdaFunc('x: x.nLepGood[0]')),
        #Plot("nLepLoose_Mini",      ["TH1D","nLepLoose_Mini","",10,-0.5,9.5],       LambdaFunc('x: x.nLepLoose_Mini[0]')),
        #Plot("nLepFO_Mini",      ["TH1D","nLepFO_Mini","",10,-0.5,9.5],       LambdaFunc('x: x.nLepFO_Mini[0]')),
        #Plot("nLepFOVeto_Mini",      ["TH1D","nLepFOVeto_Mini","",10,-0.5,9.5],       LambdaFunc('x: x.nLepFOVeto_Mini[0]')),
        #Plot("nTauSel_Mini",      ["TH1D","nTauSel_Mini","",10,-0.5,9.5],       LambdaFunc('x: x.nTauSel_Mini[0]')),
        #Plot("nJet40_Mini",      ["TH1D","nJet40_Mini","",10,-0.5,9.5],       LambdaFunc('x: x.nJet40_Mini[0]')),
        #Plot("nBJetMedium25_Mini",      ["TH1D","nBJetMedium25_Mini","",10,-0.5,9.5],       LambdaFunc('x: x.nBJetMedium25_Mini[0]')),

        #Plot("minMllSFOS_Mini",      ["TH1D","minMllSFOS_Mini","",20,0.0,500.],       LambdaFunc('x: x.minMllSFOS_Mini[0]')),
        #Plot("htJet40j_Mini",      ["TH1D","htJet40j_Mini","",20,0.0,500.],       LambdaFunc('x: x.htJet40j_Mini[0]')),
        #Plot("mhtJet40_Mini",      ["TH1D","mhtJet40_Mini","",20,0.0,500.],       LambdaFunc('x: x.mhtJet40_Mini[0]')),
        #Plot("JetSel_Mini_pt",      ["TH1D","JetSel_Mini_pt","",10,0., 500.],       LambdaFunc('x: x.JetSel_Mini_pt'), isCollection=True),
        #Plot("JetSel_Mini_eta", ["TH1D","JetSel_Mini_eta","",20,-3.,3.], LambdaFunc('x: x.JetSel_Mini_eta'), isCollection=True),
        #Plot("JetSel_Mini_phi", ["TH1D","JetSel_Mini_phi","",20,-3.,3.], LambdaFunc('x: x.JetSel_Mini_phi'), isCollection=True),
        #Plot("JetSel_Mini_btagCSV", ["TH1D","JetSel_Mini_btagCSV","",20,0.,1.], LambdaFunc('x: x.JetSel_Mini_btagCSV'), isCollection=True),
        #Plot("JetSel_Mini_mass",      ["TH1D","JetSel_Mini_mass","",10,0., 200.],       LambdaFunc('x: x.JetSel_Mini_mass'), isCollection=True),
        ]
plotter                 = Plotter("Plotter",plots)
xsWeighter              = XSWeighter("XSWeighter")
baselineSkimmer         = BaselineSkimmer("BaselineSkimmer")
signalRegionSkimmer     = SignalRegionSkimmer("SignalRegionSkimmer")

sequence = Sequence()
sequence.add(xsWeighter)
#sequence.add(baselineSkimmer)
#sequence.add(signalRegionSkimmer)
sequence.add(plotter)

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "MCDistributions.root"
