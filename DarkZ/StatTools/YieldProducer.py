from Core.Module import Module

class YieldProducer(Module):
    def __init__(self,name,mass_window_list,systList=[]):
        self.name = name
        self.mass_window_list = mass_window_list
        self.systList = systList

    def begin(self):
        for mWindow in self.mass_window_list:
            self.writer.book(mWindow.makeHistName()+"_"+self.dataset.parent.name,"TH1D",mWindow.makeHistName(),"",1,-0.5,0.5)
            for syst in self.systList:
                self.writer.book(mWindow.makeHistName()+"_"+syst.name,"TH1D",mWindow.makeHistName()+"_"+syst.name,"",1,-0.5,0.5)

    def analyze(self,event):
        for mWindow in self.mass_window_list:
            if mWindow.inWindow(event.Z2.vec.M()):
                self.writer.objs[mWindow.makeHistName()+"_"+self.dataset.parent.name].Fill(0.,event.weight)
        return True
