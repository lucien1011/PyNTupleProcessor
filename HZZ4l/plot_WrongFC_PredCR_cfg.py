
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from HZZ4l.Dataset.Run2016.WrongFC_MC import * 
from HZZ4l.Dataset.Run2016.WrongFC_Data import * 

from HZZ4l.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

out_path = "WrongFC/DataMCDistributions/SkimTree_WrongFC_Run2016Data_v1/2018-12-10_3P1F/"

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [60,0.,120.]
h4lPlotRange = [110,60.,500.]

general_plots = []
eachCR = "3p1f"
general_plots.extend([
    Plot("Z1_mass_"+eachCR,         ["TH1D","Z1_mass_"+eachCR,"",]+mZ1PlotRange,        LambdaFunc('x: x.massZ1[0]'),),       #selFunc=LambdaFunc(region_sel_str_whole)      ),
    Plot("Z2_mass_"+eachCR,         ["TH1D","Z2_mass_"+eachCR,"",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),),       #selFunc=LambdaFunc(region_sel_str_whole)      ), 
    Plot("h4L_mass_"+eachCR,        ["TH1D","h4L_mass_"+eachCR,"",]+h4lPlotRange,       LambdaFunc('x: x.mass4l[0]'),),       #selFunc=LambdaFunc(region_sel_str_whole)      ), 
    Plot("met_"+eachCR,             ["TH1D","met_"+eachCR,"",40,0.,200.],               LambdaFunc('x: x.met[0]'),   ),       #selFunc=LambdaFunc(region_sel_str_whole),     ),
    Plot("nVtx_"+eachCR,            ["TH1D","nVtx_"+eachCR,"",30,0.0,60.0],             LambdaFunc('x: x.nVtx[0]'),  ),       #selFunc=LambdaFunc(region_sel_str_whole),     ),
    ])

plots =  general_plots

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/HZZ4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,Data_Run2016,predCR,]
justEndSequence         = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = wrongFC_3p1f_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/HZZ4l/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
