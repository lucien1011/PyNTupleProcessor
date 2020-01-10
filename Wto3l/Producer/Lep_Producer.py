from Core.Module import Module
import ROOT as r
from ROOT import TLorentzVector 
import math as m
from Utils.DeltaR import deltaR

class Lep_Producer(Module):
    def __init__(self,name):
        super(Lep_Producer,self).__init__(name)

    def analyze(self,event):
        event.Lep1_fromZp, event.Lep2_fromZp, event.Lep1_notZp = TLorentzVector(), TLorentzVector(), TLorentzVector(),
        Q1, Q2 = TLorentzVector(), TLorentzVector(),
        lll1, lll2, lll3 = TLorentzVector(), TLorentzVector(), TLorentzVector(),
        event.Lep_leading_fromZp, event.Lep_subleading_fromZp, event.Lep_leading_notZp, event.Lep_subleading_notZp = TLorentzVector(), TLorentzVector(), TLorentzVector(), TLorentzVector(),
        lep_dR = 0
        notZp_lep_dR = 0
        totallep_thirdlep_dR = 0
        lll1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
        lll2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
        lll3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
        totalLep = TLorentzVector()
        totalLep = lll1 + lll2 + lll3
        #print event.MomIdL1[0],event.MomIdL2[0],event.MomIdL3[0],event.idL1[0],event.idL2[0],event.idL3[0]
        if event.MomIdL1[0] == 999888 and event.MomIdL2[0] == 999888 and event.MomIdL3[0] != 999888:
            if event.pTL1[0] > event.pTL2[0]:
                event.Lep1_notZp.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep1_fromZp.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep2_fromZp.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                if event.idL1[0] < 0 and event.idL3[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL1[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL2[0] < 0 and event.idL3[0] > 0: 
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL2[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())

                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
            else:
                event.Lep1_notZp.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep2_fromZp.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep1_fromZp.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                if event.idL1[0] < 0 and event.idL3[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())

                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL1[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())

                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL2[0] < 0 and event.idL3[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL2[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp

        if event.MomIdL1[0] == 999888 and event.MomIdL3[0] == 999888 and event.MomIdL2[0] != 999888:
            if event.pTL1[0] > event.pTL3[0]:
                event.Lep2_fromZp.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep1_fromZp.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep1_notZp.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                if event.idL1[0] < 0 and event.idL2[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL1[0] > 0 and event.idL2[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL2[0] < 0 and event.idL3[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL2[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
            else:
                event.Lep1_fromZp.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep2_fromZp.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep1_notZp.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                if (event.idL1[0] < 0 and event.idL2[0] > 0) or ():
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL1[0] > 0 and event.idL2[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL2[0] < 0 and event.idL3[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL2[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp

        if event.MomIdL2[0] == 999888 and event.MomIdL3[0] == 999888 and event.MomIdL1[0] != 999888:
            if event.pTL2[0] > event.pTL3[0]:
                event.Lep2_fromZp.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep1_notZp.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep1_fromZp.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                if event.idL1[0] < 0 and event.idL2[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL1[0] > 0 and event.idL2[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL1[0] < 0 and event.idL3[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL1[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
            else:
                event.Lep1_fromZp.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep1_notZp.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep2_fromZp.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                if event.idL1[0] < 0 and event.idL2[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL1[0] > 0 and event.idL2[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep2_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    if event.Lep2_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep2_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep2_fromZp
                elif event.idL1[0] < 0 and event.idL3[0] > 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                elif event.idL1[0] > 0 and event.idL3[0] < 0:
                    Q1 = event.Lep1_notZp + event.Lep1_fromZp
                    lep_dR = deltaR(event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi(),event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi())
                    notZp_lep_dR = deltaR(Q1.Eta(), Q1.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    totallep_thirdlep_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
                    if event.Lep1_fromZp.Pt() > event.Lep1_notZp.Pt():
                        event.Lep_leading_notZp = event.Lep1_fromZp
                        event.Lep_subleading_notZp = event.Lep1_notZp
                    else:
                        event.Lep_leading_notZp = event.Lep1_notZp
                        event.Lep_subleading_notZp = event.Lep1_fromZp
                    
        Q2 = event.Lep1_fromZp + event.Lep2_fromZp
        event.Lep_leading_fromZp = event.Lep1_fromZp
        event.Lep_subleading_fromZp = event.Lep2_fromZp

        event.Zp_lep_deltaR = deltaR(event.Lep1_fromZp.Eta(), event.Lep1_fromZp.Phi(),event.Lep2_fromZp.Eta(), event.Lep2_fromZp.Phi())
        event.notZp_lep_deltaR = lep_dR
        event.notZp_mass = Q1.M()
        event.Zp_mass = Q2.M()
        event.notZp_eta = Q1.Eta()
        event.Zp_eta = Q2.Eta()
        event.notZp_phi = Q1.Phi()
        event.Zp_phi = Q2.Phi()
        event.notZp_pt = Q1.Pt()
        event.Zp_pt = Q2.Pt()
        event.Zp_lepnotfromZp_dR = deltaR(Q2.Eta(), Q2.Phi(), event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi())
        event.notZp_otherlep_dR = notZp_lep_dR
        event.totalLep_thirdLep_Zp_dR = deltaR(totalLep.Eta(), totalLep.Phi(), event.Lep1_notZp.Eta(), event.Lep1_notZp.Phi())
        event.totalLep_thirdLep_notZp_dR = totallep_thirdlep_dR
        return True
