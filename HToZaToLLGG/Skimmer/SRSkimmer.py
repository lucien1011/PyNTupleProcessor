import ROOT

from Core.Module import Module
from Core.Collection import Collection
from Core.BaseObject import BaseObject

from Physics.Z import Z_mass

class ResolvedSRSkimmer(Module):
    def analyze(self,event):
        if len(event.selElectrons) < 2 or len(event.selMuons) < 2: return False
        if len(event.selPhotons) < 2: return False
        event.Zcands = []
        for i,iEl in enumerate(event.selElectrons):
            for j,jEl in enumerate(event.selElectrons):
                if i >= j: continue
                if iEl.charge == jEl.charge: continue
                tmpCand = BaseObject(
                        "Zee_"+str(i)+"_"+str(j),
                        index1 = i,
                        index2 = j,
                        lep1P4 = iEl.p4(),
                        lep2P4 = jEl.p4(),
                        )
                tmpCand.m = (tmpCand.lep1P4+tmpCand.lep2P4).M()
                tmpCand.dm = abs(tmpCand.m-Z_mass)
                event.Zcands.append(tmpCand)
        for i,iMu in enumerate(event.selMuons):
            for j,jMu in enumerate(event.selMuons):
                if i >= j: continue
                if iMu.charge == jMu.charge: continue
                tmpCand = BaseObject(
                        "Zmm_"+str(i)+"_"+str(j),
                        index1 = i,
                        index2 = j,
                        lep1P4 = iMu.p4(),
                        lep2P4 = jMu.p4(),
                        )
                tmpCand.m = (tmpCand.lep1P4+tmpCand.lep2P4).M()
                tmpCand.dm = abs(tmpCand.m-Z_mass)
                event.Zcands.append(tmpCand)
        if not event.Zcands: return False
        dmList = [x.dm for x in event.Zcands]
        minIndex = dmList.index(min(dmList))
        event.Zcand = event.Zcands[minIndex]
        return True

class MergedSRSkimmer(Module):
    def analyze(self,event):
        if len(event.selElectrons) != 2: return False
        if event.selElectrons[0].charge == event.selElectrons[1].charge: return False
        if len(event.selPhotons) >= 1: return False
        return True
