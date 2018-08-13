from Core.Module import Module
import ROOT

class FakeRateWeighter(Module):
    def analyze(self,event):
        if "ZPlusX" in self.dataset.name:
            #if event.nZXCRFailedLeptons[0] == 1:
            if event.FRWeight == -1.: continue
            if event.nFailedLeptonsZ2[0] == 1:
                event.weight *= event.FRWeight[0]
            #elif event.nZXCRFailedLeptons[0] == 2:
            elif event.nFailedLeptonsZ2[0] == 2:
                event.weight *= -1*event.FRWeight[0]
            else:
                return False
        return True
