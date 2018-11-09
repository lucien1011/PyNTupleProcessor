from Core.Module import Module

class VariableProducer(Module):
    def analyze(self,event):
        lep12Vec = event.firstLep.p4() + event.secondLep.p4()
        event.mll = lep12Vec.M()
        return True
