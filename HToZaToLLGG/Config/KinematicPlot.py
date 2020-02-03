from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

# ____________________________________________________________________________________________________________________________________________ ||
mllPlotRange = [50,0.,200.]
mggPlotRange = [50,0.,200.]
mllggPlotRange = [50,0.,200.]

# ____________________________________________________________________________________________________________________________________________ ||
general_plots = [
        Plot("mllgg",["TH1D","mllgg","",]+mllggPlotRange, LambdaFunc('x: (x.selElectrons[0].p4()+x.selElectrons[1].p4()+x.selPhotons[0].p4()+x.selPhotons[1].p4()).M()'),),
        ]

# ____________________________________________________________________________________________________________________________________________ ||
electron_plots = [
        Plot("mll",["TH1D","mll","",]+mllPlotRange, LambdaFunc('x: (x.selElectrons[0].p4()+x.selElectrons[1].p4()).M()'),),
        ]

# ____________________________________________________________________________________________________________________________________________ ||
photon_plots = [
        Plot("mgg",["TH1D","mgg","",]+mggPlotRange, LambdaFunc('x: (x.selPhotons[0].p4()+x.selPhotons[1].p4()).M()'),),
        ]
