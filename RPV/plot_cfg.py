#UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from NanoAOD.Weighter.XSWeighter import XSWeighter

from RPV.Producer.PhysObjProducer import PhysObjProducer,JetProducer 
from RPV.Producer.AnalysisProducer import AnalysisProducer 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc


useSkimTree = True
if useSkimTree:
    from RPV.SkimTree.NanoAOD.Run2016.MC import *
else:
    from DataMC.NanoAOD.Run2016 import * 

nCores = 8
outputDir = "./testPlot_v1/"
nEvents = -1
disableProgressBar = False 
justEndSequence = False
ratio_switch = True
componentList = allMCSamples 
for dataset in componentList:
    dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

mc_plots = [
        Plot("nJet40",      ["TH1D","nJet40","",10,-0.5,9.5],       LambdaFunc('x: x.nJet40')),
        Plot("nBJet25",     ["TH1D","nBJet25","",10,-0.5,9.5],      LambdaFunc('x: len([j for j in x.LooseJets if j.btagCSVV2 > 0.8484])')),
        Plot("nLep40",      ["TH1D","nLep40","",10,-0.5,9.5],       LambdaFunc('x: x.nLep40')),
        Plot("met",         ["TH1D","met","",10,0., 500.],          LambdaFunc('x: x.MET_pt[0]')),
        Plot("ht40",        ["TH1D","ht40","",10,0.,1000.],         LambdaFunc('x: x.ht40')),
        Plot("mll",         ["TH1D","mll","",16,0.,800.],           LambdaFunc('x: x.mll if x.mll else -1.')),
        Plot("jetPt1",      ["TH1D","jetPt1","",10,0., 500.],       LambdaFunc('x: x.jets[0].pt if len(x.jets) > 0 else -1')),
        Plot("jetPt2",      ["TH1D","jetPt2","",10,0., 500.],       LambdaFunc('x: x.jets[1].pt if len(x.jets) > 1 else -1')),
        Plot("muonPt1",     ["TH1D","muonPt1","",10,0., 500.],      LambdaFunc('x: x.muons[0].pt if len(x.muons) > 0 else -1')),
        Plot("muonPt2",     ["TH1D","muonPt2","",10,0., 500.],      LambdaFunc('x: x.muons[1].pt if len(x.muons) > 1 else -1')),
        Plot("elePt1",      ["TH1D","elePt1","",10,0., 500.],       LambdaFunc('x: x.eles[0].pt if len(x.eles) > 0 else -1')),
        Plot("elePt2",      ["TH1D","elePt2","",10,0., 500.],       LambdaFunc('x: x.eles[1].pt if len(x.eles) > 1 else -1')),
        

        Plot("m0_bl",       ["TH1D","m0_bl1","",16,0., 800.],       LambdaFunc('x: x.m0_bl[0]')),
        Plot("m0_bl_peaktest", ["TH1D","m0_bl1_peaktest","",20,100., 175.], LambdaFunc('x: x.m0_bl[0] if x.m0_bl[0] > 100 and x.m0_bl[0] < 175 else -1')),
	#Plot("m0_bl2",       ["TH1D","m0_bl2","",50,0., 1200.],       LambdaFunc('x: x.m0_bl[1]')),
        Plot("m1_bl",       ["TH1D","m1_bl1","",16,0., 800.],       LambdaFunc('x: x.m1_bl[0]')),
        Plot("m1_bl_peaktest", ["TH1D","m1_bl1_peaktest","",20,100., 175.], LambdaFunc('x: x.m1_bl[0] if x.m1_bl[0] > 100 and x.m1_bl[0] < 175 else -1')),
	#Plot("m1_bl2",       ["TH1D","m1_bl2","",50,0., 1200.],       LambdaFunc('x: x.m1_bl[1]')),
        Plot("m_asym_bl",    ["TH1D","m_asym_bl","",20,0., 1.],       LambdaFunc('x: x.m_asym_bl[0]')),
        Plot("m_ct",         ["TH1D","m_ct","",16,0., 800.],         LambdaFunc('x: x.m_ct[0]')),
        ]

ratio_plots = [
	 Plot("m0_bl_prop",       ["TH1D","m0_bl1_prop","",16,0., 800.],       LambdaFunc('x: x.m0_bl[0]')),
	 Plot("m1_bl_prop",       ["TH1D","m1_bl1_prop","",16,0., 800.],       LambdaFunc('x: x.m1_bl[0]')),
	 Plot("m_asym_bl_prop",    ["TH1D","m_asym_bl_prop","",20,0., 1.],       LambdaFunc('x: x.m_asym_bl[0]')),
         Plot("m_ct_prop",         ["TH1D","m_ct_prop","",16,0., 800.],         LambdaFunc('x: x.m_ct[0]')),
         ]


xsWeighter              = XSWeighter("XSWeighter")
mediumMuonProducer      = PhysObjProducer("MediumMuonProducer","Muon","MediumMuons","Moriond17MediumMuon")
mediumElectronProducer  = PhysObjProducer("MediumElectronProducer","Electron","MediumElectrons","Moriond17MediumElectron")
jetProducer             = JetProducer("JetProducer","Jet",["MediumMuons","MediumElectrons"],"LooseJets","Moriond17LooseJet",0.4)
if ratio_switch == True:
   plotter                 = Plotter("Plotter",ratio_plots)
else:
    plotter                 = Plotter("Plotter",mc_plots)
anaProducer             = AnalysisProducer("AnaProducer")

sequence = Sequence()
sequence.add(mediumMuonProducer)
sequence.add(mediumElectronProducer)
sequence.add(jetProducer)
sequence.add(xsWeighter)
sequence.add(anaProducer)
sequence.add(plotter)

endSequence = EndSequence(skipHadd=False)
if ratio_switch == False:
   endModuleOutputDir = "/home/kshi/public_html/mcPlot/"
   endSequence.add(PlotEndModule(endModuleOutputDir,mc_plots,ratio_switch))
else:
    endModuleOutputDir = "/home/kshi/public_html/ratioPlot/"
    endSequence.add(PlotEndModule(endModuleOutputDir,ratio_plots,ratio_switch))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "MCDistribution.root"

