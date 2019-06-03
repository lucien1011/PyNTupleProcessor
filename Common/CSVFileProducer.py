from Core.Module import Module

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
        row = [var(event) for var in self.varsToWrite]
        self.writer.objs[self.csvFileSetting.keyName].writer.writerow(row)
        return True

    #def end(self):
    #    self.writer.objs[self.csvFileSetting.keyName].pyFile.close()
