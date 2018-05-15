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

def Moriond17MVALooseElectron(obj):
    if abs(obj.eta) > 2.5: return False
    etaRegions = [0.8,1.479,9999.]
    cutDict = {
            0.8: -0.7,
            1.479: -0.83,
            2.5: -0.92,
            }
    for etaRegion in etaRegions:
        if abs(obj.eta) < etaRegion: break
    return  obj.mvaSpring16GP > cutDict[etaRegion]

def Moriond17MVAMediumElectron(obj):
    if abs(obj.eta) > 2.5: return False
    etaRegions = [0.8,1.479,9999.]
    cutDict = {
            0.8: -0.155,
            1.479: -0.56,
            2.5: -0.76,
            }
    for etaRegion in etaRegions:
        if abs(obj.eta) < etaRegion: break
    return  obj.mvaSpring16GP > cutDict[etaRegion]

def Moriond17MVATightElectron(obj):
    if abs(obj.eta) > 2.5: return False
    etaRegions = [0.8,1.479,2.5]
    cutDict = {
            0.8: 0.87,
            1.479: 0.60,
            2.5: 0.17,
            }
    for etaRegion in etaRegions:
        if abs(obj.eta) < etaRegion: break
    return  obj.mvaSpring16GP > cutDict[etaRegion]
