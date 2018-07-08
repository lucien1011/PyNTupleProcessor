
# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.MC import * 
from DarkZ.Dataset.Run2017.MC import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
#from DarkZ.Dataset.Run2017.SkimTree import * 

from DarkZ.Skimmer.Preskimmer import GENPreskimmer
from DarkZ.Skimmer.FiducialSkimmer import FiducialSkimmer
from DarkZ.Skimmer.OSSFLeptonSkimmer import OSSFLeptonSkimmer
from DarkZ.Skimmer.RecoSkimmer import RecoSkimmer
from DarkZ.Producer.HZZProducer import HZZProducer

from NanoAOD.Producer.GenWeightCounter import *
from NanoAOD.Weighter.XSWeighter import *
from NanoAOD.EndModule.CutflowEndModule import CutflowEndModule

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "Higgs/DarkZ/SignalEfficiency/EventSelection_v1/Log/20180630/"
out_path = "Higgs/DarkZ/CutflowEfficiency/Log/20180707/ZD_UpTo0j_Eps1e-2_LeptonFSR/"
#out_path = "Higgs/DarkZ/CutflowEfficiency/Log/20180706/BkgMC_Run2017/"

nCores = 5
outputDir = "/raid/raid7/lucien/"+out_path
nEvents = -1
disableProgressBar = False
justEndSequence = False
#componentList = bkgSamples 
componentList = sigSamples

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 77.30
    for component in dataset.componentList:
        component.maxEvents = nEvents

xsWeighter              = XSWeighter("XSWeighter")
preskimmer              = GENPreskimmer("Preskimmer")
preskimCounter          = GenWeightCounter("GenWeightCounter",postfix="Preskim")
fidskimmer              = FiducialSkimmer("FiducialSkimmer")
fidCounter              = GenWeightCounter("GenWeightCounter",postfix="FidicialCut")
hZZProducer             = HZZProducer("HZZProducer")
recoCounter             = GenWeightCounter("GenWeightCounter",postfix="Reco")
ossfSkimmer             = OSSFLeptonSkimmer("OSSFLeptonSkimmer")
ossfCounter             = GenWeightCounter("GenWeightCounter",postfix="OSSF")
recoSkimmer             = RecoSkimmer("RecoSkimmer")

sequence = Sequence()
sequence.add(xsWeighter)
sequence.add(preskimmer)
sequence.add(preskimCounter)
sequence.add(fidskimmer)
sequence.add(fidCounter)
sequence.add(ossfSkimmer)
sequence.add(ossfCounter)
sequence.add(recoSkimmer)
sequence.add(recoCounter)

cutflows = [
        "Preskim",
        "FidicialCut",
        "OSSF",
        "Reco",
        ]

endModuleOutputDir = "/home/lucien/public_html/"+out_path

cutflowEndModule = CutflowEndModule(endModuleOutputDir,cutflows=cutflows,ignoreSumw=True)

endSequence = EndSequence(skipHadd=justEndSequence)
endSequence.add(cutflowEndModule)
#endSequence.add(PlotEndModule(endModuleOutputDir,validation_plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "EventWeight.root"

