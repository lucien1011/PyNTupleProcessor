from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.mkdir_p import mkdir_p,copyFile

from HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_HToZdZd_m4l70 import * 
#from HToZdZd.Dataset.Run2016.SkimTree_DarkSUSY_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from HToZdZd.Config.MergeSampleDict import *

#____________________________________________________________________________________________________
# User Parameters
out_path                = "DarkPhotonSR/DataMCDistributions/RadiusCuts/SignifRadiusCut_mZdZDMASS/"
lumi                    = 35.9
nCores                  = 5
#outputDir               = "/raid/raid7/lucien/Higgs/HToZdZd/"+out_path
outputDir               = "/raid/raid7/rosedj1/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + [ HToZdZd_MZDZDMASS, ]
justEndSequence         = False

phpFile                 = "index.php"
region_sel_str_whole    = "x: True "
Z1vsZ2_radius           = "x: (x.massZ1[0]-ZDMASS)**2 + (x.massZ2[0]-ZDMASS)**2"

zdmass                  = float(ZDMASS) # zdmass is used for calculations (float), ZDMASS used for strings
radcut                  = RADIUSCUT
binwidth                = BINWIDTH
zoom                    = ZOOM
L                       = radcut + zoom
binwstr                 = str(binwidth).replace('.','p') # don't want unnecessary dots in file name
radcutstr               = str(radcut).replace('.','p') # don't want unnecessary dots in file name

mZ1PlotRange = [int(2*L/binwidth), zdmass-L, zdmass+L] # ensures that all plots have same binwidth
mZ2PlotRange = mZ1PlotRange
h4lPlotRange = [70,60.,200.]
#h4lPlotRange = [140,60.,200.]

#____________________________________________________________________________________________________
# Plots
signif_plots = [
        #Plot("Z1mass_vs_Z2massTEST",["TH2D","Z1mass_vs_Z2mass","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(region_sel_str_whole)),
        #Plot("Z1mass_vs_Z2mass_mZdZDMASS_finalstate=4e_radiuscut=RADIUSCUTGeV",["TH2D","Z1mass_vs_Z2mass_mZdZDMASS_finalstate=4e_radiuscut=RADIUSCUTGeV","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(Z1vsZ2_radius+'<'+str(radiuscut**2) and x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11)),
        Plot("Z1mass_vs_Z2mass_mZdZDMASS_fs4e_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV",["TH2D","Z1mass_vs_Z2mass_mZdZDMASS_fs4e_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(Z1vsZ2_radius+'<'+str(RADIUSCUT**2) +' and x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')),
        Plot("Z1mass_vs_Z2mass_mZdZDMASS_fs4mu_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV",["TH2D","Z1mass_vs_Z2mass_mZdZDMASS_fs4mu_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(Z1vsZ2_radius+'<'+str(RADIUSCUT**2) +' and x.mass4e[0] < 0 and x.mass4mu[0] > 0 and x.mass2e2mu[0] < 0')),
        Plot("Z1mass_vs_Z2mass_mZdZDMASS_fs2e2mu_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV",["TH2D","Z1mass_vs_Z2mass_mZdZDMASS_fs2e2mu_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(Z1vsZ2_radius+'<'+str(RADIUSCUT**2) +' and x.mass4e[0] < 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
        Plot("Z1mass_vs_Z2mass_mZdZDMASS_fs2mu2e_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV",["TH2D","Z1mass_vs_Z2mass_mZdZDMASS_fs2mu2e_rcut"+radcutstr+"GeV_binwid"+binwstr+"GeV","",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(Z1vsZ2_radius+'<'+str(RADIUSCUT**2) +' and x.mass4e[0] < 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
        ]

#signif_plots = []

#for cut in range(1,6):
#    cut = str(cut)
#    signif_plots.append(
#        Plot("Z1mass_vs_Z2mass_r=%sGeV"%cut,["TH2D","Z1mass_vs_Z2mass_r=%s"%cut,"",]+mZ1PlotRange+mZ2PlotRange, LambdaFunc('x: [x.massZ1[0],x.massZ2[0]]'), dim=2, selFunc=LambdaFunc(Z1vsZ2_radius+'<'+str(float(cut)**2)))
#            )

muon_plots = [
        ]

general_plots = [
        #Plot("Z1_mass",     ["TH1D","Z1_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'),       ),
        #Plot("Z2_mass",     ["TH1D","Z2_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'),       ),
        #Plot("Z1_4e_mass",     ["TH1D","Z1_4e_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')      ),
        #Plot("Z2_4e_mass",     ["TH1D","Z2_4e_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0')     ),
        #Plot("Z1_4mu_mass",     ["TH1D","Z1_4mu_mass","",]+mZ1PlotRange,  LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')      ),
        #Plot("Z2_4mu_mass",     ["TH1D","Z2_4mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0')     ),
        #Plot("Z1_2e2mu_mass",     ["TH1D","Z1_2e2mu_mass","",]+mZ1PlotRange,   LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')     ),
        #Plot("Z1_2mu2e_mass",     ["TH1D","Z1_2mu2e_mass","",]+mZ1PlotRange,   LambdaFunc('x: x.massZ1[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')     ),
        #Plot("Z2_2e2mu_mass",     ["TH1D","Z2_2e2mu_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')     ),
        #Plot("Z2_2mu2e_mass",     ["TH1D","Z2_2mu2e_mass","",]+mZ2PlotRange,   LambdaFunc('x: x.massZ2[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')     ),
        #      
        #Plot("h4L_mass",    ["TH1D","h4L_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4l[0]'),       ),
        #Plot("h4e_mass",    ["TH1D","h4e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4e[0]'), selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')       ),
        #Plot("h4mu_mass",   ["TH1D","h4mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass4mu[0]'), selFunc=LambdaFunc('x: x.mass4mu[0] > 0 and x.mass4e[0] < 0 and x.mass2e2mu[0] < 0')       ),
        #Plot("h2e2mu_mass", ["TH1D","h2e2mu_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')       ),
        #Plot("h2mu2e_mass", ["TH1D","h2mu2e_mass","",]+h4lPlotRange,   LambdaFunc('x: x.mass2e2mu[0]'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and x.mass4mu[0] < 0 and x.mass4e[0] < 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')       ),
        #Plot("h4L_Pt",      ["TH1D","h4L_Pt","",40,0.,200.],     LambdaFunc('x: x.pT4l[0]'),         ),
        #
        #Plot("mass_ratio",["TH1D","mass_ratio","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), ),
        #Plot("mass_ratio_4e",["TH1D","mass_ratio_4e","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass4e[0] > 0 and x.mass4mu[0] < 0 and x.mass2e2mu[0] < 0')),
        #Plot("mass_ratio_4mu",["TH1D","mass_ratio_4mu","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass4e[0] < 0 and x.mass4mu[0] > 0 and x.mass2e2mu[0] < 0')),
        #Plot("mass_ratio_2e2mu",["TH1D","mass_ratio_2e2mu","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13')),
        #Plot("mass_ratio_2mu2e",["TH1D","mass_ratio_2mu2e","",nBinsMassRatio,0.,1.], LambdaFunc('x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0])'), selFunc=LambdaFunc('x: x.mass2e2mu[0] > 0 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11')),
        ]

jet_plots = [
        #Plot("nJet",    ["TH1D","nJet","",5,-0.5,4.5],      LambdaFunc('x: x.njets_pt30_eta2p5[0]'),     ),
        ]

#____________________________________________________________________________________________________
#
plots = muon_plots + general_plots + jet_plots + signif_plots# big list of Plot objects
#for plot in plots:
    #plot.plotSetting.divideByBinWidth = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = darkphoton_signal_unblind_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution_radiuscut"+radcutstr+"GeV.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = "/home/rosedj1/public_html/Higgs/HToZdZd/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=True))

## Put an index.php file into Plots dir for easy visualization
copyFile('/home/rosedj1/',phpFile,endModuleOutputDir)
