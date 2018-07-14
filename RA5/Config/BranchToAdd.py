from Common.Branch import BranchToAdd
from Core.Utils.LambdaFunc import LambdaFunc
import array

label = "_Mini"
listlen = 20
method = "ret_leptonJetRecleaner"

branchesToAdd = [
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
        BranchToAdd("LepGood_isLoose",'f',listlen,"nLepGood",method,"LepGood_isLoose"+label),
        BranchToAdd("LepGood_isLooseVeto",'f',listlen,"nLepGood",method,"LepGood_isLooseVeto"+label),
        BranchToAdd("LepGood_isCleaning",'f',listlen,"nLepGood",method,"LepGood_isCleaning"+label),
        BranchToAdd("LepGood_isCleaningVeto",'f',listlen,"nLepGood",method,"LepGood_isCleaningVeto"+label),
        BranchToAdd("LepGood_isFake",'f',listlen,"nLepGood",method,"LepGood_isFO"+label),
        BranchToAdd("LepGood_isFakeVeto",'f',listlen,"nLepGood",method,"LepGood_isFOVeto"+label),
        BranchToAdd("LepGood_isTight",'f',listlen,"nLepGood",method,"LepGood_isTight"+label),
        BranchToAdd("LepGood_isTightVeto",'f',listlen,"nLepGood",method,"LepGood_isTightVeto"+label),
        ]
