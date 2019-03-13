
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from HZZ4l.Dataset.Run2017.ZXCR_MC import * 
from HZZ4l.Dataset.Run2017.ZXCR_Data import * 

from HZZ4l.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

out_path = "ZPlusX/DataMCDistributions/SkimTree_HZZ4l_ZX_Run2017Data_m4l70/2019-03-11_3P1F_DataVsPred_FRWeightFromVukasin/"

#mZ1PlotRange = [60,0.,120.]
#mZ2PlotRange = [60,0.,120.]
#h4lPlotRange = [55,60.,500.]
h4lPlotRange = [37,60.,800.]
mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [60,0.,120.]
#mZ2PlotRange = [30,0.,60.]
#h4lPlotRange = [20,100.,140.]

#sel_str_4e = "x: abs(x.lep_id[x.lep_Hindex[0]]) == 11 and abs(x.lep_id[x.lep_Hindex[1]]) == 11 and abs(x.lep_id[x.lep_Hindex[2]]) == 11 and abs(x.lep_id[x.lep_Hindex[3]]) == 11"
#sel_str_4mu = "x: abs(x.lep_id[x.lep_Hindex[0]]) == 13 and abs(x.lep_id[x.lep_Hindex[1]]) == 13 and abs(x.lep_id[x.lep_Hindex[2]]) == 13 and abs(x.lep_id[x.lep_Hindex[3]]) == 13"
#sel_str_2e2mu = "x: abs(x.lep_id[x.lep_Hindex[0]]) == 11 and abs(x.lep_id[x.lep_Hindex[1]]) == 11 and abs(x.lep_id[x.lep_Hindex[2]]) == 13 and abs(x.lep_id[x.lep_Hindex[3]]) == 13"
#sel_str_2mu2e = "x: abs(x.lep_id[x.lep_Hindex[0]]) == 13 and abs(x.lep_id[x.lep_Hindex[1]]) == 13 and abs(x.lep_id[x.lep_Hindex[2]]) == 11 and abs(x.lep_id[x.lep_Hindex[3]]) == 11"

sel_str_4e = "x: x.finalState[0] == 2"
sel_str_4mu = "x: x.finalState[0] == 1"
sel_str_2e2mu = "x: x.finalState[0] == 3"
sel_str_2mu2e = "x: x.finalState[0] == 4"

eachCR = "3p1f"
general_plots = []
general_plots.extend([
    Plot("Z1_mass_"+eachCR,         ["TH1D","Z1_mass_"+eachCR,"",]+mZ1PlotRange,        LambdaFunc('x: x.massZ1[0]'),       ),
    Plot("Z2_mass_"+eachCR,         ["TH1D","Z2_mass_"+eachCR,"",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),       ),
    Plot("Z1_4e_mass_"+eachCR,      ["TH1D","Z1_4e_mass_"+eachCR,"",]+mZ1PlotRange,     LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc(sel_str_4e)),
    Plot("Z2_4e_mass_"+eachCR,      ["TH1D","Z2_4e_mass_"+eachCR,"",]+mZ2PlotRange,     LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(sel_str_4e)),
    Plot("Z1_4mu_mass_"+eachCR,     ["TH1D","Z1_4mu_mass_"+eachCR,"",]+mZ1PlotRange,    LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc(sel_str_4mu)),
    Plot("Z2_4mu_mass_"+eachCR,     ["TH1D","Z2_4mu_mass_"+eachCR,"",]+mZ2PlotRange,    LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(sel_str_4mu)),
    Plot("Z1_2e2mu_mass_"+eachCR,   ["TH1D","Z1_2e2mu_mass_"+eachCR,"",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc(sel_str_2e2mu)),
    Plot("Z2_2e2mu_mass_"+eachCR,   ["TH1D","Z2_2e2mu_mass_"+eachCR,"",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(sel_str_2e2mu)),
    Plot("Z1_2mu2e_mass_"+eachCR,   ["TH1D","Z1_2mu2e_mass_"+eachCR,"",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc(sel_str_2mu2e)),
    Plot("Z2_2mu2e_mass_"+eachCR,   ["TH1D","Z2_2mu2e_mass_"+eachCR,"",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(sel_str_2mu2e)),
                   
    Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'), selFunc=LambdaFunc(sel_str_4e)       ),
    Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'), selFunc=LambdaFunc(sel_str_4mu)       ),
    Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'), selFunc=LambdaFunc(sel_str_2e2mu)       ),
    Plot("h2mu2e_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'), selFunc=LambdaFunc(sel_str_2mu2e)       ),
 
    Plot("met_"+eachCR,             ["TH1D","met_"+eachCR,"",40,0.,200.],               LambdaFunc('x: x.met[0]'),          ),
    Plot("nVtx_"+eachCR,            ["TH1D","nVtx_"+eachCR,"",30,0.0,60.0],             LambdaFunc('x: x.nVtx[0]'),         ),
    ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

predCR.isSignal         = False

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/HZZ4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [Data_Run2017,predCR,WZTo3LNu,qqZZTo4L,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 41.4
        #dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = zx_3p1f_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/HZZ4l/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
