from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2017.SkimTree_DarkPhoton_m4l70 import * 
from DarkZ.Sequence.RecoSequence import * 
from DarkZ.Producer.VariableProducer import VariableProducer

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.MergeSampleDict import mergeSampleDict

import copy

mZ1PlotRange = [40,40.,120.]
mZ2PlotRange = [30,0.,60.]
#h4lPlotRange = [110,60.,500.]
#h4lPlotRange = [25,100.,150.]
h4lPlotRange = [20,100.,140.]
deltaRPlotRange2 = [20,0.,2.]
deltaRPlotRange = [40,0.,4.]


User                    = os.environ['USER']
out_path                = "ZPlusX/Systematic/2019-05-03_Run2017/"
lumi                    = 41.4
nCores                  = 3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [ZPlusX,] 
justEndSequence         = False

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
        
        Plot("met",         ["TH1D","met","",40,0.,200.],       LambdaFunc('x: x.met[0]'),          ),
        Plot("nVtx",        ["TH1D","nVtx","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]')),
        Plot("nVtx_4mu",        ["TH1D","nVtx_4mu","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')),
        Plot("nVtx_4e",        ["TH1D","nVtx_4e","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')),
        Plot("nVtx_2e2mu",        ["TH1D","nVtx_2e2mu","",30,0.0,60.0],      LambdaFunc('x: x.nVtx[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0')),
        ]

syst_UniIso_plots = []
syst_AsymIso_plots = []
for p in general_plots:
    new_UniIso_p = copy.deepcopy(p)
    new_UniIso_p.getEventWeight = LambdaFunc('x: x.weight*x.weight_FRUniIso')
    new_UniIso_p.key += "_UniIso"
    new_UniIso_p.rootSetting[1] += "_UniIso"
    syst_UniIso_plots.append(new_UniIso_p)

    new_AsymIso_p = copy.deepcopy(p)
    new_AsymIso_p.getEventWeight = LambdaFunc('x: x.weight*x.weight_FRAsymIso')
    new_AsymIso_p.key += "_AsymIso"
    new_AsymIso_p.rootSetting[1] += "_AsymIso"
    syst_AsymIso_plots.append(new_AsymIso_p)


plots = general_plots + syst_AsymIso_plots + syst_UniIso_plots

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)
variableProducer        = VariableProducer("VariableProducer")

sequence                = zx_syst_signal_sequence
sequence.add(variableProducer)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Higgs/DarkZ/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))
