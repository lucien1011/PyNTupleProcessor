from RPV.Analyzer.Plotter.Plot import Plot
from Utils.LambdaFunc import LambdaFunc

eventBasedPlots = [
        Plot("nJet40",      ["TH1D","nJet40","",20,-0.5,19.5],      LambdaFunc('x: len([j for j in x.LooseJets if j.pt > 40])')),
        Plot("nBJet25",     ["TH1D","nBJet25","",10,-0.5,9.5],      LambdaFunc('x: len([j for j in x.LooseJets if j.btagCSVV2 > 0.8989])')),
        Plot("ht40",        ["TH1D","ht40","",60,0.,6000.],         LambdaFunc('x: sum([j.pt for j in x.LooseJets if j.pt > 40])')),
        Plot("met",         ["TH1D","met","",60,0.,6000.],          LambdaFunc('x: x.MET_pt[0]')),
        Plot("nMediumMuon", ["TH1D","nMedMuon","",10,-0.5,9.5],     LambdaFunc('x: len(x.MediumMuons)')),
        Plot("nMediumElectron", ["TH1D","nMedElectron","",10,-0.5,9.5],     LambdaFunc('x: len(x.MediumElectrons)')),
        ]

muonPlots = [
        Plot("MedMuonPt",   ["TH1D","MedMuonPt","",20,0.,1000.],    LambdaFunc('x: [mu.pt for mu in x.MediumMuons]'), isCollection=True),
        Plot("MedMuonEta",  ["TH1D","MedMuonEta","",20,-3.,3.],     LambdaFunc('x: [mu.eta for mu in x.MediumMuons]'), isCollection=True),
        Plot("MedMuonDxy",  ["TH1D","MedMuonDxy","",20,0.,0.01],     LambdaFunc('x: [mu.dxy for mu in x.MediumMuons]'), isCollection=True),
        Plot("MedMuonDz",   ["TH1D","MedMuonDz","",20,0.,0.1],      LambdaFunc('x: [mu.dz for mu in x.MediumMuons]'), isCollection=True),
        Plot("MedMuonSip",  ["TH1D","MedMuonSip","",20,0.,8],     LambdaFunc('x: [mu.sip3d for mu in x.MediumMuons]'), isCollection=True),
        ]

electronPlots = [
        Plot("MedElectronPt",   ["TH1D","MedElectronPt","",20,0.,1000.],    LambdaFunc('x: [ele.pt for ele in x.MediumElectrons]'), isCollection=True),
        Plot("MedElectronEta",  ["TH1D","MedElectronEta","",20,-3.,3.],     LambdaFunc('x: [ele.eta for ele in x.MediumElectrons]'), isCollection=True),
        Plot("MedElectronDxy",  ["TH1D","MedElectronDxy","",20,0.,0.01],     LambdaFunc('x: [mu.dxy for mu in x.MediumElectrons]'), isCollection=True),
        Plot("MedElectronDz",   ["TH1D","MedElectronDz","",20,0.,0.1],      LambdaFunc('x: [ele.dz for ele in x.MediumElectrons]'), isCollection=True),
        Plot("MedElectronSip",  ["TH1D","MedElectronSip","",20,0.,8],     LambdaFunc('x: [ele.sip3d for ele in x.MediumElectrons]'), isCollection=True),
        ]

allPlots = eventBasedPlots + muonPlots + electronPlots
