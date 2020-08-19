from Core.Module import Module

class TTWWSkimmer(Module):
    def analyze(self,event):
        if event.nBJetMediumRA525[0] < 1:
            return False
        return True
