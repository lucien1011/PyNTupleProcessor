from Core.Module import Module
from Core.Utils.LambdaFunc import LambdaFunc

class CustomVariable(LambdaFunc):
    def __init__(self,inputStr,selStr="x: True"):
        super(CustomVariable,self).__init__(inputStr)
        self.selFunc = LambdaFunc(selStr)

    def end(self):     
        if hasattr(self,"func"):
            del self.func
        if hasattr(self,"selFunc"):
            del self.selFunc

class CSVFileSetting(object):
    def __init__(self,keyName,args,objType="CSVFile"):
        self.keyName = keyName
        self.objType = objType
        self.args = args

class CSVFileProducer(Module):
    def __init__(self,name,varsToWrite,csvFileSetting):
        super(CSVFileProducer,self).__init__(name)
        self.varsToWrite = varsToWrite
        self.csvFileSetting = csvFileSetting

    def begin(self):
        self.writer.book(self.csvFileSetting.keyName,self.csvFileSetting.objType,*self.csvFileSetting.args)

    def analyze(self,event):
        row = [var(event) for var in self.varsToWrite if var.selFunc(event)]
        self.writer.objs[self.csvFileSetting.keyName].writer.writerow(row)
        return True

    def end(self):
        for var in self.varsToWrite:
            var.end()
        self.writer.objs[self.csvFileSetting.keyName].pyFile.close()
        del self.writer.objs[self.csvFileSetting.keyName]
