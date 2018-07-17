def conept_RA5(lep):
    if (abs(lep.pdgId)!=11 and abs(lep.pdgId)!=13):
        return lep.pt
    A = 0.12 if (abs(lep.pdgId)==11) else 0.16
    B = 0.80 if (abs(lep.pdgId)==11) else 0.76
    C = 7.2 if (abs(lep.pdgId)==11) else 7.2
    if (lep.jetPtRelv2>C):
        return lep.pt*(1+max(lep.miniRelIso-A,0))
    else:
        return max(lep.pt,lep.pt/lep.jetPtRatiov2*B)
