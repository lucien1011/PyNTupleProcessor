from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

# ________________________________________________________________________ ||
mZ1PlotRange        = [80,0.,120.]
mZ2PlotRange        = [60,0.,60.]
h4lPlotRange        = [80,80.,160.]
anglePlotRange      = [50,-3.14,3.14]
cosThetaPlotRange   = [50,-1.,1.]

deltaRPlotRange3    = [40,0.,0.5]
deltaRPlotRange2    = [20,0.,2.]
deltaRPlotRange     = [40,0.,4.]
hPtPlotRange        = [40,0.,200.]

mu1PtPlotRange      = [20,0.,200.]
mu2PtPlotRange      = [20,0.,100.]
mu3PtPlotRange      = [20,0.,100.]
mu4PtPlotRange      = [20,0.,50.]

el1PtPlotRange      = [20,0.,200.]
el2PtPlotRange      = [20,0.,100.]
el3PtPlotRange      = [20,0.,100.]
el4PtPlotRange      = [20,0.,50.]

mu1EtaPlotRange     = [20,-3.,3.]
mu2EtaPlotRange     = [20,-3.,3.]
mu3EtaPlotRange     = [20,-3.,3.]
mu4EtaPlotRange     = [20,-3.,3.]

el1EtaPlotRange     = [20,-3.,3.]
el2EtaPlotRange     = [20,-3.,3.]
el3EtaPlotRange     = [20,-3.,3.]
el4EtaPlotRange     = [20,-3.,3.]

mu1EtaPlotRange     = [40,-5.,5.]

kfactorRange        =[100,1.0,1.2]

#deltaRPlotRange     =[100,0.,4.]

lepeffPlotRange     =[20,0,2]

nleptonRange        =[10,0,10]

# ________________________________________________________________________ ||
sel_4e_str      = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_2mu2e_str   = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_4mu_str     = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"
sel_2e2mu_str   = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"

var_mZ1_str             = "x.massZ1[0]"
var_mZ2_str             = "x.massZ2[0]"
var_m4l_str             = "x.mass4l[0]"
var_hPt_str             = "x.pT4l[0]"
var_cosThetaStar_str    = "x.cosThetaStar"
var_cosTheta1_str       = "x.cosTheta1"
var_cosTheta2_str       = "x.cosTheta2"
var_phi_str             = "x.phi"
var_phi1_str            = "x.phi1"

var_mu1Pt_str   = "[x.pTL1[0]] if abs(x.idL1[0]) == 13 else []"
var_mu2Pt_str   = "[x.pTL2[0]] if abs(x.idL2[0]) == 13 else []"
var_mu3Pt_str   = "[x.pTL3[0]] if abs(x.idL3[0]) == 13 else []"
var_mu4Pt_str   = "[x.pTL4[0]] if abs(x.idL4[0]) == 13 else []"
var_el1Pt_str   = "[x.pTL1[0]] if abs(x.idL1[0]) == 11 else []"
var_el2Pt_str   = "[x.pTL2[0]] if abs(x.idL2[0]) == 11 else []"
var_el3Pt_str   = "[x.pTL3[0]] if abs(x.idL3[0]) == 11 else []"
var_el4Pt_str   = "[x.pTL4[0]] if abs(x.idL4[0]) == 11 else []"

var_mu1Eta_str  = "[x.etaL1[0]] if abs(x.idL1[0]) == 13 else []"
var_mu2Eta_str  = "[x.etaL2[0]] if abs(x.idL2[0]) == 13 else []"
var_mu3Eta_str  = "[x.etaL3[0]] if abs(x.idL3[0]) == 13 else []"
var_mu4Eta_str  = "[x.etaL4[0]] if abs(x.idL4[0]) == 13 else []"
var_el1Eta_str  = "[x.etaL1[0]] if abs(x.idL1[0]) == 11 else []"
var_el2Eta_str  = "[x.etaL2[0]] if abs(x.idL2[0]) == 11 else []"
var_el3Eta_str  = "[x.etaL3[0]] if abs(x.idL3[0]) == 11 else []"
var_el4Eta_str  = "[x.etaL4[0]] if abs(x.idL4[0]) == 11 else []"

var_kfactor_str = "x.k_qqZZ_qcd_M[0]*x.k_qqZZ_ewk[0]"
var_kfactor_mZ2_str = "[x.k_qqZZ_qcd_M[0]*x.k_qqZZ_ewk[0],x.massZ2[0]]"
var_kfactor_mZ1_str = "[x.k_qqZZ_qcd_M[0]*x.k_qqZZ_ewk[0],x.massZ1[0]]"
var_kfactor_m4l_str = "[x.k_qqZZ_qcd_M[0]*x.k_qqZZ_ewk[0],x.mass4l[0]]"

var_deltaRL12_str  = "x.deltaRL12"
var_deltaRL34_str  = "x.deltaRL34"

var_lepeff_mZ2_str = "[x.lepeff,x.massZ2[0]]"

var_deltaRGENZpLep_str = "x.deltaRGENZpLep"
var_deltaRGENrecolep_str = "[x.deltaRGENrecolep[i] for i in range(0,len(x.deltaRGENrecolep))]"

var_numlepton_str = "[x.nGENlep,x.nRECOlep]"
var_numlepton_ZZprime_str = "[x.nGENlep_ZZprime,x.nRECOlep_ZZprime]"
# ________________________________________________________________________ ||
general_4mu_plots = [
        #Plot("mZ1_4mu",["TH1D","mZ1_4mu","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("mZ2_4mu",["TH1D","mZ2_4mu","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("m4l_4mu",["TH1D","m4l_4mu","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("hPt_4mu",["TH1D","hPt_4mu","",]+hPtPlotRange, LambdaFunc('x: '+var_hPt_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("cosThetaStar_4mu",["TH1D","cosThetaStar_4mu","",]+cosThetaPlotRange, LambdaFunc('x: '+var_cosThetaStar_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("cosTheta1_4mu",["TH1D","cosTheta1_4mu","",]+cosThetaPlotRange, LambdaFunc('x: '+var_cosTheta1_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("cosTheta2_4mu",["TH1D","cosTheta2_4mu","",]+cosThetaPlotRange, LambdaFunc('x: '+var_cosTheta2_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("phi_4mu",["TH1D","phi_4mu","",]+anglePlotRange, LambdaFunc('x: '+var_phi_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("phi1_4mu",["TH1D","phi1_4mu","",]+anglePlotRange, LambdaFunc('x: '+var_phi1_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        
        #Plot("thetaZ1_4mu",["TH1D","thetaZ1_4mu","",]+hPtPlotRange, LambdaFunc('x: '+var_thetaZ1_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),

        #Plot("mu1Pt_4mu", ["TH1D","mu1Pt_4mu","",]+mu1PtPlotRange, LambdaFunc('x: '+var_mu1Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("mu2Pt_4mu", ["TH1D","mu2Pt_4mu","",]+mu2PtPlotRange, LambdaFunc('x: '+var_mu2Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("mu3Pt_4mu", ["TH1D","mu3Pt_4mu","",]+mu3PtPlotRange, LambdaFunc('x: '+var_mu3Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("mu4Pt_4mu", ["TH1D","mu4Pt_4mu","",]+mu4PtPlotRange, LambdaFunc('x: '+var_mu4Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        
        #Plot("mu1Eta_4mu", ["TH1D","mu1Eta_4mu","",]+mu1EtaPlotRange, LambdaFunc('x: '+var_mu1Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("mu2Eta_4mu", ["TH1D","mu2Eta_4mu","",]+mu2EtaPlotRange, LambdaFunc('x: '+var_mu2Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("mu3Eta_4mu", ["TH1D","mu3Eta_4mu","",]+mu3EtaPlotRange, LambdaFunc('x: '+var_mu3Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("mu4Eta_4mu", ["TH1D","mu4Eta_4mu","",]+mu4EtaPlotRange, LambdaFunc('x: '+var_mu4Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),

        #Plot("k-factor", ["TH1D","k-factor","",]+kfactorRange, LambdaFunc('x: '+var_kfactor_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("k-factor_vs_mZ2", ["TH2D","k-factor_vs_mZ2","",]+kfactorRange+mZ2PlotRange, LambdaFunc('x: '+var_kfactor_mZ2_str), dim = 2, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("k-factor_vs_mZ1", ["TH2D","k-factor_vs_mZ1","",]+kfactorRange+mZ1PlotRange, LambdaFunc('x: '+var_kfactor_mZ1_str), dim = 2, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("k-factor_vs_m4l", ["TH2D","k-factor_vs_m4l","",]+kfactorRange+h4lPlotRange, LambdaFunc('x: '+var_kfactor_m4l_str), dim = 2, selFunc=LambdaFunc('x: '+sel_4mu_str)),

        #Plot("deltaRL12", ["TH1D","deltaRL12","",]+deltaRPlotRange, LambdaFunc('x: '+var_deltaRL12_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("deltaRL34", ["TH1D","deltaRL34","",]+deltaRPlotRange, LambdaFunc('x: '+var_deltaRL34_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        
        #Plot("lepeff_vs_mZ2", ["TH2D","lepeff_vs_mZ2","",]+lepeffPlotRange+mZ2PlotRange, LambdaFunc('x: '+var_lepeff_mZ2_str), dim = 2, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("deltaRGENZpLep", ["TH1D","deltaRGENZpLep","",]+deltaRPlotRange2, LambdaFunc('x: '+var_deltaRGENZpLep_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("deltaRGENrecolep", ["TH1D","deltaRGENrecolep","",]+deltaRPlotRange3, LambdaFunc('x: '+var_deltaRGENrecolep_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        #Plot("nGENlep_nRECOlep", ["TH2D","nGENlep_nRECOlep","","text"]+nleptonRange+nleptonRange, LambdaFunc('x: '+var_numlepton_str), dim = 2),
        #Plot("nGENlep_nRECOlep_ZZprime", ["TH2D","nGENlep_nRECOlep_ZZprime","","text"]+nleptonRange+nleptonRange, LambdaFunc('x: '+var_numlepton_ZZprime_str), dim = 2),
        ]
