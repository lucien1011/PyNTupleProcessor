from Core.Module import Module

class HLTSkimmer(Module):
    def __init__(self,name,cutflow="LooseSignal"):
        super(HLTSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if(self.dataset.isMC):
            return True
            #return event.HLT_IsoMu22[0] or event.HLT_IsoTkMu22[0] or event.HLT_IsoMu24[0] or event.HLT_IsoTkMu24[0] or event.HLT_Ele27_eta2p1_WPTight_Gsf[0] or event.HLT_Ele27_eta2p1_WPTight_Gsf[0]
        if("SingleMuon" in self.dataset.parent.name):
          return event.HLT_IsoMu22[0] or event.HLT_IsoTkMu22[0] or event.HLT_IsoMu24[0] or event.HLT_IsoTkMu24[0] or event.HLT_Ele27_eta2p1_WPTight_Gsf[0]
        elif("SingleElectron" in self.dataset.parent.name):
            if(not (event.HLT_IsoMu22[0] or event.HLT_IsoTkMu22[0] or event.HLT_IsoMu24[0] or event.HLT_IsoTkMu24[0])):
                return event.HLT_Ele27_eta2p1_WPTight_Gsf[0]
        #else:
            #return event.HLT_IsoMu22[0] or event.HLT_IsoTkMu22[0] or event.HLT_IsoMu24[0] or event.HLT_IsoTkMu24[0] or event.HLT_Ele27_eta2p1_WPTight_Gsf[0]

