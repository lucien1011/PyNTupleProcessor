from Core.Module import Module

class EventPrinter(Module):
    def begin(self):
        self.writer.book("muonPt","TH1D","muonPt","",20,0.,100.)
        
    def analyze(self,event):
        self.writer.objs["muonPt"].Fill(event.muon_pt[0])
        return True
