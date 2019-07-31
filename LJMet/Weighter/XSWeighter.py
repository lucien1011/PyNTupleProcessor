from Core.Module import Module

class XSWeighter(Module):
    def __init__(self,name):
        super(XSWeighter,self).__init__(name)
        self.fb_to_pb_factor = 1000

    def analyze(self,event):
        event.weight = 1.
        if self.dataset.isMC and not self.dataset.skipWeight:
            event.weight *= event.MCWeight_MultiLepCalc[0]/abs(event.MCWeight_MultiLepCalc[0])
            xs = self.dataset.xs
            nevts = self.dataset.sumw
            lumi = self.dataset.lumi
            event.weight *= xs*lumi*self.fb_to_pb_factor/self.dataset.sumw
        return True
