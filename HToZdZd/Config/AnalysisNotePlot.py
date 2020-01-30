from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc
import array

# ________________________________________________________________________ ||
mZ1PlotRange_el         = [58-1,array.array('d',[4.*1.05**i for i in range(58)]),]
mZ1PlotRange_mu         = [141-1,array.array('d',[4.*1.02**i for i in range(141)]),]

mZ2PlotRange_el         = [58-1,array.array('d',[4.*1.05**i for i in range(58)]),]
mZ2PlotRange_mu         = [141-1,array.array('d',[4.*1.02**i for i in range(141)]),]

h4lPlotRange_mu         = [33-1,array.array('d',[90.*1.02**i for i in range(33)]),]
h4lPlotRange_el         = [13-1,array.array('d',[90.*1.02**i for i in range(13)]),]

# ________________________________________________________________________ ||
sel_4e_str      = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_2mu2e_str   = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"
sel_4mu_str     = "abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"
sel_2e2mu_str   = "abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"
sel_mu_str      = "abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13"
sel_el_str      = "abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11"

var_mZ1_str     = "x.massZ1[0]"
var_mZ2_str     = "x.massZ2[0]"
var_m4l_str     = "x.mass4l[0]"

# ________________________________________________________________________ ||
general_4e_plots = [
        Plot("mZ1_4e",["TH1D","mZ1_4e","",]+mZ1PlotRange_el, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("mZ2_4e",["TH1D","mZ2_4e","",]+mZ2PlotRange_el, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("m4l_4e",["TH1D","m4l_4e","",]+h4lPlotRange_el, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_4e_str)),
        Plot("mZ1mZ2_4e",["TH2D","mZ1mZ2_4e","",]+mZ1PlotRange_el+mZ2PlotRange_el, LambdaFunc('x: ['+var_mZ1_str+','+var_mZ2_str+']'), selFunc=LambdaFunc('x: '+sel_4e_str),dim=2),
        ]

general_2mu2e_plots = [
        Plot("mZ1_2mu2e",["TH1D","mZ1_2mu2e","",]+mZ1PlotRange_el, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("mZ2_2mu2e",["TH1D","mZ2_2mu2e","",]+mZ2PlotRange_el, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("m4l_2mu2e",["TH1D","m4l_2mu2e","",]+h4lPlotRange_el, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_2mu2e_str)),
        Plot("mZ1mZ2_2mu2e",["TH2D","mZ1mZ2_2mu2e","",]+mZ1PlotRange_mu+mZ2PlotRange_el, LambdaFunc('x: ['+var_mZ1_str+','+var_mZ2_str+']'), selFunc=LambdaFunc('x: '+sel_2mu2e_str),dim=2),
        ]

general_4mu_plots = [
        Plot("mZ1_4mu",["TH1D","mZ1_4mu","",]+mZ1PlotRange_mu, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mZ2_4mu",["TH1D","mZ2_4mu","",]+mZ2PlotRange_mu, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("m4l_4mu",["TH1D","m4l_4mu","",]+h4lPlotRange_mu, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_4mu_str)),
        Plot("mZ1mZ2_4mu",["TH2D","mZ1mZ2_4mu","",]+mZ1PlotRange_mu+mZ2PlotRange_mu, LambdaFunc('x: ['+var_mZ1_str+','+var_mZ2_str+']'), selFunc=LambdaFunc('x: '+sel_4mu_str),dim=2),
        ]

general_2e2mu_plots = [
        Plot("mZ1_2e2mu",["TH1D","mZ1_2e2mu","",]+mZ1PlotRange_mu, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("mZ2_2e2mu",["TH1D","mZ2_2e2mu","",]+mZ2PlotRange_mu, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),
        Plot("m4l_2e2mu",["TH1D","m4l_2e2mu","",]+h4lPlotRange_mu, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_2e2mu_str)),    
        Plot("mZ1mZ2_2e2mu",["TH2D","mZ1mZ2_2e2mu","",]+mZ1PlotRange_el+mZ2PlotRange_mu, LambdaFunc('x: ['+var_mZ1_str+','+var_mZ2_str+']'), selFunc=LambdaFunc('x: '+sel_2e2mu_str),dim=2),
        ]

general_mu_plots = [
        Plot("mZ1_mu",["TH1D","mZ1_mu","",]+mZ1PlotRange_mu, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_mu_str)),
        Plot("mZ2_mu",["TH1D","mZ2_mu","",]+mZ2PlotRange_mu, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_mu_str)),
        Plot("m4l_mu",["TH1D","m4l_mu","",]+h4lPlotRange_mu, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_mu_str)),    
        ]

general_el_plots = [
        Plot("mZ1_el",["TH1D","mZ1_el","",]+mZ1PlotRange_el, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_el_str)),
        Plot("mZ2_el",["TH1D","mZ2_el","",]+mZ2PlotRange_el, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_el_str)),
        Plot("m4l_el",["TH1D","m4l_el","",]+h4lPlotRange_el, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_el_str)),    
        ]

general_plots = general_4mu_plots + general_4e_plots + general_2e2mu_plots + general_2mu2e_plots + general_mu_plots + general_el_plots 
