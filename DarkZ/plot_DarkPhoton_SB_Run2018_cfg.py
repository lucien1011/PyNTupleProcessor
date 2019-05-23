from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2018.SkimTree_DarkPhoton_m4l70 import * 
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.MergeSampleDict import mergeSampleDict
from DarkZ.Config.PlotDefinition import *

#out_path                = "DarkPhotonSB/DataMCDistributions/2019-04-02_Run2018_m4l105To118/"
#out_path                = "DarkPhotonSB/DataMCDistributions/2019-04-02_Run2018_m4l130To140/"
out_path                = "DarkPhotonSB/DataMCDistributions/2019-05-20_Run2018_m4l70-100/"
#out_path                = "DarkPhotonSB/DataMCDistributions/2019-05-20_Run2018_m4l170-200/"
lumi                    = 59.7
nCores                  = 2
outputDir               = system.getStoragePath()+"/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [data2018] #+ [HZZd_M4,HZZd_M15,HZZd_M30,] 
justEndSequence         = False
eventSelection          = LambdaFunc("x: x.mass4l[0] > 70. and x.mass4l[0] < 100.")
#eventSelection          = LambdaFunc("x: x.mass4l[0] > 170. and x.mass4l[0] < 200.")

plots                   = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

for p in plots:
    if "m4l" in p.key: p.rootSetting = p.rootSetting[:3]+[30-1,array.array('d',[60.*1.02**i for i in range(30)]),]
    if "mZ2" in p.key: p.rootSetting = p.rootSetting[:3]+[23,4.,50.] 
    #if "m4l" in p.key: p.rootSetting = p.rootSetting[:3]+[15,170.,200.]
    #if "mZ2" in p.key: p.rootSetting = p.rootSetting[:3]+[50,0.,100.] 

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
variableProducer        = VariableProducer("VariableProducer")

sequence                = darkphoton_m4lSB_sequence
#sequence                = higgs_m4lNarrowWindow_sequence
sequence.add(variableProducer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
