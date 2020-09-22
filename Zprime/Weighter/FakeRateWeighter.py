from Core.Module import Module
import ROOT

analyze_name = "analyze"
make_map_name = "make_map"
syst_name = "syst"

class FakeRateWeighter(Module):
    def __init__(self,name,task="analyze"):
        super(FakeRateWeighter,self).__init__(name)
        self.task = task

    def analyze(self,event):
        event.weight_FRUniIso = 1.
        event.weight_FRAsymIso = 1.
        if "ZPlusX" in self.dataset.name and self.task == analyze_name:
            if event.FRWeightProd[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 1:
                event.weight *= event.FRWeightProd[0]
                event.weight_FRUniIso *= event.FRWeightProd[0]/event.FRWeightProd[0]
                event.weight_FRAsymIso *= event.FRWeightProd[0]/event.FRWeightProd[0]
            elif event.nFailedLeptonsZ2[0] == 2:
                event.weight *= -1*event.FRWeightProd[0]
                if event.deltaRL34 < 0.6:
                    event.weight_FRUniIso *= event.FRWeightProd_UniIso[0]/event.FRWeightProd[0]
                    event.weight_FRAsymIso *= event.FRWeightProd_AsymIso[0]/event.FRWeightProd[0]
            else:
                return False
        elif "ZPlusX" in self.dataset.name and self.task == syst_name:
            if event.FRWeightProd[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 1:
                event.weight *= event.FRWeightProd[0]
                event.weight_FRUniIso *= event.FRWeightProd[0]/event.FRWeightProd[0]
                event.weight_FRAsymIso *= event.FRWeightProd[0]/event.FRWeightProd[0]
                #event.weight *= event.FRWeight[0]
            elif event.nFailedLeptonsZ2[0] == 2:
                event.weight *= -1*event.FRWeightProd[0]
                if event.deltaRL34 < 0.6:
                    event.weight_FRUniIso *= event.FRWeightProd_UniIso[0]/event.FRWeightProd[0]
                    event.weight_FRAsymIso *= event.FRWeightProd_AsymIso[0]/event.FRWeightProd[0]
                    if event.massZ2[0] < 6.:
                        event.weight_FRUniIso *= -1.
                        event.weight_FRAsymIso *= -1.
            else:
                return False
        elif "ZPlusX" in self.dataset.name and self.task == make_map_name:
            if event.FRWeightProd[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 1:
                event.weight *= event.FRWeightProd[0]
            elif event.nFailedLeptonsZ2[0] == 2:
                event.weight *= -1*event.FRWeightProd[0]
            else:
                return False
        elif "PredCR" in self.dataset.name and self.dataset.isMC:
            #if event.nZXCRFailedLeptons[0] == 1:
            if event.FRWeightSum[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 2:
                #event.weight *= event.FRWeightSum[0]
                #if event.deltaRL34 > 0.6:
                if event.massZ2[0] > 12.:
                    event.weight *= event.FRWeightSum[0]
                else:
                    #event.weight *= event.FRWeightSum[0]
                    #event.weight *= event.FRWeightProd_AsymIso[0]
                    event.weight *= (event.FRWeightL3[0]+event.FRWeightL4[0])/2.
            else:
                return False
        return True
