from Core.Module import Module

class NarrowResonanceSkimmer(Module):
    def __init__(self,name,resonances):
        super(NarrowResonanceSkimmer,self).__init__(name)
        self.resonances = resonances

    def analyze(self,event):
        for resonance in self.resonances:
            if resonance.selFunc(event): return False
        return True

    def end(self):
        for resonance in self.resonances:
            resonance.selFunc.end()
