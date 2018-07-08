
# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.MC import * 
from DarkZ.Dataset.Run2017.MC import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
#from DarkZ.Dataset.Run2017.SkimTree import * 

from DarkZ.Skimmer.RecoSkimmer import RecoSkimmer
from DarkZ.Skimmer.Preskimmer import GENPreskimmer
from DarkZ.Skimmer.FiducialSkimmer import FiducialSkimmer
from DarkZ.Skimmer.NLeptonSkimmer import NLeptonSkimmer
from DarkZ.Skimmer.LeptonPtSkimmer import LeptonPtSkimmer
from DarkZ.Skimmer.OSSFLeptonSkimmer import OSSFLeptonSkimmer
from DarkZ.Skimmer.Z1Z2Skimmer import Z1Z2Skimmer
from DarkZ.Skimmer.DeltaRSkimmer import DeltaRSkimmer
from DarkZ.Skimmer.FourLeptonMassSkimmer import FourLeptonMassSkimmer
from DarkZ.Producer.CollectionProducer import CollectionProducer
#from DarkZ.Producer.HZZProducer import HZZProducer

from NanoAOD.Producer.GenWeightCounter import *
from NanoAOD.Weighter.XSWeighter import *
from NanoAOD.EndModule.CutflowEndModule import CutflowEndModule
from NanoAOD.EndModule.Cutflow import Cutflow

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
justEndSequence = True
#componentList = bkgSamples 
componentList = sigSamples

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 77.30
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence = Sequence()
xsWeighter              = XSWeighter("XSWeighter")
sequence.add(xsWeighter)

preskimmer              = GENPreskimmer("Preskimmer")
preskimCounter          = GenWeightCounter("GenWeightCounter",postfix="Preskim")
fidskimmer              = FiducialSkimmer("FiducialSkimmer")
fidCounter              = GenWeightCounter("GenWeightCounter",postfix="FidicialCut")
sequence.add(preskimmer)
sequence.add(preskimCounter)
sequence.add(fidskimmer)
sequence.add(fidCounter)

collectionProducer      = CollectionProducer("CollectionProducer")
sequence.add(collectionProducer)

nLeptonSkimmer          = NLeptonSkimmer("NLeptonSkimmer")
nLeptonCounter          = GenWeightCounter("GenWeightCounter",postfix="nLepton")
sequence.add(nLeptonSkimmer)
sequence.add(nLeptonCounter)

leptonPtSkimmer         = LeptonPtSkimmer("LeptonPtSkimmer")
leptonPtCounter         = GenWeightCounter("LeptonPtCounter",postfix="LeptonPt")
sequence.add(leptonPtSkimmer)
sequence.add(leptonPtCounter)

ossfSkimmer             = OSSFLeptonSkimmer("OSSFLeptonSkimmer")
ossfCounter             = GenWeightCounter("GenWeightCounter",postfix="OSSF")
sequence.add(ossfSkimmer)
sequence.add(ossfCounter)

z1z2Skimmer             = Z1Z2Skimmer("Z1Z2Skimmer")
z1z2Counter             = GenWeightCounter("GenWeightCounter",postfix="Z1Z2")
sequence.add(z1z2Skimmer)
sequence.add(z1z2Counter)

deltaRSkimmer           = DeltaRSkimmer("DeltaRSkimmer")
deltaRCounter           = GenWeightCounter("GenWeightCounter",postfix="DeltaR")
sequence.add(deltaRSkimmer)
sequence.add(deltaRCounter)

fourLeptonSkimmer       = FourLeptonMassSkimmer("FourLeptonSkimmer")
fourLeptonCounter       = GenWeightCounter("GenWeightCounter",postfix="h4L")
sequence.add(fourLeptonSkimmer)
sequence.add(fourLeptonCounter)

#recoSkimmer             = RecoSkimmer("RecoSkimmer")
#recoCounter             = GenWeightCounter("GenWeightCounter",postfix="Reco")
#sequence.add(recoSkimmer)
#sequence.add(recoCounter)

cutflows = [
        #Cutflow("Preskim",)
        Cutflow("FidicialCut",latexName="Gen-level fidicial cut"),
        Cutflow("nLepton",latexName="Number of lepton $\geq 4$"),
        Cutflow("LeptonPt",latexName="Leading and subleading $p_{T}$"),
        Cutflow("OSSF",latexName="Opposite sign same flavour"),
        Cutflow("Z1Z2",latexName="$40 < m_{Z1} < 120$, $12 < m_{Z2} < 120$"),
        Cutflow("DeltaR",latexName="$\\DeltaR_{i,j} > 0.02$"),
        Cutflow("h4L",latexName="$40 < m_{4l} < 120$"),
        ]

endModuleOutputDir = "/home/lucien/public_html/"+out_path

cutflowEndModule = CutflowEndModule(endModuleOutputDir,cutflows=cutflows,ignoreSumw=True)

endSequence = EndSequence(skipHadd=justEndSequence)
endSequence.add(cutflowEndModule)
#endSequence.add(PlotEndModule(endModuleOutputDir,validation_plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "EventWeight.root"

