from RA5.LeptonJetRecleaner.LeptonDefinition import _susy2lss_lepId_CBloose,_susy2lss_lepId_loosestFO,_susy2lss_lepId_IPcuts,_susy2lss_lepConePt1015,_susy2lss_lepId_tighterFO,_susy2lss_multiIso,_susy2lss_lepId_CB,_susy2lss_idIsoEmu_cuts
from RA5.LeptonJetRecleaner.conept import conept_RA5
from RA5.LeptonJetRecleaner.Algo import LeptonJetRecleaner

jetVarToStoreList = [
    #'mcMatchFlav',
    #'charge',
    #'ctagCsvL',
    #'ctagCsvB',
    #'area',
    #'qgl',
    #'ptd',
    #'axis2',
    #'mult',
    #'partonId',
    #'partonMotherId',
    #'nLeptons',
    #'id',
    #'puId',
    'btagCSV',
    #'btagCMVA',
    #'rawPt',
    #'mcPt',
    'mcFlavour',
    'partonFlavour',
    #'hadronFlavour',
    #'mcMatchId',
    #'corr_JECUp',
    #'corr_JECDown',
    #'corr',
    #'corr_JERUp',
    #'corr_JERDown',
    #'corr_JER',
    'pt',
    'eta',
    'phi',
    'mass',
    #'CorrFactor_L1',
    #'CorrFactor_L1L2',
    #'CorrFactor_L1L2L3',
    #'CorrFactor_L1L2L3Res',
    #'chHEF',
    #'neHEF',
]

leptonJetRecleaner2016 = LeptonJetRecleaner(
    "LeptonJetRecleaner2016",
    "Mini",
    lambda lep : lep.miniRelIso < 0.4 and _susy2lss_lepId_CBloose(lep), #and (ht>300 or _susy2lss_idIsoEmu_cuts(lep)),
    lambda lep : lep.pt>10 and _susy2lss_lepId_loosestFO(lep) and _susy2lss_lepId_IPcuts(lep), # cuts applied on top of loose
    lambda lep,ht : lep.pt>10 and _susy2lss_lepConePt1015(lep) and _susy2lss_lepId_IPcuts(lep) and (_susy2lss_lepId_loosestFO(lep) if ht>300 else _susy2lss_lepId_tighterFO(lep)), # cuts applied on top of loose
    lambda lep,ht : lep.pt>10 and _susy2lss_lepConePt1015(lep) and _susy2lss_multiIso(lep) and _susy2lss_lepId_CB(lep) and (ht>300 or _susy2lss_idIsoEmu_cuts(lep)), # cuts applied on top of loose
    cleanJet = lambda lep,jet,dr : dr<0.4,
    selectJet = lambda jet: abs(jet.eta)<2.4,
    cleanTau = lambda lep,tau,dr: dr<0.4,
    looseTau = lambda tau: tau.pt > 20 and abs(tau.eta)<2.3 and abs(tau.dxy) < 1000 and abs(tau.dz) < 0.2 and tau.idMVANewDM >= 1 and tau.idDecayMode, # used in cleaning
    tightTau = lambda tau: tau.idMVANewDM == 3, # on top of loose
    cleanJetsWithTaus = False,
    doVetoZ = True,
    doVetoLMf = True,
    doVetoLMt = True,
    jetPt = 40,
    bJetPt = 25,
    coneptdef = lambda lep: conept_RA5(lep),
    storeJetVariables = True,
    jetVarToStore = " ".join(jetVarToStoreList),
    )

leptonAlgoDict = {
    "Run2016": leptonJetRecleaner2016,
}
