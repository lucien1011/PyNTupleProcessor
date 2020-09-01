from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from Wto3l.Dataset.Run2017.Wto3l_MC import *
from Wto3l.Dataset.Run2018.Wto3l_MC import *

from Wto3l.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

out_path = "Wto3l/"

general_plots = []
# __________________________________________________________________________________ ||
sel_3mu = "x.lep_id.size() >= 3 and x.lep_pt.size() >= 3"
# __________________________________________________________________________________ ||

general_plots.extend([
    #Plot("Lep1_pt",          ["TH1D","Lep1_pt","",40,0.,200.],           LambdaFunc('x:x.Lep1.Pt()'),	selFunc=LambdaFunc('x:x.Lep1.Pt() > 0')        ),
    #Plot("Lep2_pt",          ["TH1D","Lep2_pt","",40,0.,200.],           LambdaFunc('x:x.Lep2.Pt()'),	selFunc=LambdaFunc('x:x.Lep2.Pt() > 0')        ),
    #Plot("Lep3_pt",          ["TH1D","Lep3_pt","",200,0.,200.],          LambdaFunc('x:x.Lep3.Pt()'),	selFunc=LambdaFunc('x:x.Lep3.Pt > 0')        ),

    #Plot("Lep1_eta",         ["TH1D","Lep1_eta","",60,-3.,3.],           LambdaFunc('x:x.Lep1.Eta()'),  selFunc=LambdaFunc('x:x.Lep1.Eta()')        ),
    #Plot("Lep2_eta",         ["TH1D","Lep2_eta","",60,-3.,3.],           LambdaFunc('x:x.Lep2.Eta()'),  selFunc=LambdaFunc('x:x.Lep2.Eta()')        ),
    #Plot("Lep3_eta",         ["TH1D","Lep3_eta","",60,-3.,3.],           LambdaFunc('x:x.Lep3.Eta()'),	selFunc=LambdaFunc('x:x.Lep3.Eta()')        ),

    #Plot("Lep1_phi",         ["TH1D","Lep1_phi","",40,-4.,4.],           LambdaFunc('x:x.Lep1.Phi()'),  selFunc=LambdaFunc('x:x.Lep1.Phi()')        ),
    #Plot("Lep2_phi",         ["TH1D","Lep2_phi","",40,-4.,4.],           LambdaFunc('x:x.Lep2.Phi()'),  selFunc=LambdaFunc('x:x.Lep2.Phi()')        ),
    #Plot("Lep3_phi",         ["TH1D","Lep3_phi","",40,-4.,4.],           LambdaFunc('x:x.Lep3.Phi()'),  selFunc=LambdaFunc('x:x.Lep3.Phi()')        ),

    #Plot("3lep_pt",          ["TH1D","3lep_pt","",40,0.,200.],           LambdaFunc('x:x.pT3l[0]'),	selFunc=LambdaFunc('x:x.pT3l[0] > 0')        ),
    #Plot("Lep1+Lep2_pt",     ["TH1D","Lep1+Lep2_pt","",40,0.,200.],      LambdaFunc('x:x.twolpt'),	selFunc=LambdaFunc('x:x.twolpt > 0')      ),
    #Plot("Mass1",            ["TH1D","Mass1","",80,0.,200.],             LambdaFunc('x:x.mass1'),       selFunc=LambdaFunc('x:x.mass1 > 0')        ),
    #Plot("Mass2",            ["TH1D","Mass2","",80,0.,200.],             LambdaFunc('x:x.mass2'),       selFunc=LambdaFunc('x:x.mass2 > 0')        ),
    #Plot("Transverse_Mass",  ["TH1D","Transverse_Mass","",100,0.,500.],            LambdaFunc('x:x.mt'),                selFunc=LambdaFunc('x:x.mt')        ),
    #Plot("Mass1vsMass2",     ["TH2D","Mass1_vs_Mass2","",80,0.,200.,80,0.,200.],   LambdaFunc('x:[x.mass1,x.mass2]'),	selFunc=LambdaFunc('x:[x.mass1 > 0,x.mass2 > 0]'),   dim = 2 ),
                  
    Plot("met",              ["TH1D","met","",50,0.,250.],               LambdaFunc('x: x.met[0]'),   	selFunc=LambdaFunc('x:x.met[0] > 0 and '+sel_3mu),     ),
    Plot("met_phi",          ["TH1D","met_phi","",40,-4.,4.],            LambdaFunc('x: x.met_phi[0]'), selFunc=LambdaFunc('x:x.met_phi[0]'),     ),

    #Plot("IsoL3",            ["TH1D","IsoL3","",20,0.,1.],               LambdaFunc('x: x.IsoL3[0]'),   selFunc=LambdaFunc('x:x.IsoL3[0] > 0'),     ), 
        ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 1
outputDir               = "results/"
nEvents                 = -1
disableProgressBar      = False
#componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,Data_Run2016,Data_sr_Run2016,WmTo3munu_ZpM45,WmTo3munu_ZpM15,WpTo3munu_ZpM45,WpTo3munu_ZpM15]#predCR]
#componentList           = [WZTo3LNu,Data_Run2016,WmTo3munu_ZpM45,WmTo3munu_ZpM15,WpTo3munu_ZpM45,WpTo3munu_ZpM15]
#componentList           = [WmTo3munu_ZpM15]
#componentList           = [WZTo3LNu,Data_Run2016,Data_sr_Run2016]
#componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,WmTo3munu_ZpM45,WmTo3munu_ZpM15,WpTo3munu_ZpM45,WpTo3munu_ZpM15]
#componentList		= [DYJetsToLL_M50,WZTo3LNu,TTJets,DYJetsToLL_M10To50,WpTo3munu_ZpM15]
componentList		= [WZTo3LNu_2017,TTJets_2017,DYJetsToLL_M50_2017,DYJetsToLL_M10To50_2017]
#componentList		= [WZTo3LNu_2018,TTJets_2018,DYJetsToLL_M50_2018,DYJetsToLL_M10To50_2018]
#componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,Data_sr_Run2016]
#componentList		= [WZTo3LNu_2018]
#componentList           = [DYJetsToLL_M50_memCR,DYJetsToLL_M10To50_memCR,TTJets_memCR,WZTo3LNu_memCR,Data_memCR_sr_Run2016]
#componentList           = [Data_memCR_sr_Run2016,Data_memCR_Run2016,WZTo3LNu_memCR]
#componentList           = [Data_memCR_sr_Run2016]
#componentList           = [Data_memCR_sr_Run2016,WZTo3LNu_memCR,DYJetsToLL_M50_memCR,DYJetsToLL_M10To50_memCR,TTJets_memCR]
#componentList           = [TTJets_fromT,TTJets_notfromT]
#componentList           = [TTJets_memCR]
#componentList           = [DYJetsToLL_M50_memCR]
#componentList           = [WmTo3munu_ZpM45,WmTo3munu_ZpM15,WpTo3munu_ZpM45,WpTo3munu_ZpM15]
#componentList           = [WZTo3LNu,Data_Run2016]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 35.9 #2016
	dataset.lumi = 41.4 #2017
	#dataset.lumi = 59.7 #2018
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = Wto3l_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = outputDir+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
