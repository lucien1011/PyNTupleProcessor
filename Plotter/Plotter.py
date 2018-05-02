from Core.Module import Module

class Plotter(Module):
    def __init__(self,name,plotList):
        super(Plotter,self).__init__(name)
        self.plotList = plotList

    def begin(self):
        for plot in self.plotList:
            self.writer.book(*plot.getWriterSetting())
        
    def analyze(self,event):
        for plot in self.plotList:
            if plot.selFunc and not plot.selFunc(event): continue
            for value in plot.getValues(event):
                self.writer.objs[plot.key].Fill(value,event.weight) 
        return True

    def end(self):
        super(Plotter,self).end()
        for plot in self.plotList:
            plot.end()
