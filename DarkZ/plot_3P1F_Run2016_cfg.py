
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2016.ZXCR_MC_DarkPhoton import * 
from DarkZ.Dataset.Run2016.ZXCR_Data_DarkPhoton import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l118-130/2019-01-16_3P1F_DataVsPred_FRv2/"
#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/2019-03-07_3P1F_DataVsPred_FRWeightFromVukasin/"
#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/2019-03-07_3P1F_DataVsPred_FRWeightSumCorrIso/"
#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/2019-03-07_3P1F_DataVsPred_FRWeightFromVukasin_MaxFRL3L4/"
out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/2019-03-11_3P1F_DataVsPred_FRWeightFromVukasin/"

#mZ1PlotRange = [60,0.,120.]
#mZ2PlotRange = [60,0.,120.]
h4lPlotRange = [55,60.,500.]
mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [60,0.,120.]
#mZ2PlotRange = [30,0.,60.]
#h4lPlotRange = [20,100.,140.]

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
                   
    Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')       ),
    Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and x.mass4e[0] < 0 and x.mass2e2mu[0] < 0')       ),
    Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')       ),
    Plot("h2mu2e_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')       ),
    Plot("h4L_Pt",      ["TH1D","h4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
    
    Plot("met_"+eachCR,             ["TH1D","met_"+eachCR,"",40,0.,200.],               LambdaFunc('x: x.met[0]'),          ),
    Plot("nVtx_"+eachCR,            ["TH1D","nVtx_"+eachCR,"",30,0.0,60.0],             LambdaFunc('x: x.nVtx[0]'),         ),
    ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

predCR.isSignal         = False

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [Data_Run2016,predCR,WZTo3LNu,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
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
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
