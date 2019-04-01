
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZdZd.Dataset.Run2016.ZXCR_MC_DarkPhoton import * 
from HToZdZd.Dataset.Run2016.ZXCR_Data_DarkPhoton import * 

from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l118-130/2019-03-29_3P1F_DataVsPred/"

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [30,0.,60.]
h4lPlotRange = [20,100.,140.]

eachCR = "3p1f"
general_plots = []
general_plots.extend([
    Plot("Z1_mass_"+eachCR,         ["TH1D","Z1_mass_"+eachCR,"",]+mZ1PlotRange,        LambdaFunc('x: x.massZ1[0]'),       ),
    Plot("Z2_mass_"+eachCR,         ["TH1D","Z2_mass_"+eachCR,"",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),       ),
    Plot("Z1_4e_mass_"+eachCR,      ["TH1D","Z1_4e_mass_"+eachCR,"",]+mZ1PlotRange,     LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
    Plot("Z2_4e_mass_"+eachCR,      ["TH1D","Z2_4e_mass_"+eachCR,"",]+mZ2PlotRange,     LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
    Plot("Z1_4mu_mass_"+eachCR,     ["TH1D","Z1_4mu_mass_"+eachCR,"",]+mZ1PlotRange,    LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
    Plot("Z2_4mu_mass_"+eachCR,     ["TH1D","Z2_4mu_mass_"+eachCR,"",]+mZ2PlotRange,    LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
    Plot("Z1_2e2mu_mass_"+eachCR,   ["TH1D","Z1_2e2mu_mass_"+eachCR,"",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
    Plot("Z2_2e2mu_mass_"+eachCR,   ["TH1D","Z2_2e2mu_mass_"+eachCR,"",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
    Plot("Z1_2mu2e_mass_"+eachCR,   ["TH1D","Z1_2mu2e_mass_"+eachCR,"",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
    Plot("Z2_2mu2e_mass_"+eachCR,   ["TH1D","Z2_2mu2e_mass_"+eachCR,"",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
                   
    Plot("h4L_mass_"+eachCR,        ["TH1D","h4L_mass_"+eachCR,"",]+h4lPlotRange,       LambdaFunc('x: x.mass4l[0]'),       ),
    Plot("h4e_mass_"+eachCR,        ["TH1D","h4e_mass_"+eachCR,"",]+h4lPlotRange,       LambdaFunc('x: x.mass4e[0]'),       ),
    Plot("h4mu_mass_"+eachCR,       ["TH1D","h4mu_mass_"+eachCR,"",]+h4lPlotRange,      LambdaFunc('x: x.mass4mu[0]'),      ),
    Plot("h2e2mu_mass_"+eachCR,     ["TH1D","h2mu2e_mass_"+eachCR,"",]+h4lPlotRange,    LambdaFunc('x: x.mass2e2mu[0]'),    ),
    
    ])

plots =  general_plots

predCR.isSignal         = False

nCores                  = 5
outputDir               = system.getStoragePath()+"/lucien/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [Data_Run2016,predCR]
justEndSequence         = False
eventSelection          = LambdaFunc("x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0]) < 0.05") 

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_3p1f_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
