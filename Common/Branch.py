import copy

class BranchToAdd(object):
    def __init__(self,branchName,type,lenArray,lenVar=None,method="ret_leptonJetRecleaner",inputs=""):
        self.branchName = branchName
        self.type = type
        self.lenArray = lenArray
        self.lenVar = lenVar
        self.method = method
        self.inputs = inputs

    def getInit(self):
        return [self.branchName,self.type,self.lenArray,self.lenVar]
    
    def getValue(self,event):
        # An ugly method, but no choice because Lambda function does not work with multiprocessing
        if self.method == "ret_leptonJetRecleaner":
            return event.ret[self.inputs]
        else:
            raise RuntimeError, "Other method not supported at the moment"
