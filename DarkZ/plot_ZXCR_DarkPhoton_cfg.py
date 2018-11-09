
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

#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/2018-09-05/"
#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l118-130/2018-10-23/"
out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l118-130/2018-11-06/"

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [30,0.,60.]
#mZ2PlotRange = [60,0.,120.]
#h4lPlotRange = [100,0.,500.]
h4lPlotRange = [20,100.,140.]
deltaRPlotRange2 = [40,0.,4.]
deltaRPlotRange = [40,0.,4.]
general_plots = []
for eachCR in ["3p1f","2p2f"]:
    if eachCR == "3p1f":
        region_sel_str = "x.nZXCRFailedLeptons[0] == 1"
        region_sel_str_whole = "x: x.nZXCRFailedLeptons[0] == 1"
    else:
        region_sel_str = "x.nZXCRFailedLeptons[0] == 2"
        region_sel_str_whole = "x: x.nZXCRFailedLeptons[0] == 2"

    general_plots.extend([
        Plot("Z1_mass_"+eachCR,         ["TH1D","Z1_mass_"+eachCR,"",]+mZ1PlotRange,        LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc(region_sel_str_whole)      ),
        Plot("Z2_mass_vs_DeltaR34_"+eachCR,["TH2D","Z2_mass_vs_DeltaR34_"+eachCR,"",]+mZ2PlotRange+deltaRPlotRange2,LambdaFunc('x: [x.massZ2[0],x.deltaRL34]'),selFunc=LambdaFunc(region_sel_str_whole),dim=2),
        Plot("Z2_mass_"+eachCR,         ["TH1D","Z2_mass_"+eachCR,"",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(region_sel_str_whole)      ),
        Plot("Z1_4e_mass_"+eachCR,      ["TH1D","Z1_4e_mass_"+eachCR,"",]+mZ1PlotRange,     LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
        Plot("Z2_4e_mass_"+eachCR,      ["TH1D","Z2_4e_mass_"+eachCR,"",]+mZ2PlotRange,     LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
        Plot("Z1_4mu_mass_"+eachCR,     ["TH1D","Z1_4mu_mass_"+eachCR,"",]+mZ1PlotRange,    LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)         ),
        Plot("Z2_4mu_mass_"+eachCR,     ["TH1D","Z2_4mu_mass_"+eachCR,"",]+mZ2PlotRange,    LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)         ),
        Plot("Z1_2e2mu_mass_"+eachCR,   ["TH1D","Z1_2e2mu_mass_"+eachCR,"",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13 and '+region_sel_str)       ),
        Plot("Z2_2e2mu_mass_"+eachCR,   ["TH1D","Z2_2e2mu_mass_"+eachCR,"",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13 and '+region_sel_str)       ),
        Plot("Z1_2mu2e_mass_"+eachCR,   ["TH1D","Z1_2mu2e_mass_"+eachCR,"",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11 and '+region_sel_str)       ),
        Plot("Z2_2mu2e_mass_"+eachCR,   ["TH1D","Z2_2mu2e_mass_"+eachCR,"",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11 and '+region_sel_str)       ),
              
        Plot("h4L_mass_"+eachCR,        ["TH1D","h4L_mass_"+eachCR,"",]+h4lPlotRange,       LambdaFunc('x: x.mass4l[0]'),       selFunc=LambdaFunc(region_sel_str_whole)                                  ),
        Plot("h4e_mass_"+eachCR,        ["TH1D","h4e_mass_"+eachCR,"",]+h4lPlotRange,       LambdaFunc('x: x.mass4e[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)        ),
        Plot("h4mu_mass_"+eachCR,       ["TH1D","h4mu_mass_"+eachCR,"",]+h4lPlotRange,      LambdaFunc('x: x.mass4mu[0]'),      selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)       ),
        Plot("h2e2mu_mass_"+eachCR,     ["TH1D","h2e2mu_mass_"+eachCR,"",]+h4lPlotRange,    LambdaFunc('x: x.mass2e2mu[0]'),    selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13 and '+region_sel_str)     ),
        Plot("h2mu2e_mass_"+eachCR,     ["TH1D","h2mu2e_mass_"+eachCR,"",]+h4lPlotRange,    LambdaFunc('x: x.mass2e2mu[0]'),    selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11 and '+region_sel_str)     ),
        
        Plot("met_"+eachCR,             ["TH1D","met_"+eachCR,"",40,0.,200.],               LambdaFunc('x: x.met[0]'),          selFunc=LambdaFunc(region_sel_str_whole),     ),
        Plot("nVtx_"+eachCR,            ["TH1D","nVtx_"+eachCR,"",30,0.0,60.0],             LambdaFunc('x: x.nVtx[0]'),         selFunc=LambdaFunc(region_sel_str_whole),     ),
        
        Plot("DeltaRL12_"+eachCR,       ["TH1D","DeltaL12_"+eachCR,"",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL12'),         selFunc=LambdaFunc(region_sel_str_whole),       ),
        Plot("DeltaRL13_"+eachCR,       ["TH1D","DeltaL13_"+eachCR,"",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL13'),         selFunc=LambdaFunc(region_sel_str_whole),       ),
        Plot("DeltaRL14_"+eachCR,       ["TH1D","DeltaL14_"+eachCR,"",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL14'),         selFunc=LambdaFunc(region_sel_str_whole),       ),
        Plot("DeltaRL23_"+eachCR,       ["TH1D","DeltaL23_"+eachCR,"",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL23'),         selFunc=LambdaFunc(region_sel_str_whole),       ),
        Plot("DeltaRL24_"+eachCR,       ["TH1D","DeltaL24_"+eachCR,"",]+deltaRPlotRange,  LambdaFunc('x: x.deltaRL24'),         selFunc=LambdaFunc(region_sel_str_whole),       ),
        Plot("DeltaRL34_"+eachCR,       ["TH1D","DeltaL34_"+eachCR,"",]+deltaRPlotRange2,  LambdaFunc('x: x.deltaRL34'),        selFunc=LambdaFunc(region_sel_str_whole),       ),
        Plot("MinDeltaRL_"+eachCR,      ["TH1D","MinDeltaRL_"+eachCR,"",]+deltaRPlotRange2,  LambdaFunc('x: x.minDeltaRL'),     selFunc=LambdaFunc(region_sel_str_whole),       ),
        ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,Data_Run2016,]#predCR]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_cr_v2_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
