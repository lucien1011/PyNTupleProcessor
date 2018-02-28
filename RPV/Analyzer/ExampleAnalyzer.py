from Core.Module import Module

class ExampleAnalyzer(Module):
    def begin(self):
        self.writer.book("nBJet25","TH1D","nBJet25","",10,-0.5,9.5)
        self.writer.book("nJet40","TH1D","nJet40","",20,-0.5,19.5)
        self.writer.book("ht40","TH1D","ht40","",60,0.,6000.)
        
    def analyze(self,event):
        ht40 = sum([j.pt for j in event.LooseJets if j.pt > 40])
        nBJet25 = len([j for j in event.LooseJets if j.btagCSVV2 > 0.8989])
        nJet40 = len([j for j in event.LooseJets if j.pt > 40])
        
        self.writer.objs["nJet40"].Fill(nJet40)
        self.writer.objs["nBJet25"].Fill(nBJet25)
        self.writer.objs["ht40"].Fill(ht40)

        return True
