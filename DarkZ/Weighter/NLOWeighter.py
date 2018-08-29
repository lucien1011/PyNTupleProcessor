from Core.Module import Module

class NLOWeighter(Module):
    def analyze(self,event):
        if "qqZZTo4L" in self.dataset.parent.name:
            event.weight *= event.k_qqZZ_qcd_M[0]*event.k_qqZZ_ewk[0]
        if "ggZZ" in self.dataset.parent.name:
            event.weight *= event.k_ggZZ[0]
        return True
