from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.MC import * 
from DarkZ.Dataset.Run2017.BkgMC import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
#from DarkZ.Dataset.Run2017.SkimTree import * 

#from DarkZ.Skimmer.Preskimmer import GENPreskimmer
#from DarkZ.Skimmer.FiducialSkimmer import FiducialSkimmer
from DarkZ.Skimmer.RecoSkimmer import RecoSkimmer
from DarkZ.StatTools.MassWindow import MassWindow
from DarkZ.StatTools.YieldProducer import YieldProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "MCDistributions/MC_BaselineSelection_v1/2018-07-09/"
out_path = "StatInput/SignalSelection_v1/2018-07-26/"

mass_window_list = [
        MassWindow(15,0.02),
        MassWindow(20,0.02),
        MassWindow(25,0.02),
        MassWindow(30,0.02),
        ]

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSamples
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 77.30
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = Sequence()
xsWeighter              = XSWeighter("XSWeighter")
recoSkimmer             = RecoSkimmer("RecoSkimmer")
recoSkimmer.Z2MassRange = [4.,120.]
yieldProducer           = YieldProducer("YieldProducer",mass_window_list)

sequence.add(xsWeighter)
sequence.add(recoSkimmer)
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
