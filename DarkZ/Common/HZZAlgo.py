import ROOT

import operator

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

class HZZAlgo(object):
    def __init__(self):
        self.Zmass = 91.1876

    def makeZCandidatesFromBranch(self,lep_ids,lep_pts,lep_etas,lep_phis,lep_masses):
        candidateList = []
        for ilep in range(len(lep_ids)):
            for jlep in range(ilep+1,len(lep_ids)):
                if lep_ids[ilep] + lep_ids[jlep] != 0: continue
                
                vecli = self.make4VectorFromBranch(lep_pts,lep_etas,lep_phis,lep_masses,ilep)
                veclj = self.make4VectorFromBranch(lep_pts,lep_etas,lep_phis,lep_masses,jlep)
                #veclifsr = self.make4Vector(event.lepFSR_pt,event.lepFSR_eta,event.lepFSR_phi,event.lepFSR_mass,ilep)
                #vecljfsr = self.make4Vector(event.lepFSR_pt,event.lepFSR_eta,event.lepFSR_phi,event.lepFSR_mass,jlep)
                
                vecZ = vecli + veclj
                #vecZ = veclifsr + vecljfsr
                
                lepi = Lepton(ilep,vecli,vecli)
                lepj = Lepton(jlep,veclj,veclj)

                if vecZ.M() > 0.:
                    candidateList.append(ZCandidate(vecZ,lepi,lepj))
        return candidateList

    def makeZCandidatesFromCollection(self,leps,useFSR=False):
        candidateList = []
        for ilep in range(len(leps)):
            for jlep in range(ilep+1,len(leps)):
                if leps[ilep].id + leps[jlep].id != 0: continue
                
                if not useFSR:
                    vecli = self.make4VectorFromObject(leps[ilep].pt,leps[ilep].eta,leps[ilep].phi,leps[ilep].mass)
                    veclj = self.make4VectorFromObject(leps[jlep].pt,leps[jlep].eta,leps[jlep].phi,leps[jlep].mass)
                else:
                    vecli = self.make4VectorFromObject(leps[ilep].getFriendValue("FSR","pt"),leps[ilep].getFriendValue("FSR","eta"),leps[ilep].getFriendValue("FSR","phi"),leps[ilep].getFriendValue("FSR","mass"))
                    veclj = self.make4VectorFromObject(leps[jlep].getFriendValue("FSR","pt"),leps[jlep].getFriendValue("FSR","eta"),leps[jlep].getFriendValue("FSR","phi"),leps[jlep].getFriendValue("FSR","mass"))
 
                vecZ = vecli + veclj
                #vecZ = veclifsr + vecljfsr
                
                lepi = Lepton(ilep,vecli,vecli)
                lepj = Lepton(jlep,veclj,veclj)

                if vecZ.M() > 0.:
                    candidateList.append(ZCandidate(vecZ,lepi,lepj))
        return candidateList

    def makeZ1Z2(self,ZCandidates,mZ1Range,mZ2Range):
        deltaM = 999
        foundZ1 = False
        passZ1Cut = False
        for i in range(len(ZCandidates)):
            Zi = ZCandidates[i]
            if abs(Zi.vec.M()-self.Zmass) < deltaM:
                deltaM = abs(Zi.vec.M()-self.Zmass)
                Z1 = Zi
                Z1index = i
                foundZ1 = True
        
        if Z1.vec.M() > mZ1Range[0] and Z1.vec.M() < mZ1Range[1]:
            passZ1Cut = True

        for j in range(len(ZCandidates)):
            Zj = ZCandidates[j]
            if Zj.lep1.index == Z1.lep1.index or Zj.lep1.index == Z1.lep2.index or Zj.lep2.index == Z1.lep1.index or Zj.lep2.index == Z1.lep2.index: continue
            foundZ2 = Zj.vec.M() > mZ2Range[0] and Zj.vec.M() < mZ2Range[1]
            Z2 = Zj

        return Z1,Z2,foundZ1 and passZ1Cut and foundZ2

    @staticmethod
    def make4VectorFromBranch(pts,etas,phis,masses,index):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiM(pts[index],etas[index],phis[index],masses[index])
        return vec

    @staticmethod
    def make4VectorFromObject(pt,eta,phi,mass):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiM(pt,eta,phi,mass)
        return vec
