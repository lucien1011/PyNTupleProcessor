from Core.Module import Module

class SyncPrinter(Module):
    def __init__(self,name,textFilePath,sort=True):
        super(SyncPrinter,self).__init__(name)
        self.textFilePath = textFilePath
        self.sort = sort
        if self.sort: self.sortList = []
        self.strTemplate = "%1d%9d%12d\t%+2d %5.1f\t%+2d %5.1f\t\n"
    
    def begin(self):
        self.textFile = open(self.textFilePath,"w")

    def analyze(self,event):
        key = (
                event.run[0],
                event.lumi[0],
                event.evt[0],
                event.tightLeps[0].pdgId,
                event.tightLeps[0].pt,
                event.tightLeps[1].pdgId,
                event.tightLeps[1].pt,
                )
        if not self.sort:
            #"%1d%9d%12d\t%5.3f\t%5.3f\t%5.3f\t%+2d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%1d\t%1d\t%1d\t%5.3f\t%5.3f\t%5.3f\t%+2d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%1d\t%1d\t%1d\t%5.3f\t%5.3f\n"%(
            str_to_write = self.strTemplate%key
            self.textFile.write(str_to_write)
        else:
            self.sortList.append( key )
        return True

    def end(self):
        if self.sort:
            self.sortList.sort()
            for key in self.sortList:
                str_to_write = self.strTemplate%key
                self.textFile.write(str_to_write)        
        self.textFile.close()
