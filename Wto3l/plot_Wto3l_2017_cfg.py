from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

#from Wto3l.Dataset.Run2017.Wto3l_Data import *
#from Wto3l.Dataset.Run2017.Wto3l_MC import *
from Wto3l.Dataset.Run2017.Wto3l_bkg import *
#from Wto3l.Dataset.Run2018.Wto3l_MC import *
from Wto3l.Dataset.Signal.Wmto3l_signal_MC import *
from Wto3l.Dataset.Signal.Wpto3l_signal_MC import *

from Wto3l.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

out_path = "Wto3l/"

general_plots = []
# __________________________________________________________________________________ ||
#sel_3mu = "x.lep_id.size() >= 3 and x.lep_pt.size() >= 3"
sel_iso = " and x.Lep1Iso < 0.35 and x.Lep2Iso < 0.35 and x.Lep3Iso < 0.35"
sel_all = " and x.mt < 150 and x.m3l < 100"
sel_mt = " and x.mt < 150"
sel_m3l = " and x.m3l < 100"

lep1z = "" #" and x.Lep1FromZ == 1"
lep2z = "" #" and x.Lep1FromZ == 1"
lep3z = "" #" and x.Lep3FromZ == 1"
# __________________________________________________________________________________ ||

general_plots.extend([
    Plot("Lep1_pt",             ["TH1D","Lep1_pt","",100,0.,100.],              LambdaFunc('x:x.Lep1.Pt()'),    selFunc=LambdaFunc('x:x.Lep1.Pt() > 0' + sel_iso + sel_mt + lep1z)        ),
    Plot("Lep2_pt",             ["TH1D","Lep2_pt","",100,0.,100.],              LambdaFunc('x:x.Lep2.Pt()'),    selFunc=LambdaFunc('x:x.Lep2.Pt() > 0' + sel_iso + sel_mt + lep2z)        ),
    Plot("Lep3_pt",             ["TH1D","Lep3_pt","",100,0.,100.],              LambdaFunc('x:x.Lep3.Pt()'),    selFunc=LambdaFunc('x:x.Lep3.Pt() > 0' + sel_iso + sel_mt + lep3z)        ),

    Plot("Lep1_eta",            ["TH1D","Lep1_eta","",60,-3.,3.],               LambdaFunc('x:x.Lep1.Eta()'),   selFunc=LambdaFunc('x:x.Lep1.Eta()' + sel_iso + sel_mt + lep1z)           ),
    Plot("Lep2_eta",            ["TH1D","Lep2_eta","",60,-3.,3.],               LambdaFunc('x:x.Lep2.Eta()'),   selFunc=LambdaFunc('x:x.Lep2.Eta()' + sel_iso + sel_mt + lep2z)           ),
    Plot("Lep3_eta",            ["TH1D","Lep3_eta","",60,-3.,3.],               LambdaFunc('x:x.Lep3.Eta()'),   selFunc=LambdaFunc('x:x.Lep3.Eta()' + sel_iso + sel_mt + lep3z)           ),

    Plot("Lep1_phi",            ["TH1D","Lep1_phi","",40,-4.,4.],               LambdaFunc('x:x.Lep1.Phi()'),   selFunc=LambdaFunc('x:x.Lep1.Phi()' + sel_iso + sel_mt + lep1z)           ),
    Plot("Lep2_phi",            ["TH1D","Lep2_phi","",40,-4.,4.],               LambdaFunc('x:x.Lep2.Phi()'),   selFunc=LambdaFunc('x:x.Lep2.Phi()' + sel_iso + sel_mt + lep2z)           ),
    Plot("Lep3_phi",            ["TH1D","Lep3_phi","",40,-4.,4.],               LambdaFunc('x:x.Lep3.Phi()'),   selFunc=LambdaFunc('x:x.Lep3.Phi()' + sel_iso + sel_mt + lep3z)           ),

    Plot("Lep1_Iso",            ["TH1D","Lep1_Iso","",20,0.,1.],                LambdaFunc('x: x.Lep1Iso'),     selFunc=LambdaFunc('x:x.Lep1Iso > 0' + sel_iso + sel_mt + lep1z)          ),
    Plot("Lep2_Iso",            ["TH1D","Lep2_Iso","",20,0.,1.],                LambdaFunc('x: x.Lep2Iso'),     selFunc=LambdaFunc('x:x.Lep2Iso > 0' + sel_iso + sel_mt + lep2z)          ),
    Plot("Lep3_Iso",            ["TH1D","Lep3_Iso","",20,0.,1.],                LambdaFunc('x: x.Lep3Iso'),     selFunc=LambdaFunc('x:x.Lep3Iso > 0' + sel_iso + sel_mt + lep3z)          ),

    Plot("dRLep1Lep2",          ["TH1D","dRLep1Lep2","",100,0.,6.],             LambdaFunc('x:x.dR12'),         selFunc=LambdaFunc('x:x.dR12' + sel_iso + sel_mt + lep1z + lep2z)                 ),
    Plot("dRLep1Lep3",          ["TH1D","dRLep1Lep3","",100,0.,6.],             LambdaFunc('x:x.dR13'),         selFunc=LambdaFunc('x:x.dR13' + sel_iso + sel_mt + lep1z + lep3z)                 ),
    Plot("dRLep2Lep3",          ["TH1D","dRLep2Lep3","",100,0.,6.],             LambdaFunc('x:x.dR23'),         selFunc=LambdaFunc('x:x.dR23' + sel_iso + sel_mt + lep2z + lep3z)                 ),

    Plot("Mass1",               ["TH1D","Mass1","",80,0.,200.],                 LambdaFunc('x:x.mass1'),        selFunc=LambdaFunc('x:x.mass1 > 0' + sel_mt )           ),
    Plot("Mass2",               ["TH1D","Mass2","",80,0.,200.],                 LambdaFunc('x:x.mass2'),        selFunc=LambdaFunc('x:x.mass2 > 0' + sel_mt )           ),
    #Plot("Transverse_Mass",     ["TH1D","Transverse_Mass","",100,0.,500.],      LambdaFunc('x:x.mt'),           selFunc=LambdaFunc('x:x.mt' + sel_iso + sel_mt )                  ),
    #Plot("3l_Inv_Mass",         ["TH1D","3l_Inv_Mass","",100,0.,500.],          LambdaFunc('x:x.m3l'),          selFunc=LambdaFunc('x:x.m3l' + sel_iso + sel_mt)                  ),
   
    #Plot("60_mt",          ["TH1D","60_mt","",100,0.,500.],          LambdaFunc('x:x.m3l'),          selFunc=LambdaFunc('x:x.m3l' + sel_iso + sel_mt)                  ),
    #Plot("60_m3l",         ["TH1D","60_m3l","",100,0.,500.],          LambdaFunc('x:x.m3l'),          selFunc=LambdaFunc('x:x.m3l' + sel_iso + sel_m3l)                  ),
    #Plot("60_all",         ["TH1D","60_all","",100,0.,500.],          LambdaFunc('x:x.m3l'),          selFunc=LambdaFunc('x:x.m3l' + sel_iso + sel_all)                  ),

    Plot("met",                 ["TH1D","met","",50,0.,250.],                   LambdaFunc('x: x.met[0]'),      selFunc=LambdaFunc('x:x.met[0] > 0' + sel_iso + sel_mt)           ),
    Plot("met_phi",             ["TH1D","met_phi","",40,-4.,4.],                LambdaFunc('x: x.met_phi[0]'),  selFunc=LambdaFunc('x:x.met_phi[0]' + sel_iso + sel_mt)           ),

    Plot("MCorrect",           ["TH1D","MCorrect","",2,1.,3.],         LambdaFunc('x: x.MCorrect'),    selFunc=LambdaFunc('x:x.MCorrect'),     ),

    #Plot("lep_pt",             ["TH1D","lep_pt","",200,0.,200.],               LambdaFunc('x:x.lep_pt[0]'),    selFunc=LambdaFunc('x:lep_pt[0]' + sel_mt)              ),
    #Plot("lep_eta",             ["TH1D","lep_eta","",60,-3.,3.],                LambdaFunc('x:x.lep_eta[0]'),   selFunc=LambdaFunc('x:lep_eta[0]' + sel_mt)             ),
    #Plot("lep_phi",             ["TH1D","lep_phi","",40,-4.,4.],                LambdaFunc('x:x.lep_phi[0]'),   selFunc=LambdaFunc('x:lep_phi[0]' + sel_mt)             ),
    #Plot("lep_RelIso",          ["TH1D","lep_RelIso","",20,0.,1.],              LambdaFunc('x:x.lep_RelIso[0]'),selFunc=LambdaFunc('x:lep_RelIso[0]' + sel_mt)          ),

    #Plot("nLeptons",           ["TH1D","nLeptons","",12,2.,15.],               LambdaFunc('x:x.nLeptons[0]'),  selFunc=LambdaFunc('x:x.nLeptons[0]' + sel_mt)          ),
    #Plot("lep_Sip",             ["TH1D","lep_Sip","",4,0.,4.],                 LambdaFunc('x:x.lep_Sip[0]'),   selFunc=LambdaFunc('x:x.lep_Sip[0]' + sel_mt)           ),
        ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 1
outputDir               = "results/"
nEvents                 = -1
disableProgressBar      = False
#componentList		= [DYJetsToLL_M50,WZTo3LNu,TTJets,DYJetsToLL_M10To50,WpTo3munu_ZpM15]
#componentList		= [WZTo3LNu_2017,TTJets_2017,DYJetsToLL_M50_2017,DYJetsToLL_M10To50_2017,Data_Run2017]
#componentList		= [WZTo3LNu_2018,TTJets_2018,DYJetsToLL_M50_2018,DYJetsToLL_M10To50_2018]
#componentList           = [WmTo3l_ZpM15,WmTo3l_ZpM20,WmTo3l_ZpM30,WmTo3l_ZpM45,WmTo3l_ZpM60,WpTo3l_ZpM15,WpTo3l_ZpM20,WpTo3l_ZpM30,WpTo3l_ZpM45,WpTo3l_ZpM60]
#componentList           = [WmTo3l_ZpM15,WmTo3l_ZpM20,WmTo3l_ZpM30,WmTo3l_ZpM45,WmTo3l_ZpM60,WpTo3l_ZpM15,WpTo3l_ZpM20,WpTo3l_ZpM30,WpTo3l_ZpM45,WpTo3l_ZpM60,WZTo3LNu_2017,TTJets_2017,DYJetsToLL_M50_2017,DYJetsToLL_M10To50_2017]
#componentList		= bkgSamples_2017 + dataSamples_2017
#componentList		= bkgSamples_2017 + dataSamples_2017 + [WmTo3l_ZpM15,WpTo3l_ZpM15]
#componentList		= bkgSamples_2017 + [WmTo3l_ZpM60,WpTo3l_ZpM60]
#componentList		= sigmSamples + sigpSamples
componentList 		= bkgSamples_2017 + sigmSamples + sigpSamples
#componentList		= [WpTo3l_ZpM60]#, WmTo3l_ZpM60]
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