# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Config.MergeSampleDefinition import mergeSampleDict
#from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from RA5.Sequence.RecoSequence import tl_rpv_sequence

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

#from RA5.Dataset.Run2016.Sept18_v1 import *
#from RA5.Dataset.Run2016.Sept18_v1_Data import dataComponentDict
#from RA5.Dataset.Run2016.Sept18_v1_skim import *
#from RA5.Dataset.Run2016.Sept18_v1_SMS import sigComponentDict

from RA5.Dataset.Run2016.Sept18_v1_TightLoose import skimComponentDict

if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/RPV/DataMCDistributions/2018-09-12_HLTEmulation/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    #out_path = "TightLoose/DataMCDistribution/2018-10-11_MET0ToInf_CleaningLep/"
    #out_path = "TightLoose/DataMCDistribution/2018-10-11_MET0To50_CleaningLep/"
    out_path = "TightLoose/DataMCDistribution/2018-10-11_MET50ToInf_CleaningLep/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
lepCats = [""]

nCores                      = 5
nEvents                     = -1
disableProgressBar          = False
justEndSequence             = False
verbose                     = False
#componentList               = [c for c in componentDict.values() if not c.isSignal and not (("WJets" in c.name and "HT" not in c.name) or ("DYJets" in c.name and "HT" not in c.name)) ] + dataComponentDict.values()
#componentList               = [c for c in skimComponentDict.values() if "2016H" not in c.name and "QCD" not in c.name]
#componentList               = [c for c in skimComponentDict.values() if "2016H" not in c.name]
componentList               = skimComponentDict.values()
#componentList               = [c for c in skimComponentDict.values() if c.isMC] + dataComponentDict.values()
#componentList               = [c for c in skimComponentDict.values() if "WJets" in c.name]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

lepPtRange          = [20,0.,200.]
lepEtaRange         = [10,-3.,3.]
lepPhiRange         = [10,-4.,4.]
jet1PtRange         = [20,0.,200.]
jet1PhiRange        = [18,-4.75,4.25]
jet2PtRange         = [12,0.,120.]
jetEtaRange         = [10,-3.,3.]
jet2PhiRange        = [10,-4.,4.]
htRange             = [20,0.,600.]
#metRange            = [20,0.,50.]
metRange            = [20,0.,200.]
mtRange             = [20,0.,120.]

plots = []
for lepCat in lepCats:
    plots.extend(
        [
        
        # General variable
        Plot("nJet40"+lepCat,      ["TH1D","nJet40"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA540[0]')               ),
        Plot("nJet25"+lepCat,      ["TH1D","nJet25"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA525[0]')               ),
        Plot("nBJet40"+lepCat,     ["TH1D","nBJet40"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMediumRA540[0]')         ),
        Plot("nBJet25"+lepCat,     ["TH1D","nBJet25"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMediumRA525[0]')         ),
        Plot("nLepLoose"+lepCat,    ["TH1D","nLepLoose"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: len(x.looseLeps)')           ),
        Plot("htJet"+lepCat,       ["TH1D","htJet"+lepCat,"",]+htRange,         LambdaFunc('x: x.htJet40[0]')                ),
        Plot("met_pt"+lepCat,      ["TH1D","met_pt"+lepCat,"",]+metRange,          LambdaFunc('x: x.met_pt[0]')               ),
        Plot("met_phi"+lepCat,     ["TH1D","met_phi"+lepCat,"",10,-5, 5.],          LambdaFunc('x: x.met_phi[0]')               ),
        Plot("mtmin"+lepCat,         ["TH1D","mtmin"+lepCat,"",]+mtRange,          LambdaFunc('x: x.mtmin')                  ),
        
        # Lepton kinematics
        Plot("LepTight1_Pt"+lepCat,             ["TH1D","LepTight1_Pt"+lepCat,"",]+lepPtRange,      LambdaFunc('x: x.firstLep.pt')          ),
        Plot("LepTight1_Eta"+lepCat,            ["TH1D","LepTight1_Eta"+lepCat,"",]+lepEtaRange,      LambdaFunc('x: x.firstLep.eta')        ),
        Plot("LepTight1_Phi"+lepCat,            ["TH1D","LepTight1_Phi"+lepCat,"",]+lepPhiRange,      LambdaFunc('x: x.firstLep.phi')        ),
        Plot("LepTight1_JetPtRelHv2"+lepCat,    ["TH1D","LepTight1_JetPtRelHv2"+lepCat,"",10,0.,5.],      LambdaFunc('x: x.firstLep.jetPtRelHv2')        ),
        Plot("LepTight1_dxy"+lepCat,            ["TH1D","LepTight1_dxy"+lepCat,"",10,0.,0.05],      LambdaFunc('x: x.firstLep.dxy')          ),
        Plot("LepTight1_dz"+lepCat,            ["TH1D","LepTight1_dz"+lepCat,"",10,0.,0.05],      LambdaFunc('x: x.firstLep.dz')          ),
        Plot("LepTight1_sip3d"+lepCat,            ["TH1D","LepTight1_sip3d"+lepCat,"",10,0.,5.],      LambdaFunc('x: x.firstLep.sip3d')          ),
        Plot("LepTight1_relIso04"+lepCat,    ["TH1D","LepTight1_relIso04"+lepCat,"",10,0.,1.],      LambdaFunc('x: x.firstLep.relIso04')        ),
        Plot("LepTight1_miniRelIso"+lepCat,    ["TH1D","LepTight1_miniRelIso"+lepCat,"",10,0.,0.5],      LambdaFunc('x: x.firstLep.miniRelIso')        ),

        Plot("LepLoose1_Pt"+lepCat,             ["TH1D","LepLoose1_Pt"+lepCat,"",]+lepPtRange,      LambdaFunc('x: x.secondLep.pt')          ),
        Plot("LepLoose1_Eta"+lepCat,            ["TH1D","LepLoose1_Eta"+lepCat,"",]+lepEtaRange,      LambdaFunc('x: x.secondLep.eta')        ),
        Plot("LepLoose1_Phi"+lepCat,            ["TH1D","LepLoose1_Phi"+lepCat,"",]+lepPhiRange,      LambdaFunc('x: x.secondLep.phi')        ),
        Plot("LepLoose1_JetPtRelHv2"+lepCat,    ["TH1D","LepLoose1_JetPtRelHv2"+lepCat,"",10,0.,5.],      LambdaFunc('x: x.secondLep.jetPtRelHv2')        ),
        Plot("LepLoose1_dxy"+lepCat,            ["TH1D","LepLoose1_dxy"+lepCat,"",10,0.,0.05],      LambdaFunc('x: x.secondLep.dxy')          ),
        Plot("LepLoose1_dz"+lepCat,            ["TH1D","LepLoose1_dz"+lepCat,"",10,0.,0.05],      LambdaFunc('x: x.secondLep.dz')          ),
        Plot("LepLoose1_sip3d"+lepCat,            ["TH1D","LepLoose1_sip3d"+lepCat,"",10,0.,5.],      LambdaFunc('x: x.secondLep.sip3d')          ),
        Plot("LepLoose1_relIso04"+lepCat,    ["TH1D","LepLoose1_relIso04"+lepCat,"",10,0.,1.],      LambdaFunc('x: x.secondLep.relIso04')        ),
        Plot("LepLoose1_miniRelIso"+lepCat,    ["TH1D","LepLoose1_miniRelIso"+lepCat,"",10,0.,0.5],      LambdaFunc('x: x.secondLep.miniRelIso')        ),

        # Jet kinematics
        Plot("Jet1_Pt"+lepCat,    ["TH1D","Jet1_Pt"+lepCat,"",]+jet1PtRange,      LambdaFunc('x: x.selJets[0].pt')                  ),
        Plot("Jet1_Eta"+lepCat,    ["TH1D","Jet1_Eta"+lepCat,"",]+jetEtaRange,      LambdaFunc('x: x.selJets[0].eta')                ),
        Plot("Jet1_Phi"+lepCat,    ["TH1D","Jet1_Phi"+lepCat,"",]+jet1PhiRange,      LambdaFunc('x: x.selJets[0].phi')                ),
        Plot("Jet1_chHEF"+lepCat,    ["TH1D","Jet1_chHEF"+lepCat,"",25,0.,1.],      LambdaFunc('x: x.selJets[0].chHEF')                ),
        Plot("Jet1_neHEF"+lepCat,    ["TH1D","Jet1_neHEF"+lepCat,"",25,0.,1.],      LambdaFunc('x: x.selJets[0].neHEF')                ),
        
        Plot("Jet2_Pt"+lepCat,    ["TH1D","Jet2_Pt"+lepCat,""]+jet2PtRange,      LambdaFunc('x: x.selJets[1].pt')                  ),
        Plot("Jet2_Eta"+lepCat,    ["TH1D","Jet2_Eta"+lepCat,"",]+jetEtaRange,      LambdaFunc('x: x.selJets[1].eta')                ),
        Plot("Jet2_Phi"+lepCat,    ["TH1D","Jet2_Phi"+lepCat,"",]+jet2PhiRange,      LambdaFunc('x: x.selJets[1].phi')                ),
        Plot("Jet2_chHEF"+lepCat,    ["TH1D","Jet2_chHEF"+lepCat,"",25,0.,1.],      LambdaFunc('x: x.selJets[1].chHEF')                ),
        Plot("Jet2_neHEF"+lepCat,    ["TH1D","Jet2_neHEF"+lepCat,"",25,0.,1.],      LambdaFunc('x: x.selJets[1].neHEF')                ),
         
        ]
        )
plotter                 = Plotter("Plotter",plots)

sequence = tl_rpv_sequence
sequence.add(plotter)

endSequence = EndSequence(skipHadd=False,)
endSequence.add(PlotEndModule(endModuleOutputDir,plots,scaleToData=False))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "DataMCDistributions.root"
