from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

import ROOT

# ________________________________________________________________________ ||
var_muPt_str        = "[l.pt for l in x.leptons_matched]"
var_muEta_str       = "[l.eta for l in x.leptons_matched]"
var_muMass_str      = "(x.leptons_matched[0].p4()+x.leptons_matched[1].p4()).M()"

muPtPlotRange       = [50,0.,50.]
muEtaPlotRange      = [60,-3.,3.]
muMassPlotRange     = [90,0.,90.]

# ________________________________________________________________________ ||
plots = [
        Plot("mu_pt",["TH1D","mu_pt","",]+muPtPlotRange,LambdaFunc("x: "+var_muPt_str),isCollection=True),
        Plot("mu_eta",["TH1D","mu_eta","",]+muEtaPlotRange,LambdaFunc("x: "+var_muEta_str),isCollection=True),
        Plot("mu_mass",["TH1D","mu_mass","",]+muMassPlotRange,LambdaFunc("x: "+var_muMass_str),selFunc=LambdaFunc("x: len(x.leptons_matched) >= 2")),
        ]

# ________________________________________________________________________ ||
sampleColorDict     = {
        5: ROOT.kViolet,
        10: ROOT.kBlue,
        20: ROOT.kGreen,
        30: ROOT.kOrange,
        40: ROOT.kRed,
        50: ROOT.kRed+4,
        60: ROOT.kBlack,
        }
