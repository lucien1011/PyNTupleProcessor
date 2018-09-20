from Core.Module import Module

class LeptonSyncPrinter(Module):
    def __init__(self,name,textFilePath,sort=True):
        super(LeptonSyncPrinter,self).__init__(name)
        self.textFilePath = textFilePath
        self.sort = sort
        if self.sort: self.sortList = []
        #self.strTemplate = "%1d%9d%12d\t%+2d %5.1f\t%+2d %5.1f\t\n"
        self.strTemplate = "%1d%9d%12d\t%5.3f\t%5.3f\t%5.3f\t%+2d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%1d\t%1d\t%1d\t%5.3f\t%5.3f\t%5.3f\t%+2d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%1d\t%1d\t%1d\t%5.3f\t%5.3f\n"
    
    def begin(self):
        self.textFile = open(self.textFilePath,"w")

    def analyze(self,event):
        key = (
                event.run[0],
                event.lumi[0],
                event.evt[0],
                event.tightLeps[0].pt,
                event.tightLeps[0].eta,
                event.tightLeps[0].phi,
                event.tightLeps[0].pdgId,
                event.tightLeps[0].conePt,
                event.tightLeps[0].dxy,
                event.tightLeps[0].dz,
                event.tightLeps[0].sip3d,
                event.tightLeps[0].miniRelIso,
                #event.tightLeps[0].jetPtRatiov1,
                event.tightLeps[0].jetPtRatiov2,
                #event.tightLeps[0].jetPtRelv1,
                event.tightLeps[0].jetPtRelv2,
                event.tightLeps[0].mvaIdSpring15 if abs(event.tightLeps[0].pdgId) == 11 else 0,
                event.tightLeps[0].convVeto if abs(event.tightLeps[0].pdgId) == 11 else 0,
                event.tightLeps[0].mcMatchPdgId,
                event.tightLeps[0].mcMatchPdgId,
                event.tightLeps[0].mcMatchPdgId,

                event.tightLeps[1].pt,
                event.tightLeps[1].eta,
                event.tightLeps[1].phi,
                event.tightLeps[1].pdgId,
                event.tightLeps[1].conePt,
                event.tightLeps[1].dxy,
                event.tightLeps[1].dz,
                event.tightLeps[1].sip3d,
                event.tightLeps[1].miniRelIso,
                event.tightLeps[1].jetPtRatiov1,
                #event.tightLeps[1].jetPtRatiov2,
                event.tightLeps[1].jetPtRelv1,
                #event.tightLeps[1].jetPtRelv2,
                event.tightLeps[1].mvaIdSpring15 if abs(event.tightLeps[0].pdgId) == 11 else 0,
                event.tightLeps[1].convVeto if abs(event.tightLeps[0].pdgId) == 11 else 0,
                event.tightLeps[1].mcMatchPdgId,
                event.tightLeps[1].mcMatchPdgId,
                event.tightLeps[1].mcMatchPdgId,

                event.tightLeps[0].trackIso,
                event.tightLeps[1].trackIso,
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

#      //     textfile_jets << Form("%1d%9d%12d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\n",
#      //         ss::run(), ss::lumi(), (int)ss::event(),
#      //         ss::jet_pt().at(idx_l),
#      //         ss::jets().at(idx_l).eta(),
#      //         ss::jets().at(idx_l).phi(),
#      //         ss::jets_disc_ivf().at(idx_l), // "jet1_btagCSVmva"
#      //         ss::jets_disc_ivf().at(idx_l) > 0.800, // "jet1_btagCSVMedium". medium WP
#      //         ss::jet_pt().at(idx_t),
#      //         ss::jets().at(idx_t).eta(),
#      //         ss::jets().at(idx_t).phi(),
#      //         ss::jets_disc_ivf().at(idx_t),
#      //         ss::jets_disc_ivf().at(idx_t) > 0.800
#      //         );
class JetSyncPrinter(Module):
    def __init__(self,name,textFilePath,sort=True):
        super(JetSyncPrinter,self).__init__(name)
        self.textFilePath = textFilePath
        self.sort = sort
        if self.sort: self.sortList = []
        #self.strTemplate = "%1d%9d%12d\t%+2d %5.1f\t%+2d %5.1f\t\n"
        self.strTemplate = "%1d%9d%12d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\t%5.3f\t%5.3f\t%5.3f\t%5.3f\t%1d\n"
    
    def begin(self):
        self.textFile = open(self.textFilePath,"w")

    def analyze(self,event):
        key = (
                event.run[0],
                event.lumi[0],
                event.evt[0],
                event.selJets[0].pt,
                event.selJets[0].eta,
                event.selJets[0].phi,
                event.selJets[0].btagCSV,
                event.selJets[0].btagCSV > 0.800,
                event.selJets[1].pt,
                event.selJets[1].eta,
                event.selJets[1].phi,
                event.selJets[1].btagCSV,
                event.selJets[1].btagCSV > 0.800,
                )
        if not self.sort:
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
