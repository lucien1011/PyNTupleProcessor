class MassWindow(object):
    def __init__(self,name,central_value,width,selection=None):
        self.central_value = central_value
        self.width = width
        self.lower = central_value*(1-self.width)
        self.higher = central_value*(1+self.width)
        self.selection = selection
        self.name = name

    def makeHistName(self):
        return "_".join([str(self.central_value),str(self.width)])

    def inWindow(self,value):
        return value > self.lower and value < self.higher

class MultiMassWindow(object):
    def __init__(self,name,windowList):
        self.name = name
        self.windowList = windowList

    def makeHistName(self):
        return self.name

    def __len__(self):
        return len(self.windowList)

    def __getitem__(self,index):
        if index >= len(self):
            raise IndexError
        else:
            return self.windowList[index] 

    def end(self):
        for w in self.windowList:
            w.selection.end()
