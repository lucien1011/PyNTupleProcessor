
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2016.Upsilon_Data import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

isDarkPhotonReco = True

if isDarkPhotonReco:
    #out_path = "Upsilon/DataMCDistributions/SkimTree_mZ18p96-9p96_DarkPhotonReco/2018-09-10/"
    out_path = "Upsilon/DataMCDistributions/SkimTree_mZ18p96-9p96_DarkPhotonReco_DarkPhotonSelection/2018-09-10/"
    mZ1PlotRange = [60,0.,120.]
    mZ2PlotRange = [60,0.,120.]
    h4lPlotRange = [75,50.,200.]
    Data_Run2016.componentList = ComponentList(
        [
            Component("Data_Run2016","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco//Data_Run2016-03Feb2017_4l_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
else:
    out_path = "Upsilon/DataMCDistributions/SkimTree_mZ18p96-9p96/2018-09-10/"
    mZ1PlotRange = [20,8.96,9.96]
    mZ2PlotRange = [100,0.,200.]
    h4lPlotRange = [200,0.,400.]
    Data_Run2016.componentList = ComponentList(
        [
            Component("Data_Run2016","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1//Data_Run2016-03Feb2017_4l_1.root","passedEvents",inUFTier2=False),
        ]
        )

general_plots = []
region_sel_str = "True"
region_sel_str_whole = "x: True"
general_plots.extend([
        Plot("Z1_mass",         ["TH1D","Z1_mass","",]+mZ1PlotRange,        LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc(region_sel_str_whole)      ),
        Plot("Z2_mass",         ["TH1D","Z2_mass","",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(region_sel_str_whole)      ),
        Plot("Z1_4e_mass",      ["TH1D","Z1_4e_mass","",]+mZ1PlotRange,     LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
        Plot("Z2_4e_mass",      ["TH1D","Z2_4e_mass","",]+mZ2PlotRange,     LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
        Plot("Z1_4mu_mass",     ["TH1D","Z1_4mu_mass","",]+mZ1PlotRange,    LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)         ),
        Plot("Z2_4mu_mass",     ["TH1D","Z2_4mu_mass","",]+mZ2PlotRange,    LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)         ),
        Plot("Z1_2e2mu_mass",   ["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and '+region_sel_str)       ),
        Plot("Z2_2e2mu_mass",   ["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange,  LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and '+region_sel_str)       ),
              
        Plot("h4L_mass",        ["TH1D","h4L_mass","",]+h4lPlotRange,       LambdaFunc('x: x.mass4l[0]'),       selFunc=LambdaFunc(region_sel_str_whole)                                  ),
        Plot("h4e_mass",        ["TH1D","h4e_mass","",]+h4lPlotRange,       LambdaFunc('x: x.mass4e[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)        ),
        Plot("h4mu_mass",       ["TH1D","h4mu_mass","",]+h4lPlotRange,      LambdaFunc('x: x.mass4mu[0]'),      selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and '+region_sel_str)       ),
        Plot("h2e2mu_mass",     ["TH1D","h2mu2e_mass","",]+h4lPlotRange,    LambdaFunc('x: x.mass2e2mu[0]'),    selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and '+region_sel_str)     ),
        
        Plot("h4Lmass_vs_Z1mass",["TH2D","h4Lmass_vs_Z1mass","",]+h4lPlotRange+mZ1PlotRange, LambdaFunc('x: [x.mass4l[0],x.massZ1[0]]'), dim=2, selFunc=LambdaFunc(region_sel_str_whole)),
        Plot("h4Lmass_vs_Z2mass",["TH2D","h4Lmass_vs_Z2mass","",]+h4lPlotRange+mZ2PlotRange, LambdaFunc('x: [x.mass4l[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(region_sel_str_whole)),
        Plot("Z1mass_vs_Z2mass",["TH2D","Z1mass_vs_Z2mass","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(region_sel_str_whole)),
        ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 5
outputDir               = "/raid/raid7/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [Data_Run2016,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

#sequence                = upsilon_sequence
sequence                = upsilon_signal_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
