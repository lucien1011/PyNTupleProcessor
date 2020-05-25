from Core.Module import Module
from Utils.DeltaR import deltaR,deltaPhi

import ROOT

muonMass = 0.

class VariableProducer(Module):
    def begin(self):
        ROOT.gSystem.Load("Library/computeAngles_cc.so")

    def analyze(self,event):
        event.deltaRL12 = deltaR(event.etaL1[0],event.phiL1[0],event.etaL2[0],event.phiL2[0])
        event.vecL1 = ROOT.TLorentzVector()
        event.vecL1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],muonMass)

        event.vecL2 = ROOT.TLorentzVector()
        event.vecL2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],muonMass)
        
        event.vecL3 = ROOT.TLorentzVector()
        event.vecL3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],muonMass)
        
        event.vecL4 = ROOT.TLorentzVector()
        event.vecL4.SetPtEtaPhiM(event.pTL4[0],event.etaL4[0],event.phiL4[0],muonMass)

        event.vecZ1 = event.vecL1 + event.vecL2
        event.vecZ2 = event.vecL3 + event.vecL4

        event.phiL21 = deltaPhi(event.phiL2[0],event.phiL1[0])
        event.phiL31 = deltaPhi(event.phiL3[0],event.phiL1[0])
        event.phiL41 = deltaPhi(event.phiL4[0],event.phiL1[0])

        event.cosThetaStar = ROOT.Double(0.)
        event.cosTheta1 = ROOT.Double(0.)
        event.cosTheta2 = ROOT.Double(0.)
        event.phi = ROOT.Double(0.)
        event.phi1 = ROOT.Double(0.)

        ROOT.computeAngles(
                event.vecL1,event.idL1[0],
                event.vecL2,event.idL2[0],
                event.vecL3,event.idL3[0],
                event.vecL4,event.idL4[0],
                event.cosThetaStar,
                event.cosTheta1,
                event.cosTheta2,
                event.phi,
                event.phi1,
                )

        return True
