from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_ppZZd4l import * 
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.MergeSampleDict import mergeSampleDict
from DarkZ.Config.PlotDefinition import *

#out_path                = "DarkPhotonFullm4l/DataMCDistributions/2019-05-10_ppZZd_Run2016/"
#out_path                = "DarkPhotonFullm4l/DataMCDistributions/2019-05-10_ppZZd_Run2016_mZ180To100/"
#out_path                = "DarkPhotonFullm4l/DataMCDistributions/2019-05-13_ppZZd_Run2016_m4l100To118/"
out_path                = "DarkPhotonFullm4l/DataMCDistributions/2019-05-13_ppZZd_Run2016_m4l130To170/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2018-11-09_Run2017/"
User                    = os.environ['USER']
lumi                    = 35.9
nCores                  = 3
outputDir               = system.getStoragePath()+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [
                                        ppZZd4l_M5,
                                        ppZZd4l_M15,
                                        ppZZd4l_M30,
                                        ]
#componentList           = bkgSamples + [data2017] + [HZZd_M4,HZZd_M15,HZZd_M30,] 
justEndSequence         = False
#eventSelection          = LambdaFunc('x: x.mass4l[0] > 100. and x.mass4l[0] < 118.')
eventSelection          = LambdaFunc('x: x.mass4l[0] > 130. and x.mass4l[0] < 170.')

plots                   = general_4e_plots + general_2mu2e_plots + general_4mu_plots + general_2e2mu_plots

#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
variableProducer        = VariableProducer("VariableProducer")

sequence                = darkphoton_fullm4l_sequence
#sequence                = higgs_m4lNarrowWindow_sequence
sequence.add(variableProducer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
