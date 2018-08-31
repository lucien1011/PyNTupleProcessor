from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.MC import * 
from DarkZ.Dataset.Run2017.Data import * 
from DarkZ.Dataset.Run2017.BkgMC import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
#from DarkZ.Dataset.Run2017.SkimTree import * 

#from DarkZ.Skimmer.Preskimmer import GENPreskimmer
#from DarkZ.Skimmer.FiducialSkimmer import FiducialSkimmer
from DarkZ.Skimmer.RecoSkimmer import RecoSkimmer
from DarkZ.Skimmer.BlindSkimmer import BlindSkimmer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "MCDistributions/MC_BaselineSelection_v1/2018-07-09/"
out_path = "DataMCDistributions/MC_HiggsTo4LSelection_v1/2018-07-26/"

lepton_plots = [
        Plot("Lepton1_Pt", ["TH1D","Lepton1_pt","",20,0.,200.], LambdaFunc('x: x.Z1.lep1.vec.Pt()'),),
        Plot("Lepton2_Pt", ["TH1D","Lepton2_pt","",20,0.,100.], LambdaFunc('x: x.Z1.lep2.vec.Pt()'),),
        Plot("Lepton3_Pt", ["TH1D","Lepton3_pt","",20,0.,100.], LambdaFunc('x: x.Z2.lep1.vec.Pt()'),),
        Plot("Lepton4_Pt", ["TH1D","Lepton4_pt","",20,0.,50.],  LambdaFunc('x: x.Z2.lep2.vec.Pt()'),),
        
        Plot("Lepton1_Eta", ["TH1D","Lepton1_eta","",20,-3.,3.], LambdaFunc('x: x.Z1.lep1.vec.Eta()'),),
        Plot("Lepton2_Eta", ["TH1D","Lepton2_eta","",20,-3.,3.], LambdaFunc('x: x.Z1.lep2.vec.Eta()'),),
        Plot("Lepton3_Eta", ["TH1D","Lepton3_eta","",20,-3.,3.], LambdaFunc('x: x.Z2.lep1.vec.Eta()'),),
        Plot("Lepton4_Eta", ["TH1D","Lepton4_eta","",20,-3.,3.], LambdaFunc('x: x.Z2.lep2.vec.Eta()'),),
        
        Plot("Lepton1_Phi", ["TH1D","Lepton1_phi","",20,-5.,5.], LambdaFunc('x: x.Z1.lep1.vec.Phi()'),),
        Plot("Lepton2_Phi", ["TH1D","Lepton2_phi","",20,-5.,5.], LambdaFunc('x: x.Z1.lep2.vec.Phi()'),),
        Plot("Lepton3_Phi", ["TH1D","Lepton3_phi","",20,-5.,5.], LambdaFunc('x: x.Z2.lep1.vec.Phi()'),),
        Plot("Lepton4_Phi", ["TH1D","Lepton4_phi","",20,-5.,5.], LambdaFunc('x: x.Z2.lep2.vec.Phi()'),),
            
        ]

general_plots = [
        Plot("Z1_mass",         ["TH1D","Z1_mass","",110,40.,110.],   LambdaFunc('x: x.Z1.vec.M()'),       ),
        Plot("Z2_mass",         ["TH1D","Z2_mass","",100,0.,65.],   LambdaFunc('x: x.Z2.vec.M()'),       ),
        Plot("h4L_mass",        ["TH1D","4L_mass","",25,110.,140.], LambdaFunc('x: x.hmass'),           ),
        Plot("h4L_Pt",          ["TH1D","4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
        Plot("met",             ["TH1D","met","",40,0.,200.],       LambdaFunc('x: x.met[0]'),          ),
        Plot("nVtx",            ["TH1D","nVtx","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]')),        
        Plot("Z1mass_vs_Z2mass",["TH2D","Z1mass_vs_Z2mass","",110,40.,110.,100,0.,65.], LambdaFunc('x: [x.Z1.vec.M(),x.Z2.vec.M(),]'),dim=2),
        ]

jet_plots = [
        #Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

plots = lepton_plots + general_plots + jet_plots
for plot in plots:
    plot.plotSetting.divideByBinWidth = True

nCores                  = 8
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSamples + [data2017]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 77.30
        dataset.lumi = 41.4
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = Sequence()
xsWeighter              = XSWeighter("XSWeighter")
recoSkimmer             = RecoSkimmer("RecoSkimmer")
blindSkimmer            = BlindSkimmer("BlindSkimmer")
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
#recoSkimmer.Z2MassRange = [4.,120.]
plotter                 = Plotter("Plotter",plots)

sequence.add(recoSkimmer)
sequence.add(blindSkimmer)
sequence.add(xsWeighter)
sequence.add(dataMCWeighter)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "MCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
