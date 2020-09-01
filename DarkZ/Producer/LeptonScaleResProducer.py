from Core.Module import Module
import ROOT

resUnc = 1.2

class LeptonScaleResProducer(Module):
    def analyze(self,event):
        event.vecL1_ScaleUp = self.make4Vector(event.lep_pt[event.lep_Hindex[0]]+event.lep_pterr[event.lep_Hindex[0]],event.lep_eta[event.lep_Hindex[0]],event.lep_phi[event.lep_Hindex[0]],event.lep_mass[event.lep_Hindex[0]])
        event.vecL2_ScaleUp = self.make4Vector(event.lep_pt[event.lep_Hindex[1]]+event.lep_pterr[event.lep_Hindex[1]],event.lep_eta[event.lep_Hindex[1]],event.lep_phi[event.lep_Hindex[1]],event.lep_mass[event.lep_Hindex[1]])
        event.vecL3_ScaleUp = self.make4Vector(event.lep_pt[event.lep_Hindex[2]]+event.lep_pterr[event.lep_Hindex[2]],event.lep_eta[event.lep_Hindex[2]],event.lep_phi[event.lep_Hindex[2]],event.lep_mass[event.lep_Hindex[2]])
        event.vecL4_ScaleUp = self.make4Vector(event.lep_pt[event.lep_Hindex[3]]+event.lep_pterr[event.lep_Hindex[3]],event.lep_eta[event.lep_Hindex[3]],event.lep_phi[event.lep_Hindex[3]],event.lep_mass[event.lep_Hindex[3]])
        event.vecL1_ScaleDown = self.make4Vector(event.lep_pt[event.lep_Hindex[0]]-event.lep_pterr[event.lep_Hindex[0]],event.lep_eta[event.lep_Hindex[0]],event.lep_phi[event.lep_Hindex[0]],event.lep_mass[event.lep_Hindex[0]])
        event.vecL2_ScaleDown = self.make4Vector(event.lep_pt[event.lep_Hindex[1]]-event.lep_pterr[event.lep_Hindex[1]],event.lep_eta[event.lep_Hindex[1]],event.lep_phi[event.lep_Hindex[1]],event.lep_mass[event.lep_Hindex[1]])
        event.vecL3_ScaleDown = self.make4Vector(event.lep_pt[event.lep_Hindex[2]]-event.lep_pterr[event.lep_Hindex[2]],event.lep_eta[event.lep_Hindex[2]],event.lep_phi[event.lep_Hindex[2]],event.lep_mass[event.lep_Hindex[2]])
        event.vecL4_ScaleDown = self.make4Vector(event.lep_pt[event.lep_Hindex[3]]-event.lep_pterr[event.lep_Hindex[3]],event.lep_eta[event.lep_Hindex[3]],event.lep_phi[event.lep_Hindex[3]],event.lep_mass[event.lep_Hindex[3]])
        event.vecL34_ScaleUp = event.vecL3_ScaleUp+event.vecL4_ScaleUp
        event.vecL34_ScaleDown = event.vecL3_ScaleDown+event.vecL4_ScaleDown
        event.massZ2_ScaleUp = event.vecL34_ScaleUp.M()
        event.massZ2_ScaleDown = event.vecL34_ScaleDown.M()

        event.vecL1_ResUp = self.make4Vector(event.lep_pt[event.lep_Hindex[0]]+event.lep_pterr[event.lep_Hindex[0]]*resUnc,event.lep_eta[event.lep_Hindex[0]],event.lep_phi[event.lep_Hindex[0]],event.lep_mass[event.lep_Hindex[0]])
        event.vecL2_ResUp = self.make4Vector(event.lep_pt[event.lep_Hindex[1]]+event.lep_pterr[event.lep_Hindex[1]]*resUnc,event.lep_eta[event.lep_Hindex[1]],event.lep_phi[event.lep_Hindex[1]],event.lep_mass[event.lep_Hindex[1]])
        event.vecL3_ResUp = self.make4Vector(event.lep_pt[event.lep_Hindex[2]]+event.lep_pterr[event.lep_Hindex[2]]*resUnc,event.lep_eta[event.lep_Hindex[2]],event.lep_phi[event.lep_Hindex[2]],event.lep_mass[event.lep_Hindex[2]])
        event.vecL4_ResUp = self.make4Vector(event.lep_pt[event.lep_Hindex[3]]+event.lep_pterr[event.lep_Hindex[3]]*resUnc,event.lep_eta[event.lep_Hindex[3]],event.lep_phi[event.lep_Hindex[3]],event.lep_mass[event.lep_Hindex[3]])
        event.vecL1_ResDown = self.make4Vector(event.lep_pt[event.lep_Hindex[0]]-event.lep_pterr[event.lep_Hindex[0]]*resUnc,event.lep_eta[event.lep_Hindex[0]],event.lep_phi[event.lep_Hindex[0]],event.lep_mass[event.lep_Hindex[0]])
        event.vecL2_ResDown = self.make4Vector(event.lep_pt[event.lep_Hindex[1]]-event.lep_pterr[event.lep_Hindex[1]]*resUnc,event.lep_eta[event.lep_Hindex[1]],event.lep_phi[event.lep_Hindex[1]],event.lep_mass[event.lep_Hindex[1]])
        event.vecL3_ResDown = self.make4Vector(event.lep_pt[event.lep_Hindex[2]]-event.lep_pterr[event.lep_Hindex[2]]*resUnc,event.lep_eta[event.lep_Hindex[2]],event.lep_phi[event.lep_Hindex[2]],event.lep_mass[event.lep_Hindex[2]])
        event.vecL4_ResDown = self.make4Vector(event.lep_pt[event.lep_Hindex[3]]-event.lep_pterr[event.lep_Hindex[3]]*resUnc,event.lep_eta[event.lep_Hindex[3]],event.lep_phi[event.lep_Hindex[3]],event.lep_mass[event.lep_Hindex[3]])
        event.vecL34_ResUp = event.vecL3_ResUp+event.vecL4_ResUp
        event.vecL34_ResDown = event.vecL3_ResDown+event.vecL4_ResDown
        event.massZ2_ResUp = event.vecL34_ResUp.M()
        event.massZ2_ResDown = event.vecL34_ResDown.M()
        return True

    @staticmethod
    def make4Vector(pt,eta,phi,mass):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiM(pt,eta,phi,mass)
        return vec
