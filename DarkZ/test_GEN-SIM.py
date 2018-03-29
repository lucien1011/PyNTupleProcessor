# UF Framework specifics
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo 

from Core.NanoAODResult.Component import Component

from DarkZ.Analyzer.GENSIM import CollectionProducer
from DarkZ.EndModule.PlotEndModule import PlotEndModule
from RPV.Analyzer.Plotter.Plotter import Plotter
from RPV.Analyzer.Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

gen_cmp = Component(
        "/raid/raid7/lucien/Higgs/DarkZ-EvtGeneration/Log/2018-03-23/",
        "DarkZTo4l_v1",
        inUFTier2 = False,
        keyword = "",
        )

plots = [
        Plot("DarkZPt", ["TH1D","DarkZ-pt","",20,0.,200.], LambdaFunc('x: [x.pt() for x in x.genparts if x.pdgId() == 1023]'), isCollection=True),
        Plot("DarkZEta", ["TH1D","DarkZ-eta","",20,-5.,5.], LambdaFunc('x: [x.eta() for x in x.genparts if x.pdgId() == 1023]'), isCollection=True),
        
        Plot("HiggsPt", ["TH1D","Higgs-pt","",20,0.,200.], LambdaFunc('x: [x.pt() for x in x.genparts if x.pdgId() == 25]'), isCollection=True),
        Plot("HiggsEta", ["TH1D","Higgs-eta","",20,-5.,5.], LambdaFunc('x: [x.eta() for x in x.genparts if x.pdgId() == 25]'), isCollection=True),
        
        Plot("ZPt", ["TH1D","Z-pt","",20,0.,200.], LambdaFunc('x: [x.pt() for x in x.genparts if x.pdgId() == 23]'), isCollection=True),
        Plot("ZEta", ["TH1D","Z-eta","",20,-5.,5.], LambdaFunc('x: [x.eta() for x in x.genparts if x.pdgId() == 23]'), isCollection=True),
        
        Plot("MuonPt", ["TH1D","Muon-pt","",20,0.,200.], LambdaFunc('x: [x.pt() for x in x.genparts if abs(x.pdgId()) == 13]'), isCollection=True),
        Plot("MuonEta", ["TH1D","Muon-eta","",20,-5.,5.], LambdaFunc('x: [x.eta() for x in x.genparts if abs(x.pdgId()) == 13]'), isCollection=True),
        
        Plot("GenJetPt", ["TH1D","GenJet-pt","",20,0.,200.], LambdaFunc('x: [x.pt() for x in x.genjets]'), isCollection=True),
        Plot("GenJetEta", ["TH1D","GenJet-eta","",20,-5.,5.], LambdaFunc('x: [x.eta() for x in x.genjets]'), isCollection=True),
        Plot("nGenJet302p4", ["TH1D","nGenJet302p4","",20,-5.,5.], LambdaFunc('x: len([x.eta() for x in x.genjets if x.pt() > 30 and abs(x.eta()) < 2.4])')),
        ]

nCores = 1 
outputDir = "/raid/raid7/lucien/Higgs/DarkZ-EvtGeneration/Log/2018-03-23/testEDM_v2/"
nEvents = -1
disableProgressBar = False
justEndSequence = True

sequence = Sequence()
genParticleProducer = CollectionProducer("GenParticleProducer",("genParticles","","GEN"),selection=LambdaFunc('x: x.isHardProcess()'))
genJetProducer = CollectionProducer("GenJetProducer",("ak4GenJets","","GEN"),inCollType='std::vector<reco::GenJet>',outCollName="genjets")
plotter = Plotter("Plotter",plots)

sequence.add(genParticleProducer)
sequence.add(genJetProducer)
sequence.add(plotter)

endSequence = EndSequence()
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ-EvtGeneration/Log/2018-03-23/testEDM_v2/"
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"

componentList = [
        gen_cmp,
        ]

