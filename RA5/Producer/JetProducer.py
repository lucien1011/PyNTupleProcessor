from Core.Module import Module
from Core.Collection import Collection

class JetProducer(Module):
    def begin(self):
        self.writer.book("DiscardedEvent","TH1D","DiscardedEvent","",1,-0.5,0.5)

    def analyze(self,event):
        event.jets = Collection(event,"Jet")
        event.discjets = Collection(event,"DiscJet")
        event.selJets = []
        event.iJetSel = [int(ijet) for ijet in event.JetSelIndex]
        for ijet in event.iJetSel:
        #for ijet in event.JetSelIndex:
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
                return False
        event.selJets.sort(key=lambda x: x.pt,reverse=True)
        return True
