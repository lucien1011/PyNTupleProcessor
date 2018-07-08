from Core.Module import Module

class DeltaRSkimmer(Module):
    def analyze(self,event):
        lep_vec_list = [event.Z1.lep1.vec,event.Z1.lep2.vec,event.Z2.lep1.vec,event.Z2.lep2.vec]
        deltaRs = []
        for i,vec1 in enumerate(lep_vec_list):
            for j,vec2 in enumerate(lep_vec_list):
                if i >= j: continue
                deltaRs.append(vec1.DeltaR(vec2))
        if min(deltaRs) < 0.02: return False
        return True
