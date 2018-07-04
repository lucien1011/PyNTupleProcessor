from Core.Module import Module

class Preskimmer(Module):
    def analyze(self,event):
        if len(event.lep_id) < 4 or len(event.lep_pt) < 4: return False
        return True
