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
        "/cms/data/store/user/klo/RPV_Moriond17_GEN-SIM/v2/SMS-T1tbs-ttdilep-RPV_Madgraph_Pythia_GEN-SIM/SMS-T1tbs-DiLep_Madgraph_Pythia_test_GEN-SIM_v2/180328_152252/0000/",
        "SMS-T1tbs-DiLep",
        inUFTier2 = True,
        keyword = "",
        ).makeComponentFromEachFile()

plots = [
        Plot("MuonPt", ["TH1D","Muon-pt","",20,0.,200.], LambdaFunc('x: [x.pt() for x in x.genparts if abs(x.pdgId()) == 13]'), isCollection=True),
        Plot("MuonEta", ["TH1D","Muon-eta","",20,-5.,5.], LambdaFunc('x: [x.eta() for x in x.genparts if abs(x.pdgId()) == 13]'), isCollection=True),
        
        Plot("GenJetPt", ["TH1D","GenJet-pt","",20,0.,200.], LambdaFunc('x: [x.pt() for x in x.genjets]'), isCollection=True),
        Plot("GenJetEta", ["TH1D","GenJet-eta","",20,-5.,5.], LambdaFunc('x: [x.eta() for x in x.genjets]'), isCollection=True),
        Plot("nGenJet302p4", ["TH1D","nGenJet302p4","",20,-5.,5.], LambdaFunc('x: len([x.eta() for x in x.genjets if x.pt() > 30 and abs(x.eta()) < 2.4])')),
        ]

nCores = 1 
outputDir = "/raid/raid7/lucien/SUSY/RPV/Log/Validate_GEN-SIM/2018-03-29/"
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
endModuleOutputDir = "/home/lucien/public_html/SUSY/RPV/Log/Validate_GEN-SIM/2018-03-29/"
endSequence.add(PlotEndModule(endModuleOutputDir,plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"

componentList = gen_cmp
        
