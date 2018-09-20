from Core.Module import Module 
from RA5.LeptonJetRecleaner.Algo import passMllVeto
from RA5.LeptonJetRecleaner.LeptonDefinition import _susy2lss_lepId_CBloose,_susy2lss_lepId_loosestFO,_susy2lss_lepId_IPcuts,_susy2lss_lepConePt1015,_susy2lss_lepId_tighterFO,_susy2lss_multiIso,_susy2lss_lepId_CB,_susy2lss_idIsoEmu_cuts
from RA5.LeptonJetRecleaner.conept import conept_RA5

class SyncSkimmer(Module):
    def analyze(self,event):
        #if len(event.selJets) < 2: return False
        #event.tightLeps = [lep for lep in event.goodLeps if lep.pt>10 and _susy2lss_lepConePt1015(lep) and _susy2lss_multiIso(lep) and _susy2lss_lepId_CB(lep) and (event.htJet40[0]>300 or _susy2lss_idIsoEmu_cuts(lep))] # cuts applied on top of loose
        event.tightLeps.sort(key=lambda l: l.pt,reverse=True)
        event.tightLepsPt = [ l for l in event.tightLeps if (abs(l.pdgId) == 11 and l.pt > 15 ) or (abs(l.pdgId) == 13 and l.pt > 10)]
        event.tightLepsPt.sort(key=lambda l: l.pt,reverse=True)

        nSSLepPlus = 0
        nSSLepMinus = 0
        for l in event.tightLepsPt:
            if l.pdgId == 11 or l.pdgId == 13: nSSLepPlus += 1
            if l.pdgId == -11 or l.pdgId == -13: nSSLepMinus += 1
        
        mllList = []
        nTightLep = len(event.tightLeps)
        for il in range(0,nTightLep-1):
            lep1 = event.tightLeps[il]
            for jl in range(il+1,len(event.tightLeps)):
                lep2 = event.tightLeps[jl]
                lep12Vec = lep1.p4()+lep2.p4()
                mll = lep12Vec.M()
                mllList.append(mll)

        if event.nJetRA540[0] < 2: return False
        #if event.nJetSel[0] < 2: return False
        #if len(event.selJets) < 2: return False
        #print event.nJetRA540[0],event.nJetSel[0],len(event.selJets),len(event.iJetSel),sum([j.pt for j in event.selJets]),event.htJet40[0]
        
        if event.htJet40[0] < 80.: return False
        #if sum([j.pt for j in event.selJets]) < 80.: return False
        
        if nSSLepPlus < 2 and nSSLepMinus < 2: return False
        
        if not self.passMllTL(event.looseLeps,event.tightLeps,[0.,12.]): return False
        if not self.passMllTL(event.looseLeps,event.tightLeps,[76.,106.]): return False

        if min(mllList) < 8.: return False
        return True
    
    #def passMllTL(self,lepsl, lepst , mZ1Ranges, mZ2Ranges):
    def passMllTL(self,lepsl, lepst , mZ1Ranges):
        pairs = []
        for l1 in lepst:
            for l2 in lepsl:
                if l2 == l1: continue
                if not passMllVeto(l1,l2,mZ1Ranges[0],mZ1Ranges[1],True): return False
                #if not passMllVeto(l1,l2,mZ2Ranges[0],mZ2Ranges[1],True): return False
        return True
