from Core.Module import Module
from Core.Utils.LambdaFunc import LambdaFunc

class CustomVariable(LambdaFunc):
    def __init__(self,inputStr,selStr="x: True",globalSelStr="x: True"):
        super(CustomVariable,self).__init__(inputStr)
        self.selFunc = LambdaFunc(selStr)
        self.globalSelFunc = LambdaFunc(globalSelStr)

    def end(self):     
        if hasattr(self,"func"):
            del self.func
        if hasattr(self,"selFunc"):
            del self.selFunc
        if hasattr(self,"globalSelFunc"):
            del self.globalSelFunc

class CSVFileSetting(object):
    def __init__(self,keyName,args,objType="CSVFile"):
        self.keyName = keyName
        self.objType = objType
        self.args = args

class CSVFileProducer(Module):
    def __init__(self,name,varsToWrite,csvFileSetting,objectFunc=None,globalSelFunc=None,):
        super(CSVFileProducer,self).__init__(name)
        self.varsToWrite = varsToWrite
        self.csvFileSetting = csvFileSetting
        self.objectFunc = objectFunc
        self.globalSelFunc = globalSelFunc

    def begin(self):
        self.writer.book(self.csvFileSetting.keyName,self.csvFileSetting.objType,*self.csvFileSetting.args)

    def analyze(self,event):
        if not self.objectFunc:
            row = [var(event) for var in self.varsToWrite if var.selFunc(event)]
            self.writer.objs[self.csvFileSetting.keyName].writer.writerow(row)
        else:
            for obj in self.objectFunc(event):
                if not self.globalSelFunc(obj): continue
                row = [var(obj) for var in self.varsToWrite if var.selFunc(obj)]
                self.writer.objs[self.csvFileSetting.keyName].writer.writerow(row)
        return True

    def end(self):
        for var in self.varsToWrite:
            var.end()
        self.objectFunc.end()
        self.writer.objs[self.csvFileSetting.keyName].pyFile.close()
        del self.writer.objs[self.csvFileSetting.keyName]
