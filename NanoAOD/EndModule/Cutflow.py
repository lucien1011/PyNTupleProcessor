class Cutflow(object):
    def __init__(self,key,latexName=""):
        self.key = key
        self.latexName = key if not latexName else latexName

    def getLatexName(self):
        return self.latexName
