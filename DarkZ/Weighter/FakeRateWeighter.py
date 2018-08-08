from Core.Module import Module
import ROOT

el_histName_br = "h1D_FRel_EB"
el_histName_ec = "h1D_FRel_EE"
mu_histName_br = "h1D_FRmu_EB"
mu_histName_ec = "h1D_FRmu_EE"

class FakeRateWeighter(Module):
    def analyze(self,event):
        if "ZPlusX" in self.dataset.name:
            if event.nZXCRFailedLeptons[0] == 1:
                event.weight *= -1*event.FRWeight[0]
            elif event.nZXCRFailedLeptons[0] == 2:
                event.weight *= event.FRWeight[0]
            #else:
            #    return False
        return True 
