from Core.Module import Module

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow="DarkPhoton-SR"):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "DarkPhoton-SR":
            if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            if event.massZ1[0] <= 0. or event.massZ1[0] > 60.: return False
            if event.massZ2[0] <= 0. or event.massZ2[0] > 60.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "DarkPhoton-m4lSB":
            #if not ((event.mass4l[0]>105. and event.mass4l[0]<118.) or (event.mass4l[0]>130. and event.mass4l[0]<140.)): return False
            if event.mass4l[0] < 100.: return False
            #if not ((event.mass4l[0]>105. and event.mass4l[0]<118.)): return False
            #if not ((event.mass4l[0]>130. and event.mass4l[0]<140.)): return False
            #if not ((event.mass4l[0]>130. and event.mass4l[0]<160.)): return False
            #if not ((event.mass4l[0]>130. and event.mass4l[0]<180.)): return False
            #if event.mass4l[0] > 118. and event.mass4l[0] < 130.: return False
            if event.massZ1[0] < 0. or event.massZ1[0] > 60.: return False
            if event.massZ2[0] < 0. or event.massZ2[0] > 60.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "DarkPhoton-m4l70":
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 0. or event.massZ1[0] > 60.: return False
            if event.massZ2[0] < 0. or event.massZ2[0] > 60.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        return False
