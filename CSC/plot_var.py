from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from CSC.Dataset.SingleMuon_Run2017A_ZMu_v2 import SingleMuon_Run2017A_ZMu_v2
from CSC.Sequence.RecoSequence import MuonSequence
from CSC.Config.StandAloneMuons import plots

from Plotter.Plotter import Plotter
from Plotter.Plot import Plot
from Plotter.PlotEndModule import PlotEndModule

import os

User                    = os.environ['USER']
nCores                  = 1
out_path                = "StandAloneMuon/2020-06-12_SingleMuon_Run2017A_ZMu_v2/"
outputDir               = system.getStoragePath()+"/"+User+"/CSC/Plot/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [SingleMuon_Run2017A_ZMu_v2,]
justEndSequence         = False

sequence                = MuonSequence 
plotter                 = Plotter("Plotter",plots)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence             = EndSequence()
endSequence.add(PlotEndModule(outputDir,plots,skipSF=False))
