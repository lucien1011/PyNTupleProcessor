def Moriond17MediumMuon(obj):
    if obj.pt < 10: return False
    if abs(obj.eta) > 2.5: return False
    if not obj.mediumId: return False
    if obj.miniPFRelIso_all > 0.16: return False
    if obj.dxy > 0.05: return False
    if obj.dz > 0.1: return False
    if obj.sip3d > 4: return False
    return True
 
def Moriond17LooseMuon(obj):
    if obj.pt < 5: return False
    if abs(obj.eta) > 2.5: return False
    #if not obj.mediumId: return False
    if obj.miniPFRelIso_all > 0.40: return False
    if obj.dxy > 0.05: return False
    if obj.dz > 0.1: return False
    #if obj.sip3d < 4: return False
    return True

def Moriond17MediumElectron(obj):
    if obj.pt < 10: return False
    if abs(obj.eta) > 2.5: return False
    if obj.cutBased != 4: return False
    if obj.miniPFRelIso_all > 0.12: return False
    if obj.dxy > 0.05: return False
    if obj.dz > 0.1: return False
    if obj.sip3d > 4: return False
    if obj.lostHits != 0: return False
    if not obj.convVeto: return False
    return True

def Moriond17LooseElectron(obj):
    if obj.pt < 7: return False
    if abs(obj.eta) > 2.5: return False
    if obj.cutBased != 2: return False
    if obj.miniPFRelIso_all > 0.4: return False
    if obj.dxy > 0.05: return False
    if obj.dz > 0.1: return False
    if obj.sip3d > 4: return False
    if obj.lostHits > 1: return False
    if not obj.convVeto: return False
    return True
