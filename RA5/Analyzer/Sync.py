from Core.Module import Module

class SyncPrinter(Module):
    def __init__(self,name,textFilePath,sort=True):
        super(SyncPrinter,self).__init__(name)
        self.textFilePath = textFilePath
        self.sort = sort
        if self.sort: self.sortList = []
        self.strTemplate = "%1d%9d%12d\t\n"
    
    def begin(self):
        self.textFile = open(self.textFilePath,"w")

    def analyze(self,event):
        if not self.sort:
            str_to_write = self.strTemplate%(
            #"%1d%9d%12d\t%5.3f\t%5.3f\t%5.3f\t%+2d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%1d\t%1d\t%1d\t%5.3f\t%5.3f\t%5.3f\t%+2d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%1d\t%1d\t%1d\t%5.3f\t%5.3f\n"%(
                event.run[0],
                event.lumi[0],
                event.evt[0],
                )
            self.textFile.write(str_to_write)
        else:
            self.sortList.append( (event.run[0],event.lumi[0],event.evt[0]) )
        return True

    def end(self):
        if self.sort:
            self.sortList.sort()
            for key in self.sortList:
                str_to_write = self.strTemplate%key
                self.textFile.write(str_to_write)        
        self.textFile.close()
