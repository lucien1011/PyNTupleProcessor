from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from DarkZ.Dataset.Run2016.Upsilon_Data import * 
from DarkZ.Dataset.Run2016.Upsilon_MC import * 
from DarkZ.Dataset.Run2016.Upsilon_ZX import * 

from DarkZ.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

mergeSampleDict = {
        #"ggH":  ["ggH"],
        #"VBF":  ["VBF"],
        #"WH":   ["WHPlus","WHminus",],
        #"ZH":   ["ZH",],
        "qqZZ": ["qqZZTo4L",],
        "ggZZ": [
            "ggZZTo2e2mu",
            "ggZZTo2e2tau",
            "ggZZTo2mu2tau",
            "ggZZTo4e",
            "ggZZTo4mu",
            "ggZZTo4tau",
            ],
        "ZPlusX": ["ZPlusX"],
        }

isDarkPhotonReco = True

if isDarkPhotonReco:
    out_path = "Upsilon/DataMCDistributions/SkimTree_mZ18p96-9p96_DarkPhotonReco/2018-09-11/"
    #out_path = "Upsilon/DataMCDistributions/SkimTree_mZ18p96-9p96_DarkPhotonReco_DarkPhotonSelection/2018-09-10/"
    mZ1PlotRange = [60,0.,120.]
    mZ2PlotRange = [30,0.,60.]
    h4lPlotRange = [75,50.,200.]
    Data_Run2016.componentList = ComponentList(
        [
            Component("Data_Run2016","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco//Data_Run2016-03Feb2017_4l_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
    qqZZTo4L.componentList = ComponentList(
        [
            Component("qqZZTo4L","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco/ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
    ggZZTo4tau.componentList = ComponentList(
        [
            Component("ggZZTo4tau","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
    ggZZTo4e.componentList = ComponentList(
        [
            Component("ggZZTo4e","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
    ggZZTo4mu.componentList = ComponentList(
        [
            Component("ggZZTo4mu","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
    ggZZTo2mu2tau.componentList = ComponentList(
        [
            Component("ggZZTo2mu2tau","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
    ggZZTo2e2mu.componentList = ComponentList(
        [
            Component("ggZZTo2e2mu","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=False),
        ]
        )
    ggZZTo2e2tau.componentList = ComponentList(
        [
            Component("ggZZTo2e2tau","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1_DarkPhotonReco/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8_RunIISummer16MiniAODv2_1_1.root","passedEvents",inUFTier2=False),
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
    qqZZTo4L.componentList = ComponentList(
        [
            Component("qqZZTo4L","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_Upsilon_Run2016Data_v1/ZZTo4L_13TeV_powheg_pythia8_RunIISummer16MiniAODv2_1.root","passedEvents",inUFTier2=False),
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
componentList           = [
        Data_Run2016,
        qqZZTo4L,
        ZPlusX,
        ggZZTo2e2mu,
        ggZZTo2e2tau,
        ggZZTo2mu2tau,
        ggZZTo4e,
        ggZZTo4mu,
        ggZZTo4tau,
        ]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = upsilon_sequence
#sequence                = upsilon_signal_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/lucien/public_html/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
