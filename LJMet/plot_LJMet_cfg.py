from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from LJMet.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from LJMet.Dataset.LJMet94X_1lepTT_101118newB_step1hadds_2018 import *

out_path                = "TestPlot/2018-11-05/"
lumi                    = 35.9
nCores                  = 5
outputDir               = out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [TTToSemiLep_Mtt1000ToInf,]
justEndSequence         = False

plots = [
        Plot("AK4HT",        ["TH1D","AK4HT","",25,500.0,3000.0],      LambdaFunc('x: x.AK4HT[0]'),),
        ]

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
xsWeighter              = XSWeighter("XSWeighter")

sequence                = Sequence()
sequence.add(xsWeighter)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
