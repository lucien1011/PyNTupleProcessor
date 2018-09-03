from Core.Module import Module
from Core.Collection import Collection

class JetProducer(Module):
    def analyze(self,event):
        event.jets = Collection(event,"Jet")
        event.discjets = Collection(event,"DiscJet")
        event.selJets = []
        for ijet in event.iJetSel:
            try:
                jetToAdd = None
                if ijet >= 0:
                    index = ijet
                    jetToAdd = event.jets[index]
                else:
                    index = -ijet-1
                    jetToAdd = event.discjets[index]
                if jetToAdd and jetToAdd.pt > 40 and abs(jetToAdd.eta) < 2.4:
                    event.selJets.append(jetToAdd)
            except IndexError:
                self.writer.objs["DiscardedEvent"].Fill(0)
        event.selJets.sort(key=lambda x: x.pt,reverse=True)
        return True
