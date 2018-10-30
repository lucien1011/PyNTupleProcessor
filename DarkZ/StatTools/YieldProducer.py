from Core.Module import Module

class YieldProducer(Module):
    def __init__(self,name,mass_window_list,systList=[]):
        self.name = name
        self.mass_window_list = mass_window_list
        self.systList = systList
        #self.channelNames = ["4mu","4e","2e2mu","comb"]
        self.channelNames = ["4mu","4e","2e2mu","2mu2e","comb"]

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
        for multi_mWindow in self.mass_window_list:
            for mWindow in multi_mWindow:
                if not mWindow.selection(event): continue
                if mWindow.inWindow(event.massZ2[0]):
                    histName = "_".join([multi_mWindow.makeHistName(),"comb",])
                    self.writer.objs[histName].Fill(0.,event.weight)
                    
                    channelName = mWindow.name

                    histName = "_".join([multi_mWindow.makeHistName(),channelName,])
                    self.writer.objs[histName].Fill(0.,event.weight)

                    for syst in self.systList:
                        sysHistName = "_".join([multi_mWindow.makeHistName(),"comb",syst.name])
                        self.writer.objs[sysHistName].Fill(0.,event.weight*syst.factorFunc(event))

                        sysHistName = "_".join([multi_mWindow.makeHistName(),channelName,syst.name])
                        self.writer.objs[sysHistName].Fill(0.,event.weight*syst.factorFunc(event))
        return True

    def end(self):
        for syst in self.systList:
            syst.factorFunc.end()
        
        for multi_mWindow in self.mass_window_list:
            multi_mWindow.end()
