from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc
import array

# ________________________________________________________________________ ||
mZ1PlotRange        = [60-1,array.array('d',[40.*1.02**i for i in range(60)]),]
#mZ2PlotRange        = [180-1,array.array('d',[4.*1.02**i for i in range(180)]),]
#mZ2LowM4lPlotRange  = [140-1,array.array('d',[4.*1.02**i for i in range(140)]),]
#mZ2MidM4lPlotRange  = [140-1,array.array('d',[4.*1.02**i for i in range(140)]),]
#mZ2HighM4lPlotRange = [152-1,array.array('d',[4.*1.02**i for i in range(152)]),]
mZ2PlotRange        = [38,4.,80.,]
mZ2LowM4lPlotRange  = [28,4.,60.,]
mZ2MidM4lPlotRange  = [28,4.,60.,]
mZ2HighM4lPlotRange = [38,4.,80.,]
h4lPlotRange        = [47-1,array.array('d',[80.*1.02**i for i in range(47)]),]

sel_str         = "True"

# ________________________________________________________________________ ||
var_mZ1_str     = "x.massZ1[0]"
var_mZ2_str     = "x.massZ2[0]"
var_m4l_str     = "x.mass4l[0]"

low_m4l_str     = "x.mass4l[0] > 100 and x.mass4l[0] < 118"
mid_m4l_str     = "x.mass4l[0] > 118 and x.mass4l[0] < 130"
high_m4l_str    = "x.mass4l[0] > 130 and x.mass4l[0] < 170"

# ________________________________________________________________________ ||
general_plots = [
        Plot("mZ1",["TH1D","mZ1","",]+mZ1PlotRange, LambdaFunc('x: '+var_mZ1_str), selFunc=LambdaFunc('x: '+sel_str)),
        Plot("mZ2",["TH1D","mZ2","",]+mZ2PlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_str)),
        Plot("m4l",["TH1D","m4l","",]+h4lPlotRange, LambdaFunc('x: '+var_m4l_str), selFunc=LambdaFunc('x: '+sel_str)),

        Plot("mZ2_low-m4l",["TH1D","mZ2_low-m4l","",]+mZ2LowM4lPlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_str+' and '+low_m4l_str)),
        Plot("mZ2_mid-m4l",["TH1D","mZ2_mid-m4l","",]+mZ2MidM4lPlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_str+' and '+mid_m4l_str)),
        Plot("mZ2_high-m4l",["TH1D","mZ2_high-m4l","",]+mZ2HighM4lPlotRange, LambdaFunc('x: '+var_mZ2_str), selFunc=LambdaFunc('x: '+sel_str+' and '+high_m4l_str)),
        ]
