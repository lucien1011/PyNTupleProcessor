from Core.Module import Module

class EventPrinter(Module):
    def analyze(self,event):
        print event.muon_pt[0]
