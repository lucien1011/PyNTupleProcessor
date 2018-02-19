
from ..Writer import Writer

class UFEventReader(object):
    def __init__(self,dataset,sequence,outputInfo):
        self.dataset = dataset
        self.sequence = sequence
        self.outputInfo = outputInfo
        self.writer = Writer(dataset,outputInfo)

    def begin(self,events):
        self.writer.initObjects()
        for module in self.sequence:
            module.writer = self.writer
            module.dataset = self.dataset
            module.begin()

    def end(self):
        for module in self.sequence:
            module.end()
        self.writer.write()
        #self.writer.closeAll()

    def event(self,event):
        for module in self.sequence:
            if not module.analyze(event): break
            pass

    def copyFrom(self, src): pass

