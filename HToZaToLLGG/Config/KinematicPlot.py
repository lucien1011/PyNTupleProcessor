from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

# ____________________________________________________________________________________________________________________________________________ ||
mllPlotRange    = [50,0.,200.]
mggPlotRange    = [50,0.,200.]
mllggPlotRange  = [50,0.,200.]
elPtPlotRange   = [20,0.,200.]
muPtPlotRange   = [20,0.,200.]
phoPtPlotRange  = [20,0.,200.]
elEtaPlotRange  = [20,-3.,3.]
muEtaPlotRange  = [20,-3.,3.]
phoEtaPlotRange = [20,-3.,3.]

# ____________________________________________________________________________________________________________________________________________ ||
general_plots = [
        Plot("mllgg",["TH1D","mllgg","",]+mllggPlotRange, LambdaFunc('x: (x.Zcand.lep1P4+x.Zcand.lep2P4+x.selPhotons[0].p4()+x.selPhotons[1].p4()).M()'),),
        ]

# ____________________________________________________________________________________________________________________________________________ ||
lepton_plots = [
        #Plot("mll",["TH1D","mll","",]+mllPlotRange, LambdaFunc('x: (x.selElectrons[0].p4()+x.selElectrons[1].p4()).M()'),),
        Plot("mll",["TH1D","mll","",]+mllPlotRange, LambdaFunc('x: x.Zcand.m'),),
        Plot("el_pt",["TH1D","el_pt","",]+elPtPlotRange, LambdaFunc('x: [x.pt for x in x.selElectrons]'),isCollection=True,),
        Plot("mu_pt",["TH1D","mu_pt","",]+muPtPlotRange, LambdaFunc('x: [x.pt for x in x.selMuons]'),isCollection=True,),
        Plot("mu_eta",["TH1D","mu_eta","",]+muEtaPlotRange, LambdaFunc('x: [x.eta for x in x.selMuons]'),isCollection=True,),
        Plot("el_eta",["TH1D","el_eta","",]+elEtaPlotRange, LambdaFunc('x: [x.eta for x in x.selElectrons]'),isCollection=True,),
        ]

# ____________________________________________________________________________________________________________________________________________ ||
photon_plots = [
        Plot("mgg",["TH1D","mgg","",]+mggPlotRange, LambdaFunc('x: (x.selPhotons[0].p4()+x.selPhotons[1].p4()).M()'),),
        Plot("pho_pt",["TH1D","pho_pt","",]+phoPtPlotRange, LambdaFunc('x: [x.pt for x in x.selPhotons]'),isCollection=True,),
        Plot("pho_eta",["TH1D","pho_eta","",]+phoEtaPlotRange, LambdaFunc('x: [x.eta for x in x.selPhotons]'),isCollection=True,),
        ]
