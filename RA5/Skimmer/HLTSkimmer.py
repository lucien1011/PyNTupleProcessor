from Core.Module import Module

class HLTSkimmer(Module):
    def __init__(self,name,emulation=False,cutflow="SR"):
        super(HLTSkimmer,self).__init__(name)
        self.emulation = emulation
        self.cutflow = cutflow

    def return_sr_trigger(self,event):
        if self.emulation or (self.dataset.isData and "2016" in self.dataset.parent.name):
            notRunH = ("2016H" not in self.dataset.parent.name and self.dataset.isData) or self.dataset.isMC
            if event.htJet40[0] < 300.:
                if abs(event.firstLep.pdgId) == abs(event.secondLep.pdgId) and abs(event.firstLep.pdgId) == 11:
                    return event.HLT_BIT_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v[0] 
                elif abs(event.firstLep.pdgId) == abs(event.secondLep.pdgId) and abs(event.firstLep.pdgId) == 13:
                    if notRunH:
                        return event.HLT_BIT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v[0] or event.HLT_BIT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v[0]
                    else:
                        return event.HLT_BIT_HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v[0] or event.HLT_BIT_HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v[0]
                elif (abs(event.firstLep.pdgId) == 13 and abs(event.secondLep.pdgId) == 11) or (abs(event.firstLep.pdgId) == 11 and abs(event.secondLep.pdgId) == 13):
                    if notRunH:
                        return event.HLT_BIT_HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v[0] or event.HLT_BIT_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v[0]
                    else:
                        return event.HLT_BIT_HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v[0] or event.HLT_BIT_HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v[0]
            else:
                if notRunH:
                    if abs(event.firstLep.pdgId) == abs(event.secondLep.pdgId) and abs(event.firstLep.pdgId) == 11:
                        return event.HLT_BIT_HLT_DoubleMu8_Mass8_PFHT300_v[0]
                    elif abs(event.firstLep.pdgId) == abs(event.secondLep.pdgId) and abs(event.firstLep.pdgId) == 13:
                        return event.HLT_BIT_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v[0]
                    elif (abs(event.firstLep.pdgId) == 13 and abs(event.secondLep.pdgId) == 11) or (abs(event.firstLep.pdgId) == 11 and abs(event.secondLep.pdgId) == 13):
                        return event.HLT_BIT_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v[0]
                else:
                    passTrig = False
                    if abs(event.firstLep.pdgId) == abs(event.secondLep.pdgId) and abs(event.firstLep.pdgId) == 11:
                        passTrig = event.HLT_BIT_HLT_DoubleMu8_Mass8_PFHT300_v[0]
                    elif abs(event.firstLep.pdgId) == abs(event.secondLep.pdgId) and abs(event.firstLep.pdgId) == 13:
                        passTrig = event.HLT_BIT_HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v[0]
                    elif (abs(event.firstLep.pdgId) == 13 and abs(event.secondLep.pdgId) == 11) or (abs(event.firstLep.pdgId) == 11 and abs(event.secondLep.pdgId) == 13):
                        passTrig = event.HLT_BIT_HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v[0]
                    if not passTrig and self.dataset.isData:
                        return event.HLT_BIT_HLT_PFJet450_v[0]
                    else:
                        return passTrig

        else:
            raise RuntimeError,"Data other than 2016 are not supported atm"

    def analyze(self,event):
        if self.dataset.isMC and not self.emulation: return True

        if not hasattr(event,"firstLep") or not hasattr(event,"secondLep"):
            event.tightLeps.sort(key=lambda x: x.pt,reverse=True)
            firstLep = event.tightLeps[0]
            for l in event.tightLeps[1:]:
                if l.charge*event.tightLeps[0].charge > 0.:
                    secondLep = l
            event.firstLep = firstLep
            event.secondLep = secondLep

        if self.cutflow == "SR":
            return self.return_sr_trigger(event)
        elif self.cutflow == "TightLoose":
            #return self.return_tl_trigger(event)
            return self.return_sr_trigger(event)
        else:
            raise RuntimeError,"cutflow other than SR and TightLoose are not supported atm"
