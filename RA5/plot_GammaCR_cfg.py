# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Config.MergeSampleDefinition import mergeSampleDict

from RA5.Sequence.RecoSequence import gamma_cr_sequence

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

from RA5.Dataset.Run2016.Sept18_v1_GammaCR import skimComponentDict

if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/RPV/DataMCDistributions/2018-09-12_HLTEmulation/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    out_path = "GammaCR/DataMCDistribution/2018-10-04/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
lepCats = [""]

nCores                      = 5
nEvents                     = -1
disableProgressBar          = False
justEndSequence             = True
verbose                     = False
#componentList               = dataComponentDict.values() + componentDict.values() 
#componentList               = [c for c in dataComponentDict.values() if "2016H" not in c.name] + componentDict.values() 
#componentList              = [c for c in dataComponentDict.values() if "2016H" not in c.name] + [c for c in componentDict.values() if "QCD" not in c.name]
#componentList               = [c for c in skimComponentDict.values() if "2016H" not in c.name and "QCD" not in c.name]
componentList               = skimComponentDict.values()
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 27.96
    for component in dataset.componentList:
        component.maxEvents = nEvents

plots = []
for lepCat in lepCats:
    plots.extend(
        [

        Plot("nJet40"+lepCat,      ["TH1D","nJet40"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA540[0]')               ),
        Plot("nJet25"+lepCat,      ["TH1D","nJet25"+lepCat,"",10,-0.5,9.5],       LambdaFunc('x: x.nJetRA525[0]')               ),
        Plot("nBJet40"+lepCat,     ["TH1D","nBJet40"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMediumRA540[0]')         ),
        Plot("nBJet25"+lepCat,     ["TH1D","nBJet25"+lepCat,"",7,-0.5,6.5],      LambdaFunc('x: x.nBJetMediumRA525[0]')         ),
        Plot("htJet"+lepCat,       ["TH1D","htJet"+lepCat,"",20,0.,1000.],         LambdaFunc('x: x.htJet40[0]')                ),
        Plot("met_pt"+lepCat,      ["TH1D","met_pt"+lepCat,"",25,0., 250.],          LambdaFunc('x: x.met_pt[0]')               ),
        Plot("met_phi"+lepCat,     ["TH1D","met_phi"+lepCat,"",10,-5, 5.],          LambdaFunc('x: x.met_phi[0]')               ),
        #Plot("mtmin"+lepCat,         ["TH1D","mtmin"+lepCat,"",20,0., 200.],          LambdaFunc('x: x.mtmin')                  ),
        
        Plot("LepTightPt1"+lepCat,    ["TH1D","LepTightPt1"+lepCat,"",20,0.,200.],      LambdaFunc('x: x.firstLep.pt')          ),
        Plot("LepTightEta1"+lepCat,    ["TH1D","LepTightEta1"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.firstLep.eta')        ),
        Plot("LepTightPhi1"+lepCat,    ["TH1D","LepTightPhi1"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.firstLep.phi')        ),

        #Plot("JetPt1"+lepCat,    ["TH1D","JetPt1"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.selJets[0].pt')                  ),
        #Plot("JetEta1"+lepCat,    ["TH1D","JetEta1"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.selJets[0].eta')                ),

        #Plot("JetPhi1"+lepCat,    ["TH1D","JetPhi1"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.selJets[0].phi')                ),
        #Plot("JetPt2"+lepCat,    ["TH1D","JetPt2"+lepCat,"",20,0.,400.],      LambdaFunc('x: x.selJets[1].pt')                  ),
        #Plot("JetEta2"+lepCat,    ["TH1D","JetEta2"+lepCat,"",10,-3.,3.],      LambdaFunc('x: x.selJets[1].eta')                ),

        #Plot("JetPhi2"+lepCat,    ["TH1D","JetPhi2"+lepCat,"",10,-5.,5.],      LambdaFunc('x: x.selJets[1].phi')                ),
        ]
        )
plotter                 = Plotter("Plotter",plots)

sequence = gamma_cr_sequence
sequence.add(plotter)

endSequence = EndSequence(skipHadd=False,)
endSequence.add(PlotEndModule(endModuleOutputDir,plots,scaleToData=True))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "DataMCDistributions.root"
