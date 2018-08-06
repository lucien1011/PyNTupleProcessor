from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2017.SkimTree import * 
#from DarkZ.Dataset.Run2017.SkimTree_SMHiggs import * 

from DarkZ.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from DarkZ.Skimmer.BlindSkimmer import BlindSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "MCDistributions/MC_BaselineSelection_v1/2018-07-02/"
#out_path = "DataMCDistributions/SkimTree_SignalSelection_v2/2018-07-30/"
out_path = "DataMCDistributions/SkimTree_SignalSelection_v3/2018-08-03/"
#out_path = "DataMCDistributions/SkimTree_HiggsTo4L-m4l118To130Selection_v2/2018-07-30/"
#out_path = "DataMCDistributions/Dibug_passFullSelection/2018-07-30/"

muon_plots = [
        Plot("LeadingLepton_pt", ["TH1D","LeadingLepton_pt","",20,0.,200.], LambdaFunc('x: max([ x.pTL1[0], x.pTL2[0], x.pTL3[0], x.pTL4[0] ])')),
        
        Plot("Muon1_Pt", ["TH1D","Muon1_pt","",20,0.,200.], LambdaFunc('x: [x.pTL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Pt", ["TH1D","Muon2_pt","",20,0.,100.], LambdaFunc('x: [x.pTL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Pt", ["TH1D","Muon3_pt","",20,0.,100.], LambdaFunc('x: [x.pTL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Pt", ["TH1D","Muon4_pt","",20,0.,50.],  LambdaFunc('x: [x.pTL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        
        Plot("Muon1_Eta", ["TH1D","Muon1_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Eta", ["TH1D","Muon2_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Eta", ["TH1D","Muon3_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Eta", ["TH1D","Muon4_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        
        Plot("Muon1_Phi", ["TH1D","Muon1_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL1[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon2_Phi", ["TH1D","Muon2_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL2[0]] if abs(x.idL2[0]) == 13 else []'), isCollection=True),
        Plot("Muon3_Phi", ["TH1D","Muon3_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL3[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),
        Plot("Muon4_Phi", ["TH1D","Muon4_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL4[0]] if abs(x.idL1[0]) == 13 else []'), isCollection=True),

        Plot("Electron1_Pt", ["TH1D","Electron1_pt","",20,0.,200.], LambdaFunc('x: [x.pTL1[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron2_Pt", ["TH1D","Electron2_pt","",20,0.,100.], LambdaFunc('x: [x.pTL2[0]] if abs(x.idL2[0]) == 11 else []'), isCollection=True),
        Plot("Electron3_Pt", ["TH1D","Electron3_pt","",20,0.,100.], LambdaFunc('x: [x.pTL3[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron4_Pt", ["TH1D","Electron4_pt","",20,0.,50.],  LambdaFunc('x: [x.pTL4[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        
        Plot("Electron1_Eta", ["TH1D","Electron1_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL1[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron2_Eta", ["TH1D","Electron2_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL2[0]] if abs(x.idL2[0]) == 11 else []'), isCollection=True),
        Plot("Electron3_Eta", ["TH1D","Electron3_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL3[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron4_Eta", ["TH1D","Electron4_eta","",20,-3.,3.], LambdaFunc('x: [x.etaL4[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        
        Plot("Electron1_Phi", ["TH1D","Electron1_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL1[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron2_Phi", ["TH1D","Electron2_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL2[0]] if abs(x.idL2[0]) == 11 else []'), isCollection=True),
        Plot("Electron3_Phi", ["TH1D","Electron3_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL3[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        Plot("Electron4_Phi", ["TH1D","Electron4_phi","",20,-5.,5.], LambdaFunc('x: [x.phiL4[0]] if abs(x.idL1[0]) == 11 else []'), isCollection=True),
        ]

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [30,0.,60.]
#h4lPlotRange = [110,60.,500.]
h4lPlotRange = [20,100.,140.]
general_plots = [
        Plot("Z1_mass",     ["TH1D","Z1_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       ),
        Plot("Z2_mass",     ["TH1D","Z2_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'),       ),
        Plot("Z1_4e_mass",     ["TH1D","Z1_4e_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')      ),
        Plot("Z2_4e_mass",     ["TH1D","Z2_4e_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')     ),
        Plot("Z1_4mu_mass",     ["TH1D","Z1_4mu_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')      ),
        Plot("Z2_4mu_mass",     ["TH1D","Z2_4mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')     ),
        Plot("Z1_2e2mu_mass",     ["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')      ),
        Plot("Z2_2e2mu_mass",     ["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')     ),
              
        Plot("h4L_mass",    ["TH1D","h4L_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'),       ),
        Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')       ),
        Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')       ),
        Plot("h2e2mu_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')       ),
        Plot("h4L_Pt",      ["TH1D","h4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
        
        Plot("met",         ["TH1D","met","",40,0.,200.],       LambdaFunc('x: x.met[0]'),          ),
        Plot("nVtx",        ["TH1D","nVtx","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]')),
        Plot("nVtx_4mu",        ["TH1D","nVtx_4mu","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
        Plot("nVtx_4e",        ["TH1D","nVtx_4e","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
        Plot("nVtx_2e2mu",        ["TH1D","nVtx_2e2mu","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')),
        ]

jet_plots = [
        Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

plots = muon_plots + general_plots + jet_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [data2017]
#componentList           = [data2017]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 41.4
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = Sequence()
dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")
anaSkimmer              = AnalysisSkimmer("AnalysisSkimmer")
bliSkimmer              = BlindSkimmer("BlindSkimmer")
plotter                 = Plotter("Plotter",plots)

sequence.add(anaSkimmer)
sequence.add(bliSkimmer)
sequence.add(xsWeighter)
sequence.add(nloWeighter)
sequence.add(dataMCWeighter)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
