from Core.Module import Module

class EventWeighter(Module):
    def analyze(self,event):
        event.weight = 1.
        return True
