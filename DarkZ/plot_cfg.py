from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.MC import * 
from DarkZ.Dataset.Run2017.BkgMC import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
#from DarkZ.Dataset.Run2017.SkimTree import * 

#from DarkZ.Skimmer.Preskimmer import GENPreskimmer
#from DarkZ.Skimmer.FiducialSkimmer import FiducialSkimmer
from DarkZ.Skimmer.RecoSkimmer import RecoSkimmer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

out_path = "MCDistributions/MC_BaselineSelection_v1/2018-07-09/"
#out_path = "MCDistributions/MC_HiggsTo4LSelection_v1/2018-07-09/"

muon_plots = [
        Plot("Muon1_Pt", ["TH1D","Muon1_pt","",20,0.,200.], LambdaFunc('x: x.Z1.lep1.vec.Pt()'),),
        Plot("Muon2_Pt", ["TH1D","Muon2_pt","",20,0.,100.], LambdaFunc('x: x.Z1.lep2.vec.Pt()'),),
        Plot("Muon3_Pt", ["TH1D","Muon3_pt","",20,0.,100.], LambdaFunc('x: x.Z2.lep1.vec.Pt()'),),
        Plot("Muon4_Pt", ["TH1D","Muon4_pt","",20,0.,50.],  LambdaFunc('x: x.Z2.lep2.vec.Pt()'),),
        
        Plot("Muon1_Eta", ["TH1D","Muon1_eta","",20,-3.,3.], LambdaFunc('x: x.Z1.lep1.vec.Eta()'),),
        Plot("Muon2_Eta", ["TH1D","Muon2_eta","",20,-3.,3.], LambdaFunc('x: x.Z1.lep2.vec.Eta()'),),
        Plot("Muon3_Eta", ["TH1D","Muon3_eta","",20,-3.,3.], LambdaFunc('x: x.Z2.lep1.vec.Eta()'),),
        Plot("Muon4_Eta", ["TH1D","Muon4_eta","",20,-3.,3.], LambdaFunc('x: x.Z2.lep2.vec.Eta()'),),
        
        Plot("Muon1_Phi", ["TH1D","Muon1_phi","",20,-5.,5.], LambdaFunc('x: x.Z1.lep1.vec.Phi()'),),
        Plot("Muon2_Phi", ["TH1D","Muon2_phi","",20,-5.,5.], LambdaFunc('x: x.Z1.lep2.vec.Phi()'),),
        Plot("Muon3_Phi", ["TH1D","Muon3_phi","",20,-5.,5.], LambdaFunc('x: x.Z2.lep1.vec.Phi()'),),
        Plot("Muon4_Phi", ["TH1D","Muon4_phi","",20,-5.,5.], LambdaFunc('x: x.Z2.lep2.vec.Phi()'),),
            
        ]

general_plots = [
        Plot("Z1_mass",     ["TH1D","Z1_mass","",30,0.,150.],   LambdaFunc('x: x.Z1.vec.M()'),       ),
        Plot("Z2_mass",     ["TH1D","Z2_mass","",30,0.,150.],   LambdaFunc('x: x.Z2.vec.M()'),       ),
        Plot("h4L_mass",    ["TH1D","4L_mass","",25,100.,150.], LambdaFunc('x: x.hmass'),           ),
        #Plot("h4L_Pt",      ["TH1D","4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
        #Plot("met",         ["TH1D","met","",40,0.,200.],       LambdaFunc('x: x.met[0]'),          ),
        #Plot("nVtx",        ["TH1D","nVtx","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]')),
        ]

jet_plots = [
        #Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

plots = muon_plots + general_plots + jet_plots
for plot in plots:
    plot.plotSetting.divideByBinWidth = True

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSamples
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 77.30
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = Sequence()
xsWeighter              = XSWeighter("XSWeighter")
recoSkimmer             = RecoSkimmer("RecoSkimmer")
recoSkimmer.Z1MassRange = [80.,100.]
recoSkimmer.Z2MassRange = [15.,115.]
recoSkimmer.m4lCut      = [115.,130.]
plotter                 = Plotter("Plotter",plots)

sequence.add(xsWeighter)
sequence.add(recoSkimmer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "MCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
