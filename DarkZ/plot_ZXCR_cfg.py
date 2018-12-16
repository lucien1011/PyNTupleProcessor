
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2016.ZXCR_MC import * 
from DarkZ.Dataset.Run2016.ZXCR_Data import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "DataMCDistributions/SkimTree_ZXCR_HIG-16-041Selection_Run2016DataMC_v2/2018-08-23/"
out_path = "ZPlusX/DataMCDistributions/SkimTree_PedjaInput_HIG-16-041/2018-09-24/"

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [30,0.,60.]
h4lPlotRange = [110,60.,500.]
#h4lPlotRange = [20,100.,140.]
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
        Plot("Z2_mass_"+eachCR,         ["TH1D","Z2_mass_"+eachCR,"",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(region_sel_str_whole)      ),
        Plot("Z1_4e_mass_"+eachCR,      ["TH1D","Z1_4e_mass_"+eachCR,"",]+mZ1PlotRange,     LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
        Plot("Z2_4e_mass_"+eachCR,      ["TH1D","Z2_4e_mass_"+eachCR,"",]+mZ2PlotRange,     LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
        Plot("Z1_4mu_mass_"+eachCR,     ["TH1D","Z1_4mu_mass_"+eachCR,"",]+mZ1PlotRange,    LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)         ),
        Plot("Z2_4mu_mass_"+eachCR,     ["TH1D","Z2_4mu_mass_"+eachCR,"",]+mZ2PlotRange,    LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)         ),
        Plot("Z1_2e2mu_mass_"+eachCR,   ["TH1D","Z1_2e2mu_mass_"+eachCR,"",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and '+region_sel_str)       ),
        Plot("Z2_2e2mu_mass_"+eachCR,   ["TH1D","Z2_2e2mu_mass_"+eachCR,"",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and '+region_sel_str)       ),
              
        Plot("h4L_mass_"+eachCR,        ["TH1D","h4L_mass_"+eachCR,"",]+h4lPlotRange,       LambdaFunc('x: x.mass4l[0]'),       selFunc=LambdaFunc(region_sel_str_whole)                                  ),
        Plot("h4e_mass_"+eachCR,        ["TH1D","h4e_mass_"+eachCR,"",]+h4lPlotRange,       LambdaFunc('x: x.mass4e[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)        ),
        Plot("h4mu_mass_"+eachCR,       ["TH1D","h4mu_mass_"+eachCR,"",]+h4lPlotRange,      LambdaFunc('x: x.mass4mu[0]'),      selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)       ),
        Plot("h2e2mu_mass_"+eachCR,     ["TH1D","h2mu2e_mass_"+eachCR,"",]+h4lPlotRange,    LambdaFunc('x: x.mass2e2mu[0]'),    selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and '+region_sel_str)     ),
        
        Plot("met_"+eachCR,             ["TH1D","met_"+eachCR,"",40,0.,200.],               LambdaFunc('x: x.met[0]'),          selFunc=LambdaFunc(region_sel_str_whole),     ),
        Plot("nVtx_"+eachCR,            ["TH1D","nVtx_"+eachCR,"",30,0.0,60.0],             LambdaFunc('x: x.nVtx[0]'),         selFunc=LambdaFunc(region_sel_str_whole),     ),
        ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,Data_Run2016,predCR]
#componentList           = [PedjaData_Run2016,PedjaPredCR]
componentList           = [PedjaData_Run2016,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = higgs_3p1f_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
