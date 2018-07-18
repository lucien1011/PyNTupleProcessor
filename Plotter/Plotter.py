from Core.Module import Module
import copy

class Plotter(Module):
    def __init__(self,name,plotList):
        super(Plotter,self).__init__(name)
        self.plotList = plotList

    def begin(self):
        for plot in self.plotList:
            self.writer.book(*plot.getWriterSetting())
        self.plotList = [copy.deepcopy(plot) for plot in self.plotList]
        
    def analyze(self,event):
        for plot in self.plotList:
            if plot.selFunc and not plot.selFunc(event): continue
            values = plot.getValues(event)
            if not values: continue
            if not plot.isCollection and values[0] == None: continue
            for value in values:
                #self.writer.objs[plot.key].Fill(value,event.weight)
                try:
                    self.writer.objs[plot.key].Fill(value,event.weight)
                except TypeError:
                    raise RuntimeError, "Can't find "+plot.key+" in the tree"
        return True

    def end(self):
        super(Plotter,self).end()
        for plot in self.plotList:
            plot.end()
