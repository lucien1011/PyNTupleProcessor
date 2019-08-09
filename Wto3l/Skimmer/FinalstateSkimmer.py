from Core.Module import Module
import ROOT as r

class FinalstateSkimmer(Module):
    def __init__(self,name):
        super(FinalstateSkimmer,self).__init__(name)
        
    def analyze(self,event):
        '''
        if ("Data_sr_Run2016" in self.dataset.name) or ("WZTo3LNu" in self.dataset.name) or ("WmTo3munu" in self.dataset.name) or ("WpTo3munu" in self.dataset.name):
            if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and event.IsoL3[0] < 0.35:
                return True
            else:
                return False
        if "Data_Run2016" in self.dataset.name:
            if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and event.IsoL3[0] >= 0.35:
                return True
            else:
                return False
        ''' 
        '''
        if ("Data_memCR_Run2016" in self.dataset.name) or ("WZTo3LNu_memCR" in self.dataset.name) or ("TTJets_memCR" in self.dataset.name) or ("DYJetsToLL_M50_memCR" in self.dataset.name) or ("DYJetsToLL_M10To50_memCR" in self.dataset.name):
            if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13:# and event.IsoL3[0] >= 0.35 and event.etaL3[0] <= 1.4:
                return True
            elif abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13:# and event.IsoL3[0] >= 0.35 and event.etaL3[0] <= 1.4:
                return True
            else:
                return False
        if "Data_memCR_sr_Run2016" in self.dataset.name:
            if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13:# and event.IsoL3[0] >= 0.35 and event.etaL3[0] <= 1.4:
                return True
            elif abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13:# and event.IsoL3[0] >= 0.35 and event.etaL3[0] <= 1.4:
                return True
            else:
                return False
        '''
        
        if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13:
            return True
        else:
            return False
        ''' 
        if "TTJets_fromT" in self.dataset.name:
            if abs(event.MomIdL3[0]) != 24:
                return False
        if "TTJets_notfromT" in self.dataset.name:
            if abs(event.MomIdL3[0]) == 24:
                return False
        if "TTJets_fromT" in self.dataset.name:
            #event.weight *= 56.54600853*2.43
            event.weight *= 101.72
        '''
        return True
