# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.MC import * 
from DarkZ.Dataset.Run2017.SignalMC import * 
#from DarkZ.Dataset.Run2017.SkimTree import * 

from DarkZ.Skimmer.Preskimmer import GENPreskimmer
from DarkZ.Skimmer.FiducialSkimmer import FiducialSkimmer

from NanoAOD.Producer.GenWeightCounter import *
from NanoAOD.Weighter.XSWeighter import *
from NanoAOD.EndModule.CutflowEndModule import CutflowEndModule

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

validation_plots = [
        Plot("nGenLep",         ["TH1D","nGenLep","",10,-0.5,9.5],      LambdaFunc('x: len(x.genleps)'),       ),
        Plot("nZCandidates",    ["TH1D","nZCandidates","",10,-0.5,9.5], LambdaFunc('x: len(x.ZCandidates)'),       ),
        Plot("GenLep1_Pt",      ["TH1D","GenLep1_pt","",20,0.,200.],    LambdaFunc('x: x.genleps[0].pt if len(x.genleps) >= 1 else None')),
        Plot("Z1_mass",         ["TH1D","Z1_mass","",20,20.,140.],      LambdaFunc('x: x.Z1.vec.M()'),       ),
        Plot("Z2_mass",         ["TH1D","Z2_mass","",20, 0.,150.],      LambdaFunc('x: x.Z2.vec.M()'),       ),
        Plot("h4L_mass",        ["TH1D","4L_mass","",50,0.,500.],       LambdaFunc('x: x.hmass'),       ),
        ]

#out_path = "Higgs/DarkZ/SignalEfficiency/EventSelection_v1/Log/20180630/"
out_path = "Higgs/DarkZ/Acceptance/Run2017/20180706/ZD_Upto0j_Eps1e-2/"

nCores = 4
outputDir = "/raid/raid7/lucien/"+out_path
nEvents = -1
disableProgressBar = False
justEndSequence = False
#componentList = bkgSamples + sigSamples
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
plotter                 = Plotter("Plotter",validation_plots)

sequence = Sequence()
sequence.add(xsWeighter)
sequence.add(preskimmer)
sequence.add(preskimCounter)
sequence.add(fidskimmer)
sequence.add(fidCounter)
#sequence.add(plotter)

cutflows = [
        "Preskim",
        "FidicialCut",
        ]

endModuleOutputDir = "/home/lucien/public_html/"+out_path

cutflowEndModule = CutflowEndModule(endModuleOutputDir,cutflows=cutflows,ignoreSumw=True)

endSequence = EndSequence(skipHadd=justEndSequence)
endSequence.add(cutflowEndModule)
#endSequence.add(PlotEndModule(endModuleOutputDir,validation_plots))

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "EventWeight.root"
