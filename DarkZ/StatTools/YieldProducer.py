from Core.Module import Module

class YieldProducer(Module):
    def __init__(self,name,mass_window_list,systList=[]):
        self.name = name
        self.mass_window_list = mass_window_list
        self.systList = systList
        self.channelNames = ["4mu","4e","2e2mu","comb"]

    def begin(self):
        for mWindow in self.mass_window_list:
            for channelName in self.channelNames:
                #histName = "_".join([mWindow.makeHistName(),self.dataset.parent.name,channelName,])
                histName = "_".join([mWindow.makeHistName(),channelName,])
                self.writer.book(histName,"TH1D",histName,"",1,-0.5,0.5)
                for syst in self.systList:
                    #sysHistName = "_".join([mWindow.makeHistName(),self.dataset.parent.name,channelName,syst.name])
                    sysHistName = "_".join([mWindow.makeHistName(),channelName,syst.name])
                    self.writer.book(sysHistName,"TH1D",sysHistName,"",1,-0.5,0.5)


    def analyze(self,event):
        for mWindow in self.mass_window_list:
            #if mWindow.inWindow(event.Z2.vec.M()):
            if mWindow.inWindow(event.massZ2[0]):
                #histName = "_".join([mWindow.makeHistName(),self.dataset.parent.name,"comb",])
                histName = "_".join([mWindow.makeHistName(),"comb",])
                self.writer.objs[histName].Fill(0.,event.weight)
                if event.mass4e[0] > 0.:
                    #histName = "_".join([mWindow.makeHistName(),self.dataset.parent.name,"4e",])
                    histName = "_".join([mWindow.makeHistName(),"4e",])
                    self.writer.objs[histName].Fill(0.,event.weight)
                elif event.mass4mu[0] > 0.:
                    #histName = "_".join([mWindow.makeHistName(),self.dataset.parent.name,"4mu",])
                    histName = "_".join([mWindow.makeHistName(),"4mu",])
                    self.writer.objs[histName].Fill(0.,event.weight)
                elif event.mass2e2mu[0] > 0.:
                    #histName = "_".join([mWindow.makeHistName(),self.dataset.parent.name,"2e2mu",])
                    histName = "_".join([mWindow.makeHistName(),"2e2mu",])
                    self.writer.objs[histName].Fill(0.,event.weight)
        return True