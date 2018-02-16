
class UFEventReader(object):
    def __init__(self,sequence):
        self.sequence = sequence

    def begin(self,events):
        for module in self.sequence:
            module.begin()

    def end(self):
        for module in self.sequence:
            module.end()

    def event(self,event):
        for module in self.sequence:
            if not module.analyze(event): break
            pass

    def copyFrom(self, src): pass

