from Core.Module import Module
from Core.Collection import Collection

class NJet40Producer(Module):
    def begin(self):
        self.writer.book("DiscardedEvent","TH1D","DiscardedEvent","",1,-0.5,0.5)

    def analyze(self,event):
        event.jets = Collection(event,"Jet")
        event.discjets = Collection(event,"DiscJet")
        event.nJet40_recal = 0
        for ijet in event.iJetSel:
            try:
                if ijet >= 0:
                    index = ijet
                    jetPt = event.jets[index].pt 
                    jetEta = abs(event.jets[index].eta)
                else:
                    index = -ijet-1
                    jetPt = event.discjets[index].pt 
                    jetEta = abs(event.discjets[index].eta)
            except IndexError:
                self.writer.objs["DiscardedEvent"].Fill(0)
            if jetPt > 40 and jetEta < 2.4:
                event.nJet40_recal += 1
            
        return True
