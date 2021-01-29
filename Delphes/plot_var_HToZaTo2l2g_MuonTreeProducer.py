from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Delphes.Dataset.HToZaTo2l2g.MuonTreeProducer import * 

from Plotter.Plotter import Plotter
from Plotter.Plot import Plot
from Plotter.PlotEndModule import PlotEndModule

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

lumi                    = 1.
nCores                  = 1
outputDir               = "/Users/lucien/CMS/HEP-ML-Tools/Delphes/Plot/2020-06-10/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [HToZaTo2l2g_M1,]
justEndSequence         = False


plots             = [
        Plot("Muon_Pt",["TH1D","Muon_Pt","",20,0.,100.],LambdaFunc("x: x.Muon_Pt[0]"),selFunc=LambdaFunc("x: len(x.Muon_Pt) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_Eta",["TH1D","Muon_Eta","",20,-3.,3.],LambdaFunc("x: x.Muon_Eta[0]"),selFunc=LambdaFunc("x: len(x.Muon_Pt) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_Phi",["TH1D","Muon_Phi","",20,-3.,3.],LambdaFunc("x: x.Muon_Phi[0]"),selFunc=LambdaFunc("x: len(x.Muon_Pt) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_T",["TH1D","Muon_T","",20,0.,100.],LambdaFunc("x: x.Muon_T[0]*1E-0"),selFunc=LambdaFunc("x: len(x.Muon_T) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_Isolation",["TH1D","Muon_Isolation","",20,0.,0.5],LambdaFunc("x: x.Muon_IsolationVar[0]"),selFunc=LambdaFunc("x: len(x.Muon_IsolationVar) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_TrackD0",["TH1D","Muon_TrackD0","",20,-1.,1.],LambdaFunc("x: x.Muon_TrackD0[0]"),selFunc=LambdaFunc("x: len(x.Muon_TrackD0) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_TrackDZ",["TH1D","Muon_TrackDZ","",20,-100.,100.],LambdaFunc("x: x.Muon_TrackDZ[0]"),selFunc=LambdaFunc("x: len(x.Muon_TrackDZ) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_TrackVx",["TH1D","Muon_TrackVx","",20,-0.3,-0.2],LambdaFunc("x: x.Muon_TrackVx[0]"),selFunc=LambdaFunc("x: len(x.Muon_TrackVx) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_TrackVy",["TH1D","Muon_TrackVy","",20,0.66,0.72],LambdaFunc("x: x.Muon_TrackVy[0]"),selFunc=LambdaFunc("x: len(x.Muon_TrackVy) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_TrackVz",["TH1D","Muon_TrackVz","",20,-100,100.],LambdaFunc("x: x.Muon_TrackVz[0]"),selFunc=LambdaFunc("x: len(x.Muon_TrackVz) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_GenPt",["TH1D","Muon_GenPt","",20,0.,100.],LambdaFunc("x: x.Muon_GenPt[0]"),selFunc=LambdaFunc("x: len(x.Muon_GenPt) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_GenEta",["TH1D","Muon_GenEta","",20,-3.,3.],LambdaFunc("x: x.Muon_GenEta[0]"),selFunc=LambdaFunc("x: len(x.Muon_GenPt) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_GenPhi",["TH1D","Muon_GenPhi","",20,-3.,3.],LambdaFunc("x: x.Muon_GenPhi[0]"),selFunc=LambdaFunc("x: len(x.Muon_GenPt) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        Plot("Muon_GenCharge",["TH1D","Muon_GenCharge","",3,-1.5,1.5,],LambdaFunc("x: x.Muon_GenCharge[0]"),selFunc=LambdaFunc("x: len(x.Muon_GenCharge) > 0"),getEventWeight=LambdaFunc("x: 1."),),
        ]

sequence                = Sequence() 
plotter                 = Plotter("Plotter",plots)
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence             = EndSequence()
endSequence.add(PlotEndModule(outputDir,plots,skipSF=False))
