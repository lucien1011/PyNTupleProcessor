from Core.Module import Module
from Core.Collection import Collection

from Utils.MiscVar import mtFunc

import ROOT

class Category(object):
    def __init__(self):
        pass

class SRCatProducer(object):
    def __init__(self):
        self.posCharges = [+1.,+1.]
        self.negCharges = [-1.,-1.]

    def getSRStr(self,number):
        return "SR"+number

    def getSRCat(self,nj,nb,ht,met,mt,lepCat,charges):
        if lepCat == "HH":
            return self.getSRCatHH(nj,nb,ht,met,mt,charges)
        elif lepCat == "HL":
            return self.getSRCatHL(nj,nb,ht,met,mt,charges)
        elif lepCat == "LL":
            return self.getSRCatLL(nj,nb,ht,met,mt,charges)

    def getSRCatHH(self,nj,nb,ht,met,mt,charges):
        if met < 50.:
            if ht > 1125. and ht < 1300.:
                return self.getSRStr("61")
            elif ht > 1300. and ht < 1600.:
                return self.getSRStr("62")
            elif ht > 1600:
                return self.getSRStr("63")
            elif ht > 300. and ht < 1125.:
                if nb == 0:
                    if nj >= 2 and nj <= 4:
                        return self.getSRStr("51")
                    elif nj >= 5:
                        return self.getSRStr("52")
                elif nb == 1:
                    if nj >= 2 and nj <= 4:
                        return self.getSRStr("53")
                    elif nj >= 5:
                        return self.getSRStr("54")
                elif nb == 2:
                    if nj >= 2 and nj <= 4:
                        return self.getSRStr("55")
                    elif nj >= 5:
                        return self.getSRStr("56")
                elif nb >= 3:
                    if nj >= 2 and nj <= 4:
                        return self.getSRStr("57")
                    elif nj >= 5:
                        return self.getSRStr("58")
            elif ht < 300.:
                    if nj >= 2 and nj <= 4:
                        return self.getSRStr("59")
                    elif nj >= 5:
                        return self.getSRStr("60")
        if met < 300.:
            if ht > 1125. and ht < 1300.:
                if charges == self.posCharges: return self.getSRStr("46") 
                if charges == self.negCharges: return self.getSRStr("47") 
            elif ht > 1300. and ht < 1600.:
                if charges == self.posCharges: return self.getSRStr("48") 
                if charges == self.negCharges: return self.getSRStr("49") 
            elif ht > 1600:
                if charges == self.posCharges: return self.getSRStr("50") 
                if charges == self.negCharges: return self.getSRStr("51")
            elif ht > 300. and ht < 1125.:
                if nb == 0:
                    if nj >= 2 and nj <= 4 and mt < 120. and met > 50. and met < 200.:
                        return self.getSRStr("2")
                    elif nj >= 5 and mt < 120. and met > 50. and met < 200.:
                        return self.getSRStr("4")
                    elif nj >= 2 and nj <= 4 and mt < 120. and met > 200. and met < 300.:
                        if charges == self.posCharges: return self.getSRStr("5") 
                        if charges == self.negCharges: return self.getSRStr("6")
                    elif nj >= 5 and mt < 120. and met > 200. and met < 300.:
                        return self.getSRStr("7")
                    elif nj >= 2 and nj <= 4 and mt > 120. and met > 50. and met < 200.:
                        if charges == self.posCharges: return self.getSRStr("8") 
                        if charges == self.negCharges: return self.getSRStr("9")
                    else:
                        return self.getSRStr("10")
                elif nb == 1:
                    if nj >= 2 and nj <= 4 and mt < 120. and met > 50. and met < 200.:
                        return self.getSRStr("12")
                    elif nj >= 5 and mt < 120. and met > 50. and met < 200.:
                        if charges == self.posCharges: return self.getSRStr("15") 
                        if charges == self.negCharges: return self.getSRStr("16")
                    elif nj >= 2 and nj <= 4 and mt < 120. and met > 200. and met < 300.:
                        if charges == self.posCharges: return self.getSRStr("17") 
                        if charges == self.negCharges: return self.getSRStr("18")
                    elif nj >= 5 and mt < 120. and met > 200. and met < 300.:
                        return self.getSRStr("19")
                    elif nj >= 2 and nj <= 4 and mt > 120. and met > 50. and met < 200.:
                        if charges == self.posCharges: return self.getSRStr("20") 
                        if charges == self.negCharges: return self.getSRStr("21")
                    else:
                        return self.getSRStr("22")
                elif nb == 2:
                    if nj >= 2 and nj <= 4 and mt < 120. and met > 50. and met < 200.:
                        return self.getSRStr("24")
                    elif nj >= 5 and mt < 120. and met > 50. and met < 200.:
                        if charges == self.posCharges: return self.getSRStr("27") 
                        if charges == self.negCharges: return self.getSRStr("28")
                    elif nj >= 2 and nj <= 4 and mt > 120. and met > 200. and met < 300.:
                        if charges == self.posCharges: return self.getSRStr("29") 
                        if charges == self.negCharges: return self.getSRStr("30")
                    elif nj >= 5 and mt < 120. and met > 200. and met < 300.:
                        return self.getSRStr("31")
                    elif nj >= 2 and nj <= 4 and mt < 120. and met > 50. and met < 200.:
                        if charges == self.posCharges: return self.getSRStr("32") 
                        if charges == self.negCharges: return self.getSRStr("33")
                    else:
                        return self.getSRStr("34")
                elif nb >= 3:
                    if mt < 120.:
                        if met > 50. and met < 200.:
                            if charges == self.posCharges: return self.getSRStr("37") 
                            if charges == self.negCharges: return self.getSRStr("38")
                        elif met > 200. and met < 300.:
                            return self.getSRStr("39")
                    else:
                            return self.getSRStr("41")
            elif ht < 300.:
                if nb == 0:
                    if nj >= 2 and nj <= 4 and mt < 120. and met > 50. and met < 200.:
                        return self.getSRStr("1")
                    else:
                        return self.getSRStr("3")
                elif nb == 1:
                    if nj >= 2 and nj <= 4 and mt < 120. and met > 50. and met < 200.:
                        return self.getSRStr("11")
                    else:
                        if charges == self.posCharges: return self.getSRStr("13") 
                        if charges == self.negCharges: return self.getSRStr("14")
                elif nb == 2:
                    if nj >= 2 and nj <= 4 and mt < 120. and met > 50. and met < 200.:
                        return self.getSRStr("23")
                    else:
                        if charges == self.posCharges: return self.getSRStr("25") 
                        if charges == self.negCharges: return self.getSRStr("26")
                elif nb >= 3:
                    if mt < 120.:
                        if charges == self.posCharges: return self.getSRStr("35") 
                        if charges == self.negCharges: return self.getSRStr("36")
                    else:
                        return self.getSRStr("40")
        elif met > 300. and met < 500.:
                if charges == self.posCharges: return self.getSRStr("42") 
                if charges == self.negCharges: return self.getSRStr("43")
        elif met > 500.:
                if charges == self.posCharges: return self.getSRStr("44") 
                if charges == self.negCharges: return self.getSRStr("45")

    def getSRCatLL(self,nj,nb,ht,met,mt,charges):
        return self.getSRStr("1")

    def getSRCatHL(self,nj,nb,ht,met,mt,charges):
        return self.getSRStr("1")

class LeptonCatProducer(Module):
    def __init__(self,name):
        super(LeptonCatProducer,self).__init__(name)
        self.SRCatProducer =  SRCatProducer()

    def analyze(self,event):
        event.tightLeps.sort(key=lambda x: x.pt,reverse=True)
        event.cat = Category()

        #print [l.pt for l in event.tightLeps]
        #print [l.charge for l in event.tightLeps]
        firstLep = event.tightLeps[0]
        for l in event.tightLeps[1:]:
            if l.charge*event.tightLeps[0].charge > 0.:
                secondLep = l
        if firstLep.pt > 25 and secondLep.pt > 25: event.cat.lepCat = "HH"
        if firstLep.pt > 25 and secondLep.pt < 25: event.cat.lepCat = "HL"
        if firstLep.pt < 25 and secondLep.pt < 25: event.cat.lepCat = "LL"

        mt = min([mtFunc(firstLep.pt,firstLep.phi,event.met_pt[0],event.met_phi[0]),mtFunc(secondLep.pt,secondLep.phi,event.met_pt[0],event.met_phi[0]),])
        event.mtmin = mt
        
        event.cat.SRCat = self.SRCatProducer.getSRCat(event.nJetRA540[0],event.nBJetMediumRA525[0],event.htJet40[0],event.met_pt[0],event.mtmin,event.cat.lepCat,[firstLep.charge,secondLep.charge])

        event.firstLep = firstLep
        event.secondLep = secondLep

        return True

class CategoryProducer(Module):
    def analyze(self,event):
        event.goodLeps = Collection(event,"LepGood")
        event.tightLeps = [l for l in event.goodLeps if l.isTight]
        event.tightLeps.sort(key=lambda x: x.pt,reverse=True)
        if len(event.tightLeps) != 2: return False
        event.cat = Category()
        if event.tightLeps[0].pt > 25 and event.tightLeps[1].pt > 25: event.cat.lepCat = "HH"
        if event.tightLeps[0].pt > 25 and event.tightLeps[1].pt < 25: event.cat.lepCat = "HL"
        if event.tightLeps[0].pt < 25 and event.tightLeps[1].pt < 25: event.cat.lepCat = "LL"

        mt = min([mtFunc(event.tightLeps[0].pt,event.tightLeps[0].phi,event.met_pt[0],event.met_phi[0]),mtFunc(event.tightLeps[1].pt,event.tightLeps[1].phi,event.met_pt[0],event.met_phi[0]),])

        #veclep1 = event.tightLeps[0].p4()
        #veclep2 = event.tightLeps[1].p4()
        #met_pt = event.met_pt[0]
        #met_phi = event.met_phi[0]
        #met = ROOT.TLorentzVector() 
        #met.SetPtEtaPhiM(met_pt,0,met_phi,0)
        #met.SetPz(0)
        #met.SetE(met.Pt())
        #mt1 = (veclep1 + met).Mt()
        #mt2 = (veclep2 + met).Mt()
        #mt = min([mt1,mt2])
        event.mtmin = mt
        event.cat.jetCat = "0"
        #print(event.cat.lepCat, event.nJet25[0], mt, event.met_pt[0], event.nJet40_recal, event.htJet40[0], event.tightLeps[0].charge, event.tightLeps[1].charge)
        if event.cat.lepCat == "HH":
            if event.htJet40[0] >= 1125 and event.htJet40[0] <= 1300 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.tightLeps[0].charge > 0:
                    event.cat.jetCat = "SR46"
                elif event.tightLeps[0].charge < 0:
                    event.cat.jetCat = "SR47"
            elif event.htJet40[0] >= 1300 and event.htJet40[0] <= 1600 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.tightLeps[0].charge > 0:
                    event.cat.jetCat = "SR48"
                elif event.tightLeps[0].charge < 0:
                    event.cat.jetCat = "SR49"
            elif event.htJet40[0] > 1600 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.tightLeps[0].charge > 0:
                    event.cat.jetCat = "SR50"
                elif event.tightLeps[0].charge < 0:
                    event.cat.jetCat = "SR51"

            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                event.cat.jetCat = "SR42"
            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                event.cat.jetCat = "SR43"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                event.cat.jetCat = "SR44"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                event.cat.jetCat = "SR45"

            if event.nJet25 == 0:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR1"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR2"
                        elif event.nJet40_recal >= 5:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR3"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR4"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300:
                            event.cat.jetCat = "SR3"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR5"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR6"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR7"
                elif event.htJet40[0] < 300:
                    event.cat.jetCat = "SR3"
                elif event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR8"
                            else:
                                event.cat.jetCat = "SR9"
                        elif event.nJet40_recal >= 5:
                            event.cat.jetCat = "SR10"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        event.cat.jetCat = "SR10"
            elif event.nJet25 == 1:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR11"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR12"
                        elif event.nJet40_recal >= 5:
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR13"
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR14"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR15"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR16"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR13"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR14"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR17"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR18"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR19"
                elif event.htJet40[0] < 300:
                    if event.tightLeps[0].charge > 0:
                        event.cat.jetCat = "SR13"
                    else:
                        event.cat.jetCat = "SR14"
                elif event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR20"
                            else:
                                event.cat.jetCat = "SR21"
                        elif event.nJet40_recal >= 5:
                            event.cat.jetCat = "SR22"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        event.cat.jetCat = "SR22"
            elif event.nJet25 == 2:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR23"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR24"
                        elif event.nJet40_recal >= 5:
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR25"
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR26"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR27"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR28"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR25"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR26"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR29"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR30"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR31"
                elif event.htJet40[0] < 300:
                    if event.tightLeps[0].charge > 0:
                        event.cat.jetCat = "SR25"
                    else:
                        event.cat.jetCat = "SR26"
                elif event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR32"
                            else:
                                event.cat.jetCat = "SR33"
                        elif event.nJet40_recal >= 5:
                            event.cat.jetCat = "SR34"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        event.cat.jetCat = "SR34"
            if event.nJet25 >= 3 and event.nJet40_recal >= 2:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR35"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR36"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR37"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR38"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR35"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR36"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR39"
                else:
                    if event.met_pt[0] > 50 and event.met_pt[0] < 300:
                        if event.htJet40[0] < 300:
                            event.cat.jetCat = "SR40"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR41"

        if event.cat.lepCat == "HL":
            if event.htJet40[0] >= 1125 and event.htJet40[0] <= 1300 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.tightLeps[0].charge > 0:
                    event.cat.jetCat = "SR38"
                elif event.tightLeps[0].charge < 0:
                    event.cat.jetCat = "SR39"
            elif event.htJet40[0] >= 1300 and event.htJet40[0] <= 1600 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.tightLeps[0].charge > 0:
                    event.cat.jetCat = "SR40"
                elif event.tightLeps[0].charge < 0:
                    event.cat.jetCat = "SR41"
            
            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                event.cat.jetCat = "SR34"
            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                event.cat.jetCat = "SR35"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                event.cat.jetCat = "SR36"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                event.cat.jetCat = "SR37"
            if mt > 120 and event.met_pt[0] <= 300 and event.met_pt[0] >= 50 and event.nJet40_recal >= 2 and event.htJet40[0] < 300:
                event.cat.jetCat = "SR32"
            if mt > 120 and event.met_pt[0] <= 300 and event.met_pt[0] >= 50 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                event.cat.jetCat = "SR33"

            if event.nJet25 == 0:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR1"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR2"
                        elif event.nJet40_recal >= 5:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR3"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR4"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300:
                            event.cat.jetCat = "SR3"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR5"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR6"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR7"
            elif event.nJet25 == 1:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR8"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR9"
                        elif event.nJet40_recal >= 5:
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR10"
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR11"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR12"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR13"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR10"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR11"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR14"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR16"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR17"
            elif event.nJet25 == 2:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.htJet40[0] < 300:
                                event.cat.jetCat = "SR18"
                            elif event.htJet40[0] <= 1125:
                                event.cat.jetCat = "SR19"
                        elif event.nJet40_recal >= 5:
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR20"
                            if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR21"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge > 0:
                                event.cat.jetCat = "SR22"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.tightLeps[0].charge < 0:
                                event.cat.jetCat = "SR23"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR20"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR21"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR24"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR25"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR26"
            if event.nJet25 >= 3 and event.nJet40_recal >= 2:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR27"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR28"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR29"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR30"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge > 0:
                            event.cat.jetCat = "SR27"
                        if event.htJet40[0] < 300 and event.tightLeps[0].charge < 0:
                            event.cat.jetCat = "SR28"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR31"

        if event.cat.lepCat == "LL":
            if event.nJet40_recal >= 2 and event.htJet40[0] > 300:
                if mt > 120 and event.met_pt[0] >= 50:
                    event.cat.jetCat = "SR8"
                if event.nJet25 >= 3 and mt < 120 and event.met_pt[0] >= 50:
                    event.cat.jetCat = "SR7"
                if event.nJet25 == 0 and mt < 120 and event.met_pt[0] >= 50 and event.met_pt[0] <= 200:
                    event.cat.jetCat = "SR1"
                if event.nJet25 == 0 and mt < 120 and event.met_pt[0] >= 200:
                    event.cat.jetCat = "SR2"
                if event.nJet25 == 1 and mt < 120 and event.met_pt[0] >= 50 and event.met_pt[0] <= 200:
                    event.cat.jetCat = "SR3"
                if event.nJet25 == 1 and mt < 120 and event.met_pt[0] >= 200:
                    event.cat.jetCat = "SR4"
                if event.nJet25 == 2 and mt < 120 and event.met_pt[0] >= 50 and event.met_pt[0] <= 200:
                    event.cat.jetCat = "SR5"
                if event.nJet25 == 2 and mt < 120 and event.met_pt[0] >= 200:
                    event.cat.jetCat = "SR6"
        #print(event.cat.jetCat)
        #event.cat.lepCat.__dict__
        return True
