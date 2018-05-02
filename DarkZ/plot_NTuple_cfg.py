from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.SkimTree import bkg_cmps,sig_cmps 
from DarkZ.Producer.EventWeightProducer import EventWeightProducer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

muon_plots = [
        Plot("Muon1_Pt", ["TH1D","Muon1_pt","",20,0.,200.], LambdaFunc('x: [x.pTL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Pt", ["TH1D","Muon2_pt","",20,0.,200.], LambdaFunc('x: [x.pTL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Pt", ["TH1D","Muon3_pt","",20,0.,200.], LambdaFunc('x: [x.pTL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Pt", ["TH1D","Muon4_pt","",20,0.,200.], LambdaFunc('x: [x.pTL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        
        Plot("Muon1_Eta", ["TH1D","Muon1_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Eta", ["TH1D","Muon2_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Eta", ["TH1D","Muon3_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Eta", ["TH1D","Muon4_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        ]

general_plots = [
        Plot("Z1_mass",     ["TH1D","Z1_mass","",20,55.,125.],  LambdaFunc('x: x.massZ1[0]'),       ),
        Plot("Z2_mass",     ["TH1D","Z2_mass","",40,0.,120.],   LambdaFunc('x: x.massZ2[0]'),       ),
        Plot("h4L_mass",    ["TH1D","4L_mass","",40,0.,200.],   LambdaFunc('x: x.mass4l[0]'),       ),
        Plot("h4L_Pt",      ["TH1D","4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
        Plot("met",         ["TH1D","met","",40,0.,200.],       LambdaFunc('x: x.met[0]'),          ),
        ]

jet_plots = [
        Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

plots = muon_plots + general_plots + jet_plots

nCores                  = 3 
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ-Ana/Log/MC_distribution/2018-04-26/Plots_v1/"
nEvents                 = -1
disableProgressBar      = False
componentList           = bkg_cmps + sig_cmps
rootTree                = "passedEvents"
justEndSequence         = False

sequence                = Sequence()
eventWeightProducer     = EventWeightProducer('EventWeightProducer',35.9)
sequence.add(eventWeightProducer)
plotter                 = Plotter("Plotter",plots)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "Plotter.root"

endSequence = EndSequence()
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ-Ana/Log/MC_distribution/2018-04-26/Plots_v1/"
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
