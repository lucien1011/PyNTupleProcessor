from Core.Module import Module

class TTbarSkimmer(Module):
    def __init__(self,name,csvCut=0.8484,cutflow="LooseSignal"):
        self.csvCut = csvCut
        self.cutflow = cutflow

    def analyze(self,event):
        event.jets = [p for p in event.LooseJets if p.pt > 30]
        event.jets.sort(key=lambda x: x.pt,reverse=True)
        event.nJet40 = len(event.jets)

        event.ht40 = 0.
        for ps in [event.jets]:
            for p in ps:
                event.ht40 += p.pt

        event.muons = [p for p in event.MediumMuons if p.pt > 30]
        event.muons.sort(key=lambda x: x.pt,reverse=True)

        event.eles = [p for p in event.MediumElectrons if p.pt > 30]
        event.eles.sort(key=lambda x: x.pt,reverse=True)

        if len(event.muons) < 1: return False
        if len(event.eles) < 1: return False

        temp = False

        for i in range(0,len(event.jets)):
            if event.jets[i].btagCSVV2 >= self.csvCut:
               temp = True
               break
        else:
               temp = False

        if not temp: return False

        event.nMuon40 = len(event.muons)

        return True
