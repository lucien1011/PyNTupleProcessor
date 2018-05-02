# UF Framework specifics
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo 

from Core.Component import Component

from DarkZ.Analyzer.GENSIM import CollectionProducer
from DarkZ.EndModule.PlotEndModule import PlotEndModule
from RPV.Analyzer.Plotter.Plotter import Plotter
from RPV.Analyzer.Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

componentList = Component(
        "/cms/data/store/user/klo/DarkPhoton_Moriond17_GEN-SIM/v2/ZD_UpTo0j_MZD20_Eps1e-2/PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3-LHE-GEN-SIM/180403_154314/0000/",
        "DarkZTo4l_v1",
        inUFTier2 = True,
        exclude = "inLHE",
        ).makeComponentFromEachFile()

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
outputDir = "/raid/raid7/lucien/Higgs/DarkZ-EvtGeneration/Log/2018-04-03/GEN-SIM_Validation_v2/"
nEvents = -1
disableProgressBar = False
justEndSequence = False

sequence = Sequence()
genParticleProducer = CollectionProducer("GenParticleProducer",("genParticles","","SIM"),selection=LambdaFunc('x: x.isHardProcess()'))
genJetProducer = CollectionProducer("GenJetProducer",("ak4GenJets","","SIM"),inCollType='std::vector<reco::GenJet>',outCollName="genjets")
plotter = Plotter("Plotter",plots)

sequence.add(genParticleProducer)
sequence.add(genJetProducer)
sequence.add(plotter)

endSequence = EndSequence()
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ-EvtGeneration/Log/2018-04-03/GEN-SIM_Validation_v2/"
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"
