
from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

#from DarkZ.Dataset.Run2016.ZXCR_MC_DarkPhoton import * 
#from DarkZ.Dataset.Run2016.ZXCR_Data_DarkPhoton import * 

from Wto3l.Dataset.Run2016.Wto3l_Data import *
from Wto3l.Dataset.Run2016.Wto3l_MC import *
from Wto3l.Dataset.Run2016.Wto3l_Data_sr import *
from Wto3l.Dataset.Run2016.Wto3l_MC_sr import *
from Wto3l.Dataset.Run2016.Wto3l_memCR_Data import *
from Wto3l.Dataset.Run2016.Wto3l_memCR_Data_sr import *
from Wto3l.Dataset.Run2016.Wto3l_memCR_MC import *
from Wto3l.Dataset.Run2016.TTbar_test import *

from Wto3l.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

#out_path = "ZPlusX/DataMCDistributions/SkimTree_DarkPhoton_ZX_Run2016Data_m4l118-130/2018-11-06/"
#out_path = "Wto3l/DataMCDistributions/Run2016/2019-07-21/"
#out_path = "Wto3l/DataMCDistributions/Run2016/2019-07-25/looselepton_CR/"
#out_path = "Wto3l/DataMCDistributions/Run2016/2019-07-25/MConly_SR/"
#out_path = "Wto3l/DataMCDistributions/Run2016/2019-07-25/TTbar_test/"
#out_path = "Wto3l/FakeRate/Run2016/2019-08-13/finalstate_eem/failIso_endcap_TTbar_WOZpeak/"
#out_path = "Wto3l/DataMCDistributions/Run2016/2019-08-06/FReemWOZpeak_SR_mmm/"
#out_path = "Wto3l/SR_MCDistributions/Run2016/2019-08-07/check_TT_DY/"
#out_path = "Wto3l/DataMCDistributions/Run2016/candidate_for_NN/WmTo3munu_ZpM15/"
out_path = "Wto3l/DataMCDistributions/Run2016/candidate_for_NN/TTJets/"


mZ1PlotRange = [40,40.,120.]
#mZ2PlotRange = [30,0.,60.]
#mZ2PlotRange = [60,0.,120.]
#h4lPlotRange = [100,0.,500.]
#h4lPlotRange = [20,100.,140.]
#deltaRPlotRange2 = [40,0.,4.]
#deltaRPlotRange = [40,0.,4.]
general_plots = []
#for eachCR in ["3p1f","2p2f"]:
    #if eachCR == "3p1f":
        #region_sel_str = "x.nZXCRFailedLeptons[0] == 1"
        #region_sel_str_whole = "x: x.nZXCRFailedLeptons[0] == 1"
    #else:
        #region_sel_str = "x.nZXCRFailedLeptons[0] == 2"
        #region_sel_str_whole = "x: x.nZXCRFailedLeptons[0] == 2"

general_plots.extend([
    #Plot("Z1_mass",         ["TH1D","Z1_mass","",]+mZ1PlotRange,        LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x:x.massZ1[0] > 0')      ), 
    #Plot("Lep1_pt",          ["TH1D","Lep1_pt","",40,0.,200.],           LambdaFunc('x:x.Lep1.Pt()'),          selFunc=LambdaFunc('x:x.Lep1.Pt() > 0')        ),
    #Plot("Lep2_pt",          ["TH1D","Lep2_pt","",40,0.,200.],           LambdaFunc('x:x.Lep2.Pt()'),          selFunc=LambdaFunc('x:x.Lep2.Pt() > 0')        ),
    #Plot("Lep3_pt",          ["TH1D","Lep3_pt","",40,0.,200.],           LambdaFunc('x:x.Lep3.Pt()'),          selFunc=LambdaFunc('x:x.Lep3.Pt() > 0')        ),
    #Plot("Lep3_pt",          ["TH1D","Lep3_pt","",200,0.,200.],           LambdaFunc('x:x.Lep3.Pt()'),          selFunc=LambdaFunc('x:x.Lep3.Pt > 0')        ),

    #Plot("Lep3_eta",          ["TH1D","Lep3_eta","",60,-3.,3.],           LambdaFunc('x:x.Lep3.Eta()'),          selFunc=LambdaFunc('x:x.Lep3.Eta()')        ),
    #Plot("3lep_pt",          ["TH1D","3lep_pt","",40,0.,200.],           LambdaFunc('x:x.pT3l[0]'),          selFunc=LambdaFunc('x:x.pT3l[0] > 0')        ),
    #Plot("Lep1+Lep2_pt",     ["TH1D","Lep1+Lep2_pt","",40,0.,200.],      LambdaFunc('x:x.twolpt'),        selFunc=LambdaFunc('x:x.twolpt > 0')      ),
    Plot("Z1_mass",          ["TH1D","Z1_mass","",80,0.,200.],           LambdaFunc('x:x.mass1'),          selFunc=LambdaFunc('x:x.mass1 > 0')        ),
    Plot("Z2_mass",          ["TH1D","Z2_mass","",80,0.,200.],           LambdaFunc('x:x.mass2'),          selFunc=LambdaFunc('x:x.mass2 > 0')        ),
    Plot("Z1combZ2_mass",          ["TH1D","Z1combZ2_mass","",80,0.,200.],         LambdaFunc('x:[x.mass1,x.mass2]'),     isCollection=True),

    #Plot("Zp_mass",          ["TH1D","Zp_mass","",80,0.,200.],           LambdaFunc('x:x.Zp_mass'),          selFunc=LambdaFunc('x:x.Zp_mass > 0')        ),
    #Plot("notZp_mass",          ["TH1D","notZp_mass","",80,0.,200.],           LambdaFunc('x:x.notZp_mass'),          selFunc=LambdaFunc('x:x.notZp_mass > 0')        ),
     #Plot("Transverse_Mass",          ["TH1D","Transverse_Mass","",100,0.,500.],           LambdaFunc('x:x.mt'),          selFunc=LambdaFunc('x:x.mt')        ),
     Plot("Z1_mass_vs_Z2_mass",   ["TH2D","Z1_mass_vs_Z2_mass","",80,0.,200.,80,0.,200.],   LambdaFunc('x:[x.mass1,x.mass2]'),   dim = 2 ),
     #Plot("Zp_mass_vs_notZp_mass",   ["TH2D","Zp_mass_vs_notZp_mass","",80,0.,200.,80,0.,200.],   LambdaFunc('x:[x.Zp_mass,x.notZp_mass]'),   dim = 2 ),
     #Plot("Zp_pt",          ["TH1D","Zp_pt","",80,0.,200.],           LambdaFunc('x:x.Zp_pt'),          selFunc=LambdaFunc('x:x.Zp_pt > 0')        ),
     #Plot("notZp_pt",          ["TH1D","notZp_pt","",80,0.,200.],           LambdaFunc('x:x.notZp_pt'),          selFunc=LambdaFunc('x:x.notZp_pt > 0')        ),
     Plot("M1_pt",          ["TH1D","M1_pt","",80,0.,200.],           LambdaFunc('x:x.mass1_pt'),          selFunc=LambdaFunc('x:x.mass1_pt > 0')        ),
     Plot("M2_pt",          ["TH1D","M2_pt","",80,0.,200.],           LambdaFunc('x:x.mass2_pt'),          selFunc=LambdaFunc('x:x.mass2_pt > 0')        ),
     Plot("Z1combZ2_pt",          ["TH1D","Z1combZ2_pt","",80,0.,200.],         LambdaFunc('x:[x.mass1_pt,x.mass2_pt]'),     isCollection=True),
     #Plot("Zp_eta",          ["TH1D","Zp_eta","",60,-3.,3.],           LambdaFunc('x:x.Zp_eta'),          selFunc=LambdaFunc('x:x.Zp_eta')        ),
     #Plot("notZp_eta",          ["TH1D","notZp_eta","",60,-3.,3.],           LambdaFunc('x:x.notZp_eta'),          selFunc=LambdaFunc('x:x.notZp_eta')        ),
     Plot("M1_eta",          ["TH1D","mass1_eta","",60,-3.,3.],           LambdaFunc('x:x.mass1_eta'),          selFunc=LambdaFunc('x:x.mass1_eta')        ),
     Plot("M2_eta",          ["TH1D","mass2_eta","",60,-3.,3.],           LambdaFunc('x:x.mass2_eta'),          selFunc=LambdaFunc('x:x.mass2_eta')        ),
     Plot("Z1combZ2_eta",          ["TH1D","Z1combZ2_eta","",60,-3.,3.],         LambdaFunc('x:[x.mass1_eta,x.mass2_eta]'),     isCollection=True),

     #Plot("Zp_phi",          ["TH1D","Zp_phi","",80,-4.,4.],           LambdaFunc('x:x.Zp_phi'),          selFunc=LambdaFunc('x:x.Zp_phi')        ),
     #Plot("notZp_phi",          ["TH1D","notZp_phi","",80,-4.,4.],           LambdaFunc('x:x.notZp_phi'),          selFunc=LambdaFunc('x:x.notZp_phi')        ),
     Plot("M1_phi",          ["TH1D","mass1_phi","",80,-4.,4.],           LambdaFunc('x:x.mass1_phi'),          selFunc=LambdaFunc('x:x.mass1_phi')        ),
     Plot("M2_phi",          ["TH1D","mass2_phi","",80,-4.,4.],           LambdaFunc('x:x.mass2_phi'),          selFunc=LambdaFunc('x:x.mass2_phi')        ),
     Plot("Z1combZ2_phi",          ["TH1D","Z1combZ2_phi","",80,-4.,4.],         LambdaFunc('x:[x.mass1_phi,x.mass2_phi]'),     isCollection=True),
     #Plot("Zp_lep_deltaR",          ["TH1D","Zp_lep_deltaR","",20,0.,5.],           LambdaFunc('x:x.Zp_lep_deltaR'),          selFunc=LambdaFunc('x:x.Zp_lep_deltaR')        ),
     #Plot("notZP_lep_deltaR",          ["TH1D","notZp_lep_deltaR","",20,0.,5.],           LambdaFunc('x:x.notZp_lep_deltaR'),          selFunc=LambdaFunc('x:x.notZp_lep_deltaR')        ),
     Plot("Z1_lep_deltaR",          ["TH1D","Z1_lep_deltaR","",20,0.,5.],           LambdaFunc('x:x.Z1_lep_deltaR'),          selFunc=LambdaFunc('x:x.Z1_lep_deltaR')        ),
     Plot("Z2_lep_deltaR",          ["TH1D","Z2_lep_deltaR","",20,0.,5.],           LambdaFunc('x:x.Z2_lep_deltaR'),          selFunc=LambdaFunc('x:x.Z2_lep_deltaR')        ),
     Plot("Z1combZ2_lep_deltaR",          ["TH1D","Z1combZ2_lep_deltaR","",20,0.,5.],         LambdaFunc('x:[x.Z1_lep_deltaR,x.Z2_lep_deltaR]'),     isCollection=True),
     #Plot("Lep_fromZp_pt",          ["TH1D","Lep_fromZp_pt","",80,0.,200.],         LambdaFunc('x:[x.Lep1_fromZp.Pt(),x.Lep2_fromZp.Pt()]'),     isCollection=True),
     #Plot("Lep_notZp_pt",          ["TH1D","Lep_notZp_pt","",80,0.,200.],           LambdaFunc('x:x.Lep1_notZp.Pt()'),          selFunc=LambdaFunc('x:x.Lep1_notZp.Pt()')        ),
     #Plot("deltaR_Zp_and_lepton",          ["TH1D","deltaR_Zp_and_lepton","",20,0.,5.],           LambdaFunc('x:x.Zp_lepnotfromZp_dR'),          selFunc=LambdaFunc('x:x.Zp_lepnotfromZp_dR')        ),
     #Plot("deltaR_notZp_and_lepton",          ["TH1D","deltaR_notZp_and_lepton","",20,0.,5.],           LambdaFunc('x:x.notZp_otherlep_dR'),          selFunc=LambdaFunc('x:x.notZp_otherlep_dR')        ),
     Plot("deltaR_M1_and_lepton",          ["TH1D","deltaR_M1_and_lepton","",20,0.,5.],           LambdaFunc('x:x.M1_lepnotfromM1_dR'),          selFunc=LambdaFunc('x:x.M1_lepnotfromM1_dR')        ),
     Plot("deltaR_M2_and_lepton",          ["TH1D","deltaR_M2_and_lepton","",20,0.,5.],           LambdaFunc('x:x.M2_lepnotfromM2_dR'),          selFunc=LambdaFunc('x:x.M2_lepnotfromM2_dR')        ),
     Plot("Z1combZ2_dR_Z1Z2_and_lepton",          ["TH1D","Z1combZ2_dR_Z1Z2_and_lepton","",20,0.,5.],         LambdaFunc('x:[x.M1_lepnotfromM1_dR,x.M2_lepnotfromM2_dR]'),     isCollection=True),
     #Plot("Lep_leading_fromZp_pt",          ["TH1D","Lep_leading_fromZp_pt","",80,0.,200.],           LambdaFunc('x:x.Lep_leading_fromZp.Pt()'),          selFunc=LambdaFunc('x:x.Lep_leading_fromZp.Pt()')        ),
     #Plot("Lep_subleading_fromZp_pt",          ["TH1D","Lep_subleading_fromZp_pt","",80,0.,200.],           LambdaFunc('x:x.Lep_subleading_fromZp.Pt()'),          selFunc=LambdaFunc('x:x.Lep_subleading_fromZp.Pt()')        ),
     #Plot("Lep_leading_notZp_pt",          ["TH1D","Lep_leading_notZp_pt","",80,0.,200.],           LambdaFunc('x:x.Lep_leading_notZp.Pt()'),          selFunc=LambdaFunc('x:x.Lep_leading_notZp.Pt()')        ),
     #Plot("Lep_subleading_notZp_pt",          ["TH1D","Lep_subleading_notZp_pt","",80,0.,200.],           LambdaFunc('x:x.Lep_subleading_notZp.Pt()'),          selFunc=LambdaFunc('x:x.Lep_subleading_notZp.Pt()')        ),
     Plot("Lep_leading_fromM1_pt",          ["TH1D","Lep_leading_fromM1_pt","",80,0.,200.],           LambdaFunc('x:x.Lep_leading_fromM1.Pt()'),          selFunc=LambdaFunc('x:x.Lep_leading_fromM1.Pt()')        ),
     Plot("Lep_leading_fromM2_pt",          ["TH1D","Lep_leading_fromM2_pt","",80,0.,200.],           LambdaFunc('x:x.Lep_leading_fromM2.Pt()'),          selFunc=LambdaFunc('x:x.Lep_leading_fromM2.Pt()')        ),
     Plot("Z1combZ2_Lep_leading_pt",          ["TH1D","Z1combZ2_Lep_leading_pt","",80,0.,200.],         LambdaFunc('x:[x.Lep_leading_fromM1.Pt(),x.Lep_leading_fromM2.Pt()]'),     isCollection=True),
     #Plot("deltaR_totalLep_and_thirdLep_Zp",          ["TH1D","deltaR_totalLep_and_thirdLep_Zp","",20,0.,5.],           LambdaFunc('x:x.totalLep_thirdLep_Zp_dR'),          selFunc=LambdaFunc('x:x.totalLep_thirdLep_Zp_dR')        ),
     #Plot("deltaR_totalLep_and_thirdLep_notZp",          ["TH1D","deltaR_totalLep_and_thirdLep_notZp","",20,0.,5.],           LambdaFunc('x:x.totalLep_thirdLep_notZp_dR'),          selFunc=LambdaFunc('x:x.totalLep_thirdLep_notZp_dR')        ),
     Plot("deltaR_totalLep_and_thirdLep_M1",          ["TH1D","deltaR_totalLep_and_thirdLep_M1","",20,0.,5.],           LambdaFunc('x:x.totalLep_thirdLep_M1_dR'),          selFunc=LambdaFunc('x:x.totalLep_thirdLep_M1_dR')        ),
     Plot("deltaR_totalLep_and_thirdLep_M2",          ["TH1D","deltaR_totalLep_and_thirdLep_M2","",20,0.,5.],           LambdaFunc('x:x.totalLep_thirdLep_M2_dR'),          selFunc=LambdaFunc('x:x.totalLep_thirdLep_M2_dR')        ),
     Plot("Z1combZ2_dR_totalLep_and_thirdLep",          ["TH1D","Z1combZ2_dR_totallep_and_thirdLep","",20,0.,5.],         LambdaFunc('x:[x.totalLep_thirdLep_M1_dR,x.totalLep_thirdLep_M2_dR]'),     isCollection=True),


        #Plot("Z2_mass_vs_DeltaR34_"+eachCR,["TH2D","Z2_mass_vs_DeltaR34_"+eachCR,"",]+mZ2PlotRange+deltaRPlotRange2,LambdaFunc('x: [x.massZ2[0],x.deltaRL34]'),selFunc=LambdaFunc(region_sel_str_whole),dim=2),
        #Plot("Z2_mass_"+eachCR,         ["TH1D","Z2_mass_"+eachCR,"",]+mZ2PlotRange,        LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc(region_sel_str_whole)      ),
        #Plot("Z1_4e_mass_"+eachCR,      ["TH1D","Z1_4e_mass_"+eachCR,"",]+mZ1PlotRange,     LambdaFunc('x: x.massZ1[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
        #Plot("Z2_4e_mass_"+eachCR,      ["TH1D","Z2_4e_mass_"+eachCR,"",]+mZ2PlotRange,     LambdaFunc('x: x.massZ2[0]'),       selFunc=LambdaFunc('x: x.mass4e[0] > 0 and '+region_sel_str)          ),
                      
        #Plot("met",             ["TH1D","met","",50,0.,250.],               LambdaFunc('x: x.met[0]'),          selFunc=LambdaFunc('x:x.met[0] > 0'),     ),
        #Plot("met_phi",             ["TH1D","met_phi","",40,-4.,4.],               LambdaFunc('x: x.met_phi[0]'),          selFunc=LambdaFunc('x:x.met_phi[0]'),     ),

        #Plot("IsoL3",             ["TH1D","IsoL3","",20,0.,1.],               LambdaFunc('x: x.IsoL3[0]'),          selFunc=LambdaFunc('x:x.IsoL3[0] > 0'),     ),
        #Plot("PDGIdL3",             ["TH1D","PDGIdL3","",80,-40,40],            LambdaFunc('x: x.PDG_IdL3[0]'),      selFunc=LambdaFunc('x:x.PDG_IdL3[0]'),       ),
        #Plot("MomIdL1",             ["TH1D","MomIdL1","",80,-40,40],            LambdaFunc('x: x.MomIdL1[0]'),      selFunc=LambdaFunc('x:x.MomIdL1[0]'),       ),
        #Plot("MomIdL2",             ["TH1D","MomIdL2","",80,-40,40],            LambdaFunc('x: x.MomIdL2[0]'),      selFunc=LambdaFunc('x:x.MomIdL2[0]'),       ),
        #Plot("MomIdL3",             ["TH1D","MomIdL3","",80,-40,40],            LambdaFunc('x: x.MomIdL3[0]'),      selFunc=LambdaFunc('x:x.MomIdL3[0]'),       ),
        #Plot("MomMomIdL3",             ["TH1D","MomMomIdL3","",80,-40,40],            LambdaFunc('x: x.MomMomIdL3[0]'),      selFunc=LambdaFunc('x:x.MomMomIdL3[0]'),       ),
        #Plot("MomMomIdL2",             ["TH1D","MomMomIdL2","",80,-40,40],            LambdaFunc('x: x.MomMomIdL2[0]'),      selFunc=LambdaFunc('x:x.MomMomIdL2[0]'),       ),
        #Plot("MomMomIdL1",             ["TH1D","MomMomIdL1","",80,-40,40],            LambdaFunc('x: x.MomMomIdL1[0]'),      selFunc=LambdaFunc('x:x.MomMomIdL1[0]'),       ),
        #Plot("nVtx",            ["TH1D","nVtx","",30,0.0,60.0],             LambdaFunc('x: x.nVtx[0]'),         selFunc=LambdaFunc(region_sel_str_whole),     ),
        #Plot("MinDeltaRL",      ["TH1D","MinDeltaRL","",]+deltaRPlotRange2,  LambdaFunc('x: x.minDeltaRL'),     selFunc=LambdaFunc(region_sel_str_whole),       ),
        ])

plots =  general_plots
#for plot in plots:
#    plot.plotSetting.divideByBinWidth = True

nCores                  = 2
outputDir               = "/raid/raid7/kshi/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,Data_Run2016,Data_sr_Run2016,WmTo3munu_ZpM45,WmTo3munu_ZpM15,WpTo3munu_ZpM45,WpTo3munu_ZpM15]#predCR]
#componentList           = [WZTo3LNu,Data_Run2016,WmTo3munu_ZpM45,WmTo3munu_ZpM15,WpTo3munu_ZpM45,WpTo3munu_ZpM15]
#componentList           = [WZTo3LNu,Data_Run2016,Data_sr_Run2016]
#componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,WmTo3munu_ZpM45,WmTo3munu_ZpM15,WpTo3munu_ZpM45,WpTo3munu_ZpM15]
#componentList           = [DYJetsToLL_M50,DYJetsToLL_M10To50,WZTo3LNu,TTJets,Data_sr_Run2016]
#componentList           = [DYJetsToLL_M50_memCR,DYJetsToLL_M10To50_memCR,TTJets_memCR,WZTo3LNu_memCR,Data_memCR_sr_Run2016]
#componentList           = [Data_memCR_sr_Run2016,Data_memCR_Run2016,WZTo3LNu_memCR]
#componentList           = [Data_memCR_sr_Run2016]
#componentList           = [Data_memCR_sr_Run2016,WZTo3LNu_memCR,DYJetsToLL_M50_memCR,DYJetsToLL_M10To50_memCR,TTJets_memCR]
#componentList           = [TTJets_fromT,TTJets_notfromT]
#componentList           = [TTJets_memCR]
#componentList           = [DYJetsToLL_M50_memCR]
#componentList           = [WmTo3munu_ZpM15,WpTo3munu_ZpM15]
#componentList           = [WZTo3LNu,Data_Run2016]
#componentList           = [WmTo3munu_ZpM15]
componentList           = [TTJets]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        #dataset.lumi = 41.4
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = Wto3l_sequence

sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/kshi/public_html/Zprime/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots))
