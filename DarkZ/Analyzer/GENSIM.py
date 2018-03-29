from Core.Module import Module
from DataFormats.FWLite import Handle

class CollectionProducer(Module):
    def __init__(self,name,label,inCollType='std::vector<reco::GenParticle',outCollName="genparts",selection=None):
        super(CollectionProducer,self).__init__(name)
        self.label = label
        self.inCollType = inCollType
        self.outCollName = outCollName
        self.selection = selection

    def begin(self):
        self.handle = Handle(self.inCollType)

    def analyze(self,event):
        event.getByLabel(self.label,self.handle)
        setattr(event,self.outCollName,[p for p in self.handle.product() if self.selection and self.selection(p)])
        return True
