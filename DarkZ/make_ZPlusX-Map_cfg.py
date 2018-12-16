from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import ZPlusX
from DarkZ.Sequence.RecoSequence import * 

from DarkZ.EndModule.ZPlusXEndModule import SignMapMaker

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [30,0.,120.]
#h4lPlotRange = [110,60.,500.]
#h4lPlotRange = [25,100.,150.]
h4lPlotRange = [20,100.,140.]

#out_path                = "SignalDistributions/2018-09-18_Epsilon0p1_LowMZD/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2018-09-21_UniformIso/"
out_path                = "ZPlusX/Misc/SignMap/2018-10-19/"
lumi                    = 35.9
nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [ZPlusX]
justEndSequence         = True

general_plots = [
        Plot("Z1_mass", ["TH1D","Z1_mass","",]+mZ1PlotRange,LambdaFunc('x: x.massZ1[0]'),),
        Plot("Z2_mass", ["TH1D","Z2_mass","",]+mZ2PlotRange,LambdaFunc('x: x.massZ2[0]'),),
        Plot("Z1_4e_mass",["TH1D","Z1_4e_mass","",]+mZ1PlotRange,LambdaFunc('x: x.massZ1[0]'),selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
        Plot("Z2_4e_mass",["TH1D","Z2_4e_mass","",]+mZ2PlotRange,LambdaFunc('x: x.massZ2[0]'),selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
        Plot("Z1_4mu_mass",["TH1D","Z1_4mu_mass","",]+mZ1PlotRange,LambdaFunc('x: x.massZ1[0]'),selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
        Plot("Z2_4mu_mass",["TH1D","Z2_4mu_mass","",]+mZ2PlotRange,LambdaFunc('x: x.massZ2[0]'),selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
        Plot("Z1_2e2mu_mass",["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange,LambdaFunc('x: x.massZ1[0]'),selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')),
        Plot("Z2_2e2mu_mass",["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange,LambdaFunc('x: x.massZ2[0]'),selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')),
        Plot("h4L_mass",["TH1D","h4L_mass","",]+h4lPlotRange,LambdaFunc('x: x.mass4l[0]'),),
        Plot("h4e_mass",["TH1D","h4e_mass","",]+h4lPlotRange,LambdaFunc('x: x.mass4e[0]'),selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')),
        Plot("h4mu_mass",["TH1D","h4mu_mass","",]+h4lPlotRange,LambdaFunc('x: x.mass4mu[0]'),selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and x.mass4e[0] < 0 and x.mass2e2mu[0] < 0')),
        Plot("h2e2mu_mass",["TH1D","h2mu2e_mass","",]+h4lPlotRange,LambdaFunc('x: x.mass2e2mu[0]'),selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0')),
        ]

plots =  general_plots

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=False,haddAllSamples=True)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path+"/SignMap.pck"
endSequence.add(SignMapMaker(endModuleOutputDir,plots))
