from Core.Module import Module
import ROOT

class FakeRateWeighter(Module):
    def __init__(self,name,wrong_fc_name="WrongFC_Reducible",pred_cr_name="PredCR"):
        super(FakeRateWeighter,self).__init__(name)
        self.wrong_fc_name = wrong_fc_name
        self.pred_cr_name = pred_cr_name

    def analyze(self,event):
        if self.wrong_fc_name in self.dataset.name:
            if event.FRWeightProd[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 1:
                event.weight *= event.FRWeightProd[0]
            elif event.nFailedLeptonsZ2[0] == 2:
                event.weight *= -1*event.FRWeightProd[0]
            else:
                return False
        elif self.pred_cr_name in self.dataset.name:
            #if event.nZXCRFailedLeptons[0] == 1:
            if event.FRWeightSum[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 2:
                event.weight *= event.FRWeightSum[0]
            else:
                return False
        return True
