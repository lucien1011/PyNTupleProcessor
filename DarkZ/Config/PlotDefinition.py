from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

# ________________________________________________________________________ ||
mZ1PlotRange        = [40,40.,120.]
mZ2PlotRange        = [30,0.,60.]
h4lPlotRange        = [20,100.,140.]
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

# ________________________________________________________________________ ||
sel_4e_str      = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_2mu2e_str   = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_4mu_str     = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"
sel_2e2mu_str   = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"

var_mZ1_str     = "x.massZ1[0]"
var_mZ2_str     = "x.massZ2[0]"
var_m4l_str     = "x.mass4l[0]"
var_hPt_str     = "x.pT4l[0]"

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

# ________________________________________________________________________ ||
general_4e_plots = [
        Plot("mZ1_4e",["TH1D","mZ1_4e","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("mZ2_4e",["TH1D","mZ2_4e","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("m4l_4e",["TH1D","m4l_4e","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("hPt_4e",["TH1D","hPt_4e","",]+hPtPlotRange, LambdaFunc('x: '+var_hPt_str), selFunc=LambdaFunc('x: '+sel_4e_str)),

        Plot("el1Pt_4e", ["TH1D","el1Pt_4e","",]+el1PtPlotRange, LambdaFunc('x: '+var_el1Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("el2Pt_4e", ["TH1D","el2Pt_4e","",]+el2PtPlotRange, LambdaFunc('x: '+var_el2Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("el3Pt_4e", ["TH1D","el3Pt_4e","",]+el3PtPlotRange, LambdaFunc('x: '+var_el3Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("el4Pt_4e", ["TH1D","el4Pt_4e","",]+el4PtPlotRange, LambdaFunc('x: '+var_el4Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),

        Plot("el1Eta_4e", ["TH1D","el1Eta_4e","",]+el1EtaPlotRange, LambdaFunc('x: '+var_el1Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("el2Eta_4e", ["TH1D","el2Eta_4e","",]+el2EtaPlotRange, LambdaFunc('x: '+var_el2Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("el3Eta_4e", ["TH1D","el3Eta_4e","",]+el3EtaPlotRange, LambdaFunc('x: '+var_el3Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("el4Eta_4e", ["TH1D","el4Eta_4e","",]+el4EtaPlotRange, LambdaFunc('x: '+var_el4Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4e_str)),
        ]

general_2mu2e_plots = [
        Plot("mZ1_2mu2e",["TH1D","mZ1_2mu2e","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("mZ2_2mu2e",["TH1D","mZ2_2mu2e","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("m4l_2mu2e",["TH1D","m4l_2mu2e","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("hPt_2mu2e",["TH1D","hPt_2mu2e","",]+hPtPlotRange, LambdaFunc('x: '+var_hPt_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("mu1Pt_2mu2e", ["TH1D","mu1Pt_2mu2e","",]+mu1PtPlotRange, LambdaFunc('x: '+var_mu1Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("mu2Pt_2mu2e", ["TH1D","mu2Pt_2mu2e","",]+mu2PtPlotRange, LambdaFunc('x: '+var_mu2Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("el3Pt_2mu2e", ["TH1D","el3Pt_2mu2e","",]+el3PtPlotRange, LambdaFunc('x: '+var_el3Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("el4Pt_2mu2e", ["TH1D","el4Pt_2mu2e","",]+el4PtPlotRange, LambdaFunc('x: '+var_el4Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        
        Plot("mu1Eta_2mu2e", ["TH1D","mu1Eta_2mu2e","",]+mu1EtaPlotRange, LambdaFunc('x: '+var_mu1Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("mu2Eta_2mu2e", ["TH1D","mu2Eta_2mu2e","",]+mu2EtaPlotRange, LambdaFunc('x: '+var_mu2Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("el3Eta_2mu2e", ["TH1D","el3Eta_2mu2e","",]+el3EtaPlotRange, LambdaFunc('x: '+var_el3Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("el4Eta_2mu2e", ["TH1D","el4Eta_2mu2e","",]+el4EtaPlotRange, LambdaFunc('x: '+var_el4Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        ]

general_4mu_plots = [
        Plot("mZ1_4mu",["TH1D","mZ1_4mu","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mZ2_4mu",["TH1D","mZ2_4mu","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("m4l_4mu",["TH1D","m4l_4mu","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("hPt_4mu",["TH1D","hPt_4mu","",]+hPtPlotRange, LambdaFunc('x: '+var_hPt_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mu1Pt_4mu", ["TH1D","mu1Pt_4mu","",]+mu1PtPlotRange, LambdaFunc('x: '+var_mu1Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mu2Pt_4mu", ["TH1D","mu2Pt_4mu","",]+mu2PtPlotRange, LambdaFunc('x: '+var_mu2Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mu3Pt_4mu", ["TH1D","mu3Pt_4mu","",]+mu3PtPlotRange, LambdaFunc('x: '+var_mu3Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mu4Pt_4mu", ["TH1D","mu4Pt_4mu","",]+mu4PtPlotRange, LambdaFunc('x: '+var_mu4Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        
        Plot("mu1Eta_4mu", ["TH1D","mu1Eta_4mu","",]+mu1EtaPlotRange, LambdaFunc('x: '+var_mu1Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mu2Eta_4mu", ["TH1D","mu2Eta_4mu","",]+mu2EtaPlotRange, LambdaFunc('x: '+var_mu2Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mu3Eta_4mu", ["TH1D","mu3Eta_4mu","",]+mu3EtaPlotRange, LambdaFunc('x: '+var_mu3Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mu4Eta_4mu", ["TH1D","mu4Eta_4mu","",]+mu4EtaPlotRange, LambdaFunc('x: '+var_mu4Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_4mu_str)),
        ]

general_2e2mu_plots = [
        Plot("mZ1_2e2mu",["TH1D","mZ1_2e2mu","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("mZ2_2e2mu",["TH1D","mZ2_2e2mu","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("m4l_2e2mu",["TH1D","m4l_2e2mu","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("hPt_2e2mu",["TH1D","hPt_2e2mu","",]+hPtPlotRange, LambdaFunc('x: '+var_hPt_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),

        Plot("mu3Pt_2e2mu", ["TH1D","mu3Pt_2e2mu","",]+mu3PtPlotRange, LambdaFunc('x: '+var_mu3Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("mu4Pt_2e2mu", ["TH1D","mu4Pt_2e2mu","",]+mu4PtPlotRange, LambdaFunc('x: '+var_mu4Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("el1Pt_2e2mu", ["TH1D","el1Pt_2e2mu","",]+el1PtPlotRange, LambdaFunc('x: '+var_el1Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("el2Pt_2e2mu", ["TH1D","el2Pt_2e2mu","",]+el2PtPlotRange, LambdaFunc('x: '+var_el2Pt_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),

        Plot("mu3Eta_2e2mu", ["TH1D","mu3Eta_2e2mu","",]+mu3EtaPlotRange, LambdaFunc('x: '+var_mu3Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("mu4Eta_2e2mu", ["TH1D","mu4Eta_2e2mu","",]+mu4EtaPlotRange, LambdaFunc('x: '+var_mu4Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("el1Eta_2e2mu", ["TH1D","el1Eta_2e2mu","",]+el1EtaPlotRange, LambdaFunc('x: '+var_el1Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("el2Eta_2e2mu", ["TH1D","el2Eta_2e2mu","",]+el2EtaPlotRange, LambdaFunc('x: '+var_el2Eta_str), isCollection=True, selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        ]
