from Core.Module import Module

import ROOT

class Lepton(object):
    def __init__(self,index,vec,vecnofsr):
        self.index = index
        self.vec = vec
        self.vecnofsr = vecnofsr

class ZCandidate(object):
    def __init__(self,vec,lep1,lep2):
        self.vec = vec
        self.lep1 = lep1
        self.lep2 = lep2

class HCandidate(object):
    def __init__(self,vec,Z1,Z2):
        self.vec = vec
        self.Z1 = Z1
        self.Z2 = Z2

class HZZProducer(Module):
    def __init__(self,name):
        super(HZZProducer,self).__init__(name)
        self.Zmass = 91.1876
        self.isoCutEl = 0.35
        self.isoCutMu = 0.35
        self.leadingLepPtCut = 20.0
        self.subleadingLepPtCut = 10.0
        self.deltaRCut = 0.02
        self.mllCut = 4.
        self.mZ1Range = [80.,100.]
        self.mZ2Range = [4.,120.]
        self.m4lLowCut = 115.

    def analyze(self,event):
        event.ZCandidates = self.makeZCandidates(event)
        event.HiggsCandidates = self.makeHiggsCandidates(event.ZCandidates,event)
        return True

    def makeZCandidates(self,event):
        candidateList = []
        for ilep in range(len(event.lep_id)):
            for jlep in range(ilep+1,len(event.lep_id)):
                if event.lep_id[ilep] + event.lep_id[jlep] != 0: continue
                
                vecli = self.make4Vector(event.lep_pt,event.lep_eta,event.lep_phi,event.lep_mass,ilep)
                veclj = self.make4Vector(event.lep_pt,event.lep_eta,event.lep_phi,event.lep_mass,jlep)
                veclifsr = self.make4Vector(event.lepFSR_pt,event.lepFSR_eta,event.lepFSR_phi,event.lepFSR_mass,ilep)
                vecljfsr = self.make4Vector(event.lepFSR_pt,event.lepFSR_eta,event.lepFSR_phi,event.lepFSR_mass,jlep)
                
                vecZ = veclifsr + vecljfsr
                
                lepi = Lepton(ilep,veclifsr,vecli)
                lepj = Lepton(jlep,vecljfsr,veclj)

                if vecZ.M() > 0:
                    candidateList.append(ZCandidate(vecZ,lepi,lepj))

    def makeHiggsCandidates(self,ZCandidates,event):
        HCandidates = []
        for i in range(len(ZCandidates)):
            for j in range(i+1,len(ZCandidates)):
                Zi = ZCandidates[i]
                Zj = ZCandidates[j]

                if Zi.lep1.index == Zj.lep1.index: continue
                if Zi.lep1.index == Zj.lep2.index: continue
                if Zi.lep2.index == Zj.lep1.index: continue
                if Zi.lep2.index == Zj.lep2.index: continue

                if abs(Zi.vec.M()-self.Zmass) < abs(Zj.vec.M()-self.Zmass):
                    Z1 = Zi
                    Z2 = Zj
                else:
                    Z1 = Zj
                    Z2 = Zi

                if event.lep_RelIsoNoFSR[Z1.lep1.index] > ((abs(event.lep_id[Z1.lep1.index])==11) ? self.isoCutEl : self.isoCutMu)): continue 
                if event.lep_RelIsoNoFSR[Z1.lep2.index] > ((abs(event.lep_id[Z1.lep2.index])==11) ? self.isoCutEl : self.isoCutMu)): continue 
                if event.lep_tightId[Z1.lep1.index]: continue
                if event.lep_tightId[Z1.lep2.index]: continue
                if event.lep_RelIsoNoFSR[Z2.lep1.index] > ((abs(event.lep_id[Z2.lep1.index])==11) ? self.isoCutEl : self.isoCutMu)): continue 
                if event.lep_RelIsoNoFSR[Z2.lep2.index] > ((abs(event.lep_id[Z2.lep2.index])==11) ? self.isoCutEl : self.isoCutMu)): continue 
                if event.lep_tightId[Z2.lep1.index]: continue
                if event.lep_tightId[Z2.lep2.index]: continue

                lep_vec_list = [Z1.lep1.vecnofsr,Z1.lep2.vecnofsr,Z2.lep1.vecnofsr,Z2.lep2.vecnofsr]
                
                #lep_pt_list = [Z1.lep1.vecnofsr.Pt(),Z1.lep2.vecnofsr.Pt(),Z2.lep1.vecnofsr.Pt(),Z2.lep2.vecnofsr.Pt()]
                lep_pt_list = [vec.Pt() for vec in lep_vec_list]
                lep_pt_list.sort(reverse=True)

                if lep_pt_list[0] < self.leadingLepPtCut: continue
                if lep_pt_list[1] < self.subleadingLepPtCut: continue

                deltaRs = []
                for i,vec1 in enumerate(lep_vec_list):
                    for j,vec2 in enumerate(lep_vec_list):
                        if i > j: continue
                        deltaRs.append(vec1.DeltaR(vec2))
                if min(deltaRs) < self.deltaRCut: continue

                mlls = []
                vec_i1i2 = Z1.lep1.vecnofsr+Z1.lep2.vecnofsr
                mlls.append(vec_i1i2.M())
                vec_j1j2 = Z2.lep1.vecnofsr+Z2.lep2.vecnofsr
                mlls.append(vec_j1j2.M())
                if event.lep_id[Z1.lep1.index]*event.lep_id[Z2.lep1.index] < 0:
                    vec_i1j1 = Z1.lep1.vecnofsr + Z2.lep1.vecnofsr
                    mlls.append(vec_i1j1.M())
                    vec_i2j2 = Z1.lep2.vecnofsr + Z2.lep2.vecnofsr
                    mlls.append(vec_i2j2.M())
                else:
                    vec_i1j2 = Z1.lep1.vecnofsr + Z2.lep2.vecnofsr
                    mlls.append(vec_i1j2.M())
                    vec_i1j2 = Z1.lep1.vecnofsr + Z2.lep2.vecnofsr
                    mlls.append(vec_i1j2.M())
                if min(mlls) < self.mllCut: continue

                if (Z1.vec.M() < self.mZ1Range[0]): continue
                if (Z1.vec.M() > self.mZ1Range[1]): continue
                if (Z2.vec.M() < self.mZ2Range[0]): continue
                if (Z2.vec.M() > self.mZ2Range[1]): continue

                Hvec = Z1.vec + Z2.vec
                if Hvec.M() < self.m4lLowCut: continue

                HCandidates.append(HCandidate(Hvec,Z1,Z2))

        return HCandidates
            
    @staticmethod
    def make4Vector(pts,etas,phis,masses,index):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiM(pts[index],etas[index],phis[index],masses[index])
        return vec
