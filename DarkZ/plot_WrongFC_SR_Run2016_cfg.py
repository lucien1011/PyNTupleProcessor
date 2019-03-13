
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2016.WrongFC_MC import * 
from DarkZ.Dataset.Run2016.WrongFC_Data import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l70_Run2016Data_v1/2018-09-20/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l108To140_Run2016Data_v1/2018-10-24_SR/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_WFC_m4l118To130_Run2016Data_v1/2019-01-21_SR/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l70/2019-03-08_SR_FRWeightUniIso/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-08_SR_FRWeight-mZ2-6/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l70/2019-03-08_SR_FRWeight-mZ2-6/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-08_SR_FRWeight-mZ2-6/"
#out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-08_SR/"

out_path = "WrongFC/DataMCDistributions/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l118-130/2019-03-13_SR_FRWeight-mZ2-6/"

#mZ1PlotRange = [60,0.,120.]
#mZ2PlotRange = [60,0.,120.]
#h4lPlotRange = [56,60.,600.]
mZ1PlotRange = [40,40.,120.]
#mZ2PlotRange = [60,0.,120.]
mZ2PlotRange = [30,0.,60.]
h4lPlotRange = [20,100.,140.]

#sel_str_4e = "x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
#sel_str_4mu = "x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"
#sel_str_2mu2e = "x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
#sel_str_2e2mu = "x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"

general_plots = []
general_plots.extend([
    Plot("Z1_mass", ["TH1D","Z1_mass","",]+mZ1PlotRange, LambdaFunc('x: x.massZ1[0]'),),
    Plot("Z2_mass", ["TH1D","Z2_mass","",]+mZ2PlotRange, LambdaFunc('x: x.massZ2[0]'),),
    #Plot("Z1_4e_mass", ["TH1D","Z1_4e_mass","",]+mZ1PlotRange, LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc(sel_str_4e),),
    #Plot("Z2_4e_mass", ["TH1D","Z2_4e_mass","",]+mZ2PlotRange, LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc(sel_str_4e),),
    #Plot("Z1_4mu_mass", ["TH1D","Z1_4mu_mass","",]+mZ1PlotRange, LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc(sel_str_4mu),),
    #Plot("Z2_4mu_mass", ["TH1D","Z2_4mu_mass","",]+mZ2PlotRange, LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc(sel_str_4mu),),
    #Plot("Z1_2e2mu_mass", ["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange, LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc(sel_str_2e2mu),),
    #Plot("Z2_2e2mu_mass", ["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange, LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc(sel_str_2e2mu),),
    #Plot("Z2_2mu2e_mass", ["TH1D","Z2_2mu2e_mass","",]+mZ2PlotRange, LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc(sel_str_2mu2e),), 
    Plot("h4L_mass", ["TH1D","h4L_mass","",]+h4lPlotRange, LambdaFunc('x: x.mass4l[0]'),),
    #Plot("h4e_mass", ["TH1D","h4e_mass","",]+h4lPlotRange, LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc(sel_str_4e),),
    #Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc(sel_str_4mu),),
    #Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc(sel_str_2e2mu),),
    #Plot("h2mu2e_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc(sel_str_2mu2mu),),
    ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 3
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [qqZZTo4L,Data_Run2016,WFC_Reducible,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = wrongFC_signal_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
