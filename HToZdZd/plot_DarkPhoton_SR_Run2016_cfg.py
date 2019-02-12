from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Dataset.Run2016.SkimTree_DarkSUSY_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_HToZdZd_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

mergeSampleDict = {
        "ggH":  ["ggH"],
        "VBF":  ["VBF"],
        "WH":   ["WHPlus","WHminus",],
        "ZH":   ["ZH",],
        "qqZZ": ["qqZZTo4L",],
        "ggZZ": [
            "ggZZTo2e2mu",
            "ggZZTo2e2tau",
            "ggZZTo2mu2tau",
            "ggZZTo4e",
            "ggZZTo4mu",
            "ggZZTo4tau",
            ],
        "VVVVBS": [
            "WWW_4F",
            "WWZ",
            "WZZ",
            "ZZZ",
            "WpWpJJ",
            "WWTo2L2Nu",
            ],
        "ZPlusX": ["ZPlusX"],
        }

mZ1PlotRange = [50,0.,100.]
mZ2PlotRange = [50,0.,100.]
h4lPlotRange = [70,60.,200.]
#h4lPlotRange = [140,60.,200.]

#out_path                = "DarkPhotonSB/DataMCDistributions/2019-12-14_Run2016/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-02-05_Run2016MC/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-02-05_test/"
out_path                = "DarkPhotonSB/DataMCDistributions/2019-02-07_test_ratio0p05/"
lumi                    = 35.9
nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [data2016,] + [HToZdZd_MZD30,] 
#componentList           = [HToZdZd_MZD30,] 
#componentList           = bkgSamples + [
#componentList           = [
#                                            HToZdZd_MZD15,
#                                            HToZdZd_MZD30,
#                                            HToZdZd_MZD50,
#                                            HToZdZd_MZD60,
#                                        ] 
justEndSequence         = False


muon_plots = [
        ]

general_plots = [
        Plot("Z1_mass",     ["TH1D","Z1_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       ),
        Plot("Z2_mass",     ["TH1D","Z2_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'),       ),
        Plot("Z1_4e_mass",     ["TH1D","Z1_4e_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')      ),
        Plot("Z2_4e_mass",     ["TH1D","Z2_4e_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')     ),
        Plot("Z1_4mu_mass",     ["TH1D","Z1_4mu_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')      ),
        Plot("Z2_4mu_mass",     ["TH1D","Z2_4mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')     ),
        Plot("Z1_2e2mu_mass",     ["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')      ),
        Plot("Z2_2e2mu_mass",     ["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')     ),
        Plot("Z2_2mu2e_mass",     ["TH1D","Z2_2mu2e_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')     ),
              
        Plot("h4L_mass",    ["TH1D","h4L_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'),       ),
        #Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')       ),
        #Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')       ),
        #Plot("h2e2mu_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')       ),
        Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')       ),
        Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and x.mass4e[0] < 0 and x.mass2e2mu[0] < 0')       ),
        #Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0')       ),
        Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')       ),
        Plot("h2mu2e_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')       ),
        Plot("h4L_Pt",      ["TH1D","h4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
        
        #Plot("met",         ["TH1D","met","",40,0.,200.],       LambdaFunc('x: x.met[0]'),          ),
        #Plot("nVtx",        ["TH1D","nVtx","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]')),
        #Plot("nVtx_4mu",        ["TH1D","nVtx_4mu","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
        #Plot("nVtx_4e",        ["TH1D","nVtx_4e","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
        #Plot("nVtx_2e2mu",        ["TH1D","nVtx_2e2mu","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')),
        #  
        #Plot("Z1mass_vs_Z2mass",["TH2D","Z1mass_vs_Z2mass","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, ),#selFunc=LambdaFunc(region_sel_str_whole)),
        ]

jet_plots = [
        #Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

plots = muon_plots + general_plots + jet_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_fullm4l_sequence
#sequence                = darkphoton_sb_sequence
#sequence                = darkphoton_signal_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))
