from Core.Module import Module

class AnalysisProducer(Module):
    def analyze(self,event):
        event.muons = [p for p in event.MediumMuons if p.pt > 40]
        event.muons.sort(key=lambda x: x.pt,reverse=True)

        event.eles = [p for p in event.MediumElectrons if p.pt > 40]
        event.eles.sort(key=lambda x: x.pt,reverse=True)
        
        event.leps = event.muons + event.eles
        event.leps.sort(key=lambda x: x.pt,reverse=True)
        event.nLep40 = len(event.leps)

        event.jets = [p for p in event.LooseJets if p.pt > 40]
        event.jets.sort(key=lambda x: x.pt,reverse=True)
        event.nJet40 = len(event.jets)

        event.ht40 = 0.
        for ps in [event.jets,event.leps]:
            for p in ps:
                event.ht40 += p.pt
        
        if event.nLep40 >= 2:
            vecSum = event.leps[0].p4() + event.leps[1].p4()
            event.mll = vecSum.M()
        else:
            event.mll = None


        k1 = sqrt((Et(b1)+Et(l1))^2 - (pT(b1)-pT(l1))^2)
	k2 = sqrt((Et(b1)+Et(l2))^2 - (pT(b1)-pT(l2))^2)
        if k1 >= k2:
           event.m0_bl = k1
           event.m1_bl = k2
        else:
	    event.m0_bl = k2
	    event.m1_bl = k1



        event.m_asym_bl = (event.m0_bl - event.m1_bl)/(event.m0_bl + event.m1_bl)

        
        return True
