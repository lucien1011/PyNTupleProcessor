from Core.Module import Module
from Core.Collection import Collection

class Category(object):
    def __init__(self):
        pass

class CategoryProducer(Module):
    def analyze(self,event):
        event.goodLeps = Collection(event,"LepGood")
        event.tightLeps = [l for l in event.goodLeps if l.isTight]
        event.tightLeps.sort(key=lambda x: x.pt,reverse=True)
        if len(event.tightLeps) != 2: return False
        event.cat = Category()
        if event.tightLeps[0].pt > 25 and event.tightLeps[1].pt > 25: event.cat.lepCat = "HH"
        if event.tightLeps[0].pt > 25 and event.tightLeps[1].pt < 25: event.cat.lepCat = "HL"
        if event.tightLeps[0].pt < 25 and event.tightLeps[1].pt < 25: event.cat.lepCat = "LL"
        return True
