from Core.BaseObject import BaseObject
from Plotter.Plot import Plot
from Core.Utils.LambdaFunc import LambdaFunc

single_plot_cfgs = [
        BaseObject("pt",plot_range=[20,0.,200.],),
        BaseObject("eta",plot_range=[20,-3.,3.],),
        BaseObject("phi",plot_range=[20,-3.5,3.5],),
        BaseObject("numberOfChambers",plot_range=[21,-0.5,20.5],),
        BaseObject("numberOfSegments",plot_range=[11,-0.5,10.5],),
        BaseObject("numberOfMatches",plot_range=[11,-0.5,10.5],),
        BaseObject("calEnergyEm",plot_range=[20,0.,25.],),
        BaseObject("calEnergyHad",plot_range=[20,0.,25.],),
        BaseObject("charge",plot_range=[3,-1.5,1.5],),
        BaseObject("energy",plot_range=[20,0.,1000.],),
        BaseObject("theta",plot_range=[20,0.,3.],),
        BaseObject("vx",plot_range=[50,0.,0.2],),
        BaseObject("vy",plot_range=[50,-0.1,0.0],),
        BaseObject("vz",plot_range=[20,-10.,10.],),
        BaseObject("dz",plot_range=[50,-0.1,0.1],),
        BaseObject("dxy",plot_range=[50,-0.1,0.1],),
        BaseObject("nRecHits",plot_range=[50,-0.5,49.5],),
        ]
vector_plot_cfgs = [
        BaseObject("cscSegmentRecord_nRecHits",plot_range=[10,-0.5,9.5],),
        BaseObject("cscSegmentRecord_ring",plot_range=[10,-0.5,9.5],),
        BaseObject("cscSegmentRecord_station",plot_range=[10,-0.5,9.5],),
        BaseObject("cscSegmentRecord_chamber",plot_range=[50,-0.5,49.5],),
        BaseObject("cscSegmentRecord_endcap",plot_range=[2,0.5,2.5],),
        BaseObject("cscSegmentRecord_localX",plot_range=[200,-100.,100.],),
        BaseObject("cscSegmentRecord_localY",plot_range=[200,-200.,200.],),
        ]

plots = [
        Plot("Muon_"+p.name,["TH1D","Muon_"+p.name,"",]+p.plot_range,LambdaFunc("x: [m."+p.name+" for m in x.standAloneMuons]"),isCollection=True) for p in single_plot_cfgs
        ] + [
        Plot("Muon_"+p.name,["TH1D","Muon_"+p.name,"",]+p.plot_range,LambdaFunc("x: [n for m in x.standAloneMuons for n in m."+p.name+"]"),isCollection=True) for p in vector_plot_cfgs
        ]
