from Core.Module import Module
import ROOT as r
from ROOT import TLorentzVector 
import math as m
from Utils.DeltaR import deltaR
from random import choice

class ZSelector(Module):
    def __init__(self,name):
        super(ZSelector,self).__init__(name)

    def analyze(self,event):
	event.Lep1, event.Lep2, event.Lep3, event.Met = TLorentzVector(), TLorentzVector(), TLorentzVector(), TLorentzVector(),
        event.Met.SetPtEtaPhiM(event.met[0],0,event.met_phi[0],0)
        event.Lep_leading_fromM1, event.Lep_leading_fromM2 = TLorentzVector(), TLorentzVector(),
	# --------- Order leptons by pT. L1 and L2 are tight muons, L3 is loose. L1 and L2 already ordered by pT. --------
	if event.pTL3[0] > event.pTL1[0]:
		event.Lep1.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
		event.Lep2.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
		event.Lep3.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])

		Lep1id = event.idL3[0]
		Lep2id = event.idL1[0]
		Lep3id = event.idL2[0]

		event.Lep1Iso = event.IsoL3[0]
		event.Lep2Iso = event.IsoL1[0]
		event.Lep3Iso = event.IsoL2[0]
	elif event.pTL3[0] > event.pTL2[0] and event.pTL1[0] > event.pTL3[0]:
		event.Lep1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep2.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
                event.Lep3.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])

		Lep1id = event.idL1[0]
                Lep2id = event.idL3[0]
                Lep3id = event.idL2[0]

		event.Lep1Iso = event.IsoL1[0]
                event.Lep2Iso = event.IsoL3[0]
                event.Lep3Iso = event.IsoL2[0]
	elif event.pTL3[0] < event.pTL2[0]:
		event.Lep1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
                event.Lep2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
                event.Lep3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])

		Lep1id = event.idL1[0]
                Lep2id = event.idL2[0]
                Lep3id = event.idL3[0]

		event.Lep1Iso = event.IsoL1[0]
                event.Lep2Iso = event.IsoL2[0]
                event.Lep3Iso = event.IsoL3[0]
	# ----------------------------------------------------------------------------------------------------------------
	vec = event.Lep1 + event.Lep2 + event.Lep3 + event.Met
	v3l = event.Lep1 + event.Lep2 + event.Lep3
        event.mt = vec.Mt()
	event.m3l = v3l.M()
        totallep = event.Lep1 + event.Lep2 + event.Lep3

	# --------- Define Mass1 as the highest pT muon + highest pT anti-muon -------------------------------------------
	if Lep1id + Lep2id == 0:
		P1 = event.Lep1 + event.Lep2
		if Lep1id + Lep3id == 0: 
			P2 = event.Lep1 + event.Lep3
		else:
			P2 = event.Lep2 + event.Lep3
	elif Lep1id + Lep3id == 0:
		P1 = event.Lep1 + event.Lep3
		if Lep1id + Lep2id == 0:
			P2 = event.Lep1 + event.Lep2
		else:
			P2 = event.Lep2 + event.Lep3
	# ----------------------------------------------------------------------------------------------------------------

	# --------- Define Mass1 as two closet muons ---------------------------------------------------------------------
	#if Lep1id + Lep2id == 0:
	#	if Lep1id + Lep3id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi()) < deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
	#			P1 = event.Lep1 + event.Lep2
	#			P2 = event.Lep1 + event.Lep3
	#		else:
	#			P1 = event.Lep1 + event.Lep3
	#			P2 = event.Lep1 + event.Lep2
	#	elif Lep2id + Lep3id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi()) < deltaR(event.Lep2.Eta(),event.Lep2.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
	#			P1 = event.Lep1 + event.Lep2
	#			P2 = event.Lep2 + event.Lep3
	#		else:
	#			P1 = event.Lep2 + event.Lep3
	#			P2 = event.Lep1 + event.Lep2
	#elif Lep1id + Lep3id == 0:
	#	if Lep1id + Lep2id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi()) < deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
        #                        P1 = event.Lep1 + event.Lep2
        #                        P2 = event.Lep1 + event.Lep3
        #                else:
        #                        P1 = event.Lep1 + event.Lep3
        #                        P2 = event.Lep1 + event.Lep2
	#	elif Lep2id + Lep3id == 0:
	#		if deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi()) < deltaR(event.Lep2.Eta(),event.Lep2.Phi(),event.Lep3.Eta(),event.Lep3.Phi()):
        #                        P1 = event.Lep1 + event.Lep3
        #                        P2 = event.Lep2 + event.Lep3
        #                else:
        #                        P1 = event.Lep2 + event.Lep3
        #                        P2 = event.Lep1 + event.Lep3
	# ----------------------------------------------------------------------------------------------------------------

	event.mass1  = P1.M()
        event.mass2  = P2.M()
        event.mass1_pt = P1.Pt()
        event.mass2_pt = P2.Pt()
        event.mass1_eta = P1.Eta()
        event.mass2_eta = P2.Eta()
        event.mass1_coseta = m.cos(P1.Eta())
        event.mass2_coseta = m.cos(P2.Eta())
        event.mass1_phi = P1.Phi()
        event.mass2_phi = P2.Phi()

	event.dR12 = deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep2.Eta(),event.Lep2.Phi())
	event.dR13 = deltaR(event.Lep1.Eta(),event.Lep1.Phi(),event.Lep3.Eta(),event.Lep3.Phi())
	event.dR23 = deltaR(event.Lep2.Eta(),event.Lep2.Phi(),event.Lep3.Eta(),event.Lep3.Phi())

	#iMass = 60
	#if (iMass-1) < event.mass1 < (iMass+1):
	#	event.MCorrect = 1
	#elif (iMass-1) < event.mass2 < (iMass+1):
	#	event.MCorrect = 2
	#else:
	#	event.MCorrect = 0

	if 80 < event.mass1 < 100 or 80 < event.mass2 < 100:
            return False

	return True
