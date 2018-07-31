from Core.Module import Module
from Core.Collection import Collection

import ROOT

class Category(object):
    def __init__(self):
        pass

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
        
        veclep1 = event.tightLeps[0].p4()
        veclep2 = event.tightLeps[1].p4()
        met_pt = event.met_pt[0]
        met_phi = event.met_phi[0]
        met = ROOT.TLorentzVector() 
        met.SetPtEtaPhiM(met_pt,0,met_phi,0)
        met.SetPz(0)
        met.SetE(met.Pt())
        mt1 = (veclep1 + met).Mt()
        mt2 = (veclep2 + met).Mt()
        if mt1 < mt2:
            mt = mt1
        else:
            mt = mt2              
        event.cat.jetCat = "0"
        #print(event.cat.lepCat, event.htJet40[0], event.nJet40_recal, event.met_pt[0], event.LepGood_charge[0])
        if event.cat.lepCat == "HH":
            if event.htJet40[0] >= 1125 and event.htJet40[0] <= 1300 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.LepGood_charge[0] > 0:
                    event.cat.jetCat = "SR46"
                elif event.LepGood_charge[0] < 0:
                    event.cat.jetCat = "SR47"
            elif event.htJet40[0] >= 1300 and event.htJet40[0] <= 1600 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.LepGood_charge[0] > 0:
                    event.cat.jetCat = "SR48"
                elif event.LepGood_charge[0] < 0:
                    event.cat.jetCat = "SR49"
            elif event.htJet40[0] > 1600 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.LepGood_charge[0] > 0:
                    event.cat.jetCat = "SR50"
                elif event.LepGood_charge[0] < 0:
                    event.cat.jetCat = "SR51"

            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                event.cat.jetCat = "SR42"
            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
                event.cat.jetCat = "SR43"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                event.cat.jetCat = "SR44"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
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
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR5"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR6"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR7"
                elif event.htJet40[0] < 300:
                    event.cat.jetCat = "SR3"
                elif event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.LepGood_charge[0] > 0:
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
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR13"
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR14"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR15"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR16"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR13"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR14"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR17"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR18"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR19"
                elif event.htJet40[0] < 300:
                    if event.LepGood_charge[0] > 0:
                        event.cat.jetCat = "SR13"
                    else:
                        event.cat.jetCat = "SR14"
                elif event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.LepGood_charge[0] > 0:
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
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR25"
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR26"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR27"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR28"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR25"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR26"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR29"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR30"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR31"
                elif event.htJet40[0] < 300:
                    if event.LepGood_charge[0] > 0:
                        event.cat.jetCat = "SR25"
                    else:
                        event.cat.jetCat = "SR26"
                elif event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2:
                            if event.LepGood_charge[0] > 0:
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
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR35"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR36"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR37"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR38"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR35"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR36"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR39"
                else:
                    if event.met_pt[0] > 50:
                        if event.htJet40[0] < 300:
                            event.cat.jetCat = "SR40"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR41"

        if event.cat.lepCat == "HL":
            if event.htJet40[0] >= 1125 and event.htJet40[0] <= 1300 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.LepGood_charge[0] > 0:
                    event.cat.jetCat = "SR38"
                elif event.LepGood_charge[0] < 0:
                    event.cat.jetCat = "SR39"
            elif event.htJet40[0] >= 1300 and event.htJet40[0] <= 1600 and event.nJet40_recal >= 2 and event.met_pt[0] >= 50 and event.met_pt[0] <= 300:
                if event.LepGood_charge[0] > 0:
                    event.cat.jetCat = "SR40"
                elif event.LepGood_charge[0] < 0:
                    event.cat.jetCat = "SR41"
            
            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                event.cat.jetCat = "SR34"
            if event.met_pt[0] >= 300 and event.met_pt[0] <= 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
                event.cat.jetCat = "SR35"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                event.cat.jetCat = "SR36"
            if event.met_pt[0] > 500 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
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
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR5"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
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
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR10"
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR11"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR12"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR13"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR10"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR11"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR14"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR16"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
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
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR20"
                            if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR21"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] > 0:
                                event.cat.jetCat = "SR22"
                            if event.htJet40[0] <= 1125 and event.htJet40[0] >= 300 and event.LepGood_charge[0] < 0:
                                event.cat.jetCat = "SR23"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR20"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR21"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR24"
                        if event.nJet40_recal <= 4 and event.nJet40_recal >= 2 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR25"
                        if event.nJet40_recal >= 5 and event.htJet40[0] >= 300 and event.htJet40[0] <= 1125:
                            event.cat.jetCat = "SR26"
            if event.nJet25 >= 3 and event.nJet40_recal >= 2:
                if mt < 120:
                    if event.met_pt[0] < 200 and event.met_pt[0] > 50:
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR27"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR28"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR29"
                        if event.htJet40[0] >= 300 and event.htJet40[0] <= 1125 and event.LepGood_charge[0] < 0:
                            event.cat.jetCat = "SR30"
                    elif event.met_pt[0] < 300 and event.met_pt[0] > 200:
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] > 0:
                            event.cat.jetCat = "SR27"
                        if event.htJet40[0] < 300 and event.LepGood_charge[0] < 0:
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
