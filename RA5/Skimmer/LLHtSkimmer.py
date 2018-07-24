from Core.Module import Module

class LLHtSkimmer(Module):
    def analyze(self,event):
        if event.cat.lepCat == "LL": return event.htJet40[0] > 300.
        return True
