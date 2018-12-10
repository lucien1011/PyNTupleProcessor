
from Core.Module import Module

wrong_fc_name = "WrongFC"
pred_cr_name = "PredCR"

class WrongFCSkimmer(Module):
    def __init__(self,name,cutflow="SR",wrong_fc_name=wrong_fc_name,pred_cr_name=pred_cr_name):
        super(WrongFCSkimmer,self).__init__(name)
        self.cutflow = cutflow
        self.wrong_fc_name = wrong_fc_name
        self.pred_cr_name = pred_cr_name

    def analyze(self,event):
        if self.cutflow == "CR":
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            if event.passedFullSelection[0]: return False
        elif self.cutflow == "3P1F":
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            if self.pred_cr_name not in self.dataset.name:
                if event.nZXCRFailedLeptons[0] != 1: return False
            if event.passedFullSelection[0]: return False
        elif self.cutflow == "SR":
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            if self.wrong_fc_name not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
        return True
