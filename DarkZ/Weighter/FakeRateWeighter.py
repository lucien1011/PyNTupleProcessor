from Core.Module import Module
import ROOT

analyze_name = "analyze"
make_map_name = "make_map"

class FakeRateWeighter(Module):
    def __init__(self,name,task="analyze"):
        super(FakeRateWeighter,self).__init__(name)
        self.task = task
        self.deltaR_iso = 0.6

    def analyze(self,event):
        event.weight_FRUniIso = 1.
        event.weight_FRAsymIso = 1.
        if "WFC_Reducible" in self.dataset.name and self.task == analyze_name:
            if event.FRWeightProd[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 1:
                if event.massZ2[0] > 6.:
                    event.weight *= event.FRWeightProd[0]
                    event.weight_FRUniIso_Up *= event.FRWeightProd[0]
                    event.weight_FRUniIso_Down *= event.FRWeightProd[0]
                    #event.weight *= event.FRWeight[0]
                else:
                    return False
            elif event.nFailedLeptonsZ2[0] == 2:
                if event.massZ2[0] > 6.: 
                    event.weight *= -1*event.FRWeightProd[0]
                else:
                    event.weight *= event.FRWeightProd[0]
                #if event.deltaRL34 > 0.6:
                #    event.weight_FRUniIso_Up *= -1*event.FRWeightProd[0]
                #    event.weight_FRUniIso_Down *= -1*event.FRWeightProd[0]
                #else:
                #    event.weight_FRUniIso_Up *= -1*event.FRWeightProdCorr[0]
                #    event.weight_FRUniIso_Down *= -1*event.FRWeightProdCorr[0]
            else:
                return False
        elif "ZPlusX" in self.dataset.name and self.task == analyze_name:
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
                else:
                    event.weight_FRUniIso *= event.FRWeightProd[0]/event.FRWeightProd[0]
                    event.weight_FRAsymIso *= event.FRWeightProd[0]/event.FRWeightProd[0]
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
        elif "PredCR" in self.dataset.name:
            #if event.nZXCRFailedLeptons[0] == 1:
            if event.FRWeightSum[0] == -1.: return False
            if event.nFailedLeptonsZ2[0] == 2:
                event.weight *= event.FRWeightSum[0]
                #if event.deltaRL34 > 0.6:
                #    event.weight *= event.FRWeightSum[0]
                #else:
                #    event.weight *= event.FRWeightSumCorrIso[0]
            else:
                return False
        return True
