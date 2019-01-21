from Core.Module import Module
import os

class EventPrinter(Module):
    def __init__(self,name,textFileDir):
        """
        Print event list for each SR
        """
        super(EventPrinter,self).__init__(name)
        self.textFileDir = textFileDir
        self.strTemplate = "%1d\t%9d\t%12d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5d\t%5d\t%5d\t%5d\t%5.3f\t%5.3f\n"

    def analyze(self,event):
        key = (
                event.run[0],
                event.lumi[0],
                event.evt[0],
                event.firstLep.pt,
                event.secondLep.pt,
                event.firstLep.eta,
                event.secondLep.eta,
                event.firstLep.pdgId,
                event.secondLep.pdgId,
                int(event.nJetRA540[0]),
                int(event.nBJetMediumRA540[0]),
                event.met_pt[0],
                event.htJet40[0],
                #event.mtmin,
                )
        str_to_write = self.strTemplate%key
        if (event.cat.SRCat,event.cat.lepCat.Data()) not in self.writer.objs:
            self.writer.book(
                    (event.cat.SRCat,event.cat.lepCat.Data()),
                    "TextFile",
                    os.path.join(self.writer.outputDir,event.cat.lepCat.Data()+"_"+str(event.cat.SRCat)+".txt"),
                    "w",
                    )
            #self.writer.objs[(event.cat.SRCat,event.cat.lepCat.Data())] = open(os.path.join(self.textFileDir,event.cat.lepCat.Data()+"_"+str(event.cat.SRCat)+".txt"),"w")
        self.writer.objs[(event.cat.SRCat,event.cat.lepCat.Data())].write(str_to_write)
        return True
