from Core.Module import Module

class ZMuMuSkimmer(Module):
    def analyze(self,event):

        event.jets = [p for p in event.LooseJets if p.pt > 40]
        event.jets.sort(key=lambda x: x.pt,reverse=True)
        event.nJet40 = len(event.jets)

        event.ht40 = 0.
        for ps in [event.jets]:
            for p in ps:
                event.ht40 += p.pt

        event.muons = [p for p in event.MediumMuons if p.pt > 40]
        event.muons.sort(key=lambda x: x.pt,reverse=True)

        if len(event.muons) < 2: return False
        if event.muons[0].charge == event.muons[1].charge: return False

        event.nMuon40 = len(event.muons)

        vecSum = event.muons[0].p4() + event.muons[1].p4()
        event.mll = vecSum.M()
        if event.mll < 60: return False
        if event.mll > 120: return False

        return True
