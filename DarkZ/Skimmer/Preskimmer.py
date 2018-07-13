from Core.Module import Module

class Preskimmer(Module):
    def analyze(self,event):
        if len(event.lep_id) < 4 or len(event.lep_pt) < 4: return False
        return True

class GENPreskimmer(Module):
    def analyze(self,event):
        if self.dataset.isMC and not self.dataset.isSignal:
            return (event.GENZ_DaughtersId[0] == 11 or event.GENZ_DaughtersId[0] == 13) and (event.GENZ_DaughtersId[1] == 11 or event.GENZ_DaughtersId[1] == 13)
        elif self.dataset.isSignal:
            return True
        else:
            return True
