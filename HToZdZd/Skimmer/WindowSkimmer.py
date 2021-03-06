from Core.Module import Module

class WindowSkimmer(Module):
    def __init__(self,name,invert=False):
        super(WindowSkimmer,self).__init__(name)
        self.invert = invert
    def analyze(self,event):
        if abs(event.idL1[0]) == 11 and abs(event.idL2[0]) == 11 and abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11:
            r1 = 0.05
            r2 = 0.05
        elif abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11:
            r1 = 0.02
            r2 = 0.05
        elif abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13:
            r1 = 0.02
            r2 = 0.02
        elif abs(event.idL1[0]) == 11 and abs(event.idL2[0]) == 11 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13:
            r1 = 0.05
            r2 = 0.02
        if not self.invert:
            return (event.massZ1[0]>(1.-r1)/(1+r2)*event.massZ2[0]) and (event.massZ1[0]<(1.+r1)/(1-r2)*event.massZ2[0])
        else:
            return not ((event.massZ1[0]>(1.-r1)/(1+r2)*event.massZ2[0]) and (event.massZ1[0]<(1.+r1)/(1-r2)*event.massZ2[0]))
