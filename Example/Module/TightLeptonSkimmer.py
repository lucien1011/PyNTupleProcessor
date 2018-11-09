from Core.Module import Module

class TightLeptonSkimmer(Module):
    def analyze(self,event):
        if len(event.tightLeps)< 2: return False

        event.tightLeps.sort(key=lambda x: x.pt,reverse=True)
        event.firstLep = event.tightLeps[0]
        event.found2nd = False
        for l in event.tightLeps[1:]:
            if l.charge == -1*event.firstLep.charge:
                event.found2nd = True
                event.secondLep = l
        if not event.found2nd: return False
        return True
