def Moriond17LooseJet(obj):
    if obj.pt < 25: return False
    if abs(obj.eta) > 2.5: return False
    if obj.neEmEF > 0.99: return False
    if obj.neHEF > 0.99: return False
    if obj.nConstituents <= 1: return False
    return True
