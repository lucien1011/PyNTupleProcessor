from Common.Branch import BranchToAdd
from Core.Utils.LambdaFunc import LambdaFunc
import array

label = "_Mini"
listlen = 20
method = "ret_leptonJetRecleaner"
jetVarsToStore = [
        "pt", 
        "eta", 
        "phi", 
        "mass", 
        "btagCSV",
        ]
jecStrs = [
        "",
        "_jecUp",
        "_jecDown",
        ]
jetPtStr = '40'
bJetPtStr = '25'

leptonBranches = [
        BranchToAdd("nLepGood",'i',1,"nLepGood",method=method,inputs="nLepGood"),
        BranchToAdd("nLepLoose",'i',1,"nLepLoose",method=method,inputs="nLepLoose"+label),
        BranchToAdd("nLepLooseVeto",'i',1,"nLepLooseVeto",method=method,inputs="nLepLooseVeto"+label),
        BranchToAdd("nLepCleaning",'i',1,"nLepCleaning",method=method,inputs="nLepCleaning"+label),
        BranchToAdd("nLepCleaningVeto",'i',1,"nLepCleaningVeto",method=method,inputs="nLepCleaningVeto"+label),
        BranchToAdd("nLepFO",'i',1,"nLepFO",method=method,inputs="nLepFO"+label),
        BranchToAdd("nLepFOVeto",'i',1,"nLepFOVeto",method=method,inputs="nLepFOVeto"+label),
        BranchToAdd("nLepTight",'i',1,"nLepTight",method=method,inputs="nLepTight"+label),
        BranchToAdd("nLepTightVeto",'i',1,"nLepTightVeto",method=method,inputs="nLepTightVeto"+label),

        BranchToAdd("indexLoose",'i',20,None,method=method,inputs="iL"+label),
        BranchToAdd("indexLooseVeto",'i',20,None,method=method,inputs="iLV"+label),
        BranchToAdd("indexCleaning",'i',20,None,method=method,inputs="iC"+label),
        BranchToAdd("indexCleaningVeto",'i',20,None,method=method,inputs="iCV"+label),
        BranchToAdd("indexFake",'i',20,None,method=method,inputs="iF"+label),
        BranchToAdd("indexFakeVeto",'i',20,None,method=method,inputs="iFV"+label),
        BranchToAdd("indexTight",'i',20,None,method=method,inputs="iT"+label),
        BranchToAdd("indexTightVeto",'i',20,None,method=method,inputs="iTV"+label),

        BranchToAdd("LepGood_conePt",'f',listlen,"nLepGood",method,"LepGood_conePt"),
        BranchToAdd("LepGood_isLoose",'i',listlen,"nLepGood",method,"LepGood_isLoose"+label),
        BranchToAdd("LepGood_isLooseVeto",'i',listlen,"nLepGood",method,"LepGood_isLooseVeto"+label),
        BranchToAdd("LepGood_isCleaning",'i',listlen,"nLepGood",method,"LepGood_isCleaning"+label),
        BranchToAdd("LepGood_isCleaningVeto",'i',listlen,"nLepGood",method,"LepGood_isCleaningVeto"+label),
        BranchToAdd("LepGood_isFake",'i',listlen,"nLepGood",method,"LepGood_isFO"+label),
        BranchToAdd("LepGood_isFakeVeto",'i',listlen,"nLepGood",method,"LepGood_isFOVeto"+label),
        BranchToAdd("LepGood_isTight",'i',listlen,"nLepGood",method,"LepGood_isTight"+label),
        BranchToAdd("LepGood_isTightVeto",'i',listlen,"nLepGood",method,"LepGood_isTightVeto"+label),
        ]

jetBranches = []
for jecStr in jecStrs:
    tempBranches = [
            BranchToAdd("nJetSel"+jecStr,'i',1,"nJetSel"+jecStr,method=method,inputs="nJetSel"+label+jecStr),
            BranchToAdd("iJetSel"+jecStr,'i',20,"nJetSel"+jecStr,method=method,inputs="iJSel"+label+jecStr),
            
            BranchToAdd("nDiscJetSel"+jecStr,'i',1,"nDiscJetSel"+jecStr,method=method,inputs="nDiscJetSel"+label+jecStr),
            BranchToAdd("iDiscJetSel"+jecStr,'i',20,"nDiscJetSel"+jecStr,method=method,inputs="iDiscJSel"+label+jecStr),
            
            BranchToAdd("nBJetLooseRA5"+jetPtStr+jecStr,'i',1,"nBJetLoose"+jetPtStr+jecStr,method=method,inputs="nBJetLoose"+jetPtStr+label+jecStr),
            BranchToAdd("nBJetMediumRA5"+jetPtStr+jecStr,'i',1,"nBJetMedium"+jetPtStr+jecStr,method=method,inputs="nBJetMedium"+jetPtStr+label+jecStr), 
            BranchToAdd("nBJetLooseRA5"+bJetPtStr+jecStr,'i',1,"nBJetLoose"+bJetPtStr+jecStr,method=method,inputs="nBJetLoose"+bJetPtStr+label+jecStr),
            BranchToAdd("nBJetMediumRA5"+bJetPtStr+jecStr,'i',1,"nBJetMedium"+bJetPtStr+jecStr,method=method,inputs="nBJetMedium"+bJetPtStr+label+jecStr), 
            
            BranchToAdd("nJetRA5"+jetPtStr+jecStr,'i',1,"nJet"+jetPtStr+jecStr,method=method,inputs="nJet"+jetPtStr+label+jecStr),
            BranchToAdd("nJetRA5"+bJetPtStr+jecStr,'i',1,"nJet"+bJetPtStr+jecStr,method=method,inputs="nJet"+bJetPtStr+label+jecStr),

            BranchToAdd("htJet"+jetPtStr+jecStr,'f',1,"htJet"+jetPtStr+jecStr,method=method,inputs="htJet"+jetPtStr+"j"+label+jecStr),
            BranchToAdd("htJet"+bJetPtStr+jecStr,'f',1,"htJet"+bJetPtStr+jecStr,method=method,inputs="htJet"+bJetPtStr+"j"+label+jecStr),
            
            BranchToAdd("mhtJet"+jetPtStr+jecStr,'f',1,"mhtJet"+jetPtStr+jecStr,method=method,inputs="mhtJet"+jetPtStr+label+jecStr),
            BranchToAdd("mhtJet"+bJetPtStr+jecStr,'f',1,"mhtJet"+bJetPtStr+jecStr,method=method,inputs="mhtJet"+bJetPtStr+label+jecStr),

            ]
    jetBranches.extend(tempBranches)
jecStr = ""
for jetVar in jetVarsToStore:
    jetBranches.append(
            BranchToAdd("JetSel"+jecStr+"_"+jetVar,'f',20,"nJetSel"+jecStr,method=method,inputs="JetSel"+label+jecStr+"_"+jetVar),
            )

globalBranches = [
        BranchToAdd("mZ1",'f',1,None,method=method,inputs="mZ1"+label),
        BranchToAdd("minMllAFAS",'f',1,None,method=method,inputs="minMllAFAS"+label),
        BranchToAdd("minMllAFOS",'f',1,None,method=method,inputs="minMllAFOS"+label),
        BranchToAdd("minMllAFSS",'f',1,None,method=method,inputs="minMllAFSS"+label),
        BranchToAdd("minMllSFSS",'f',1,None,method=method,inputs="minMllAFOS"+label),
        ]

branchesToAdd = leptonBranches + globalBranches + jetBranches
