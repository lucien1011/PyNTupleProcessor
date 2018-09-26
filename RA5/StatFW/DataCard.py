from StatFW.SystWriter import *

class DataCard(object):
    def __init__(self,window):
        self.sep = "---------------------------------------------------------------------------------"
        self.window = window

    def getBinName(self):
        return self.window.getBinName()

    #def makeHeader(self,rootFilePath):
    def makeHeader(self):
        header = '''
*     number of categories
*     number of samples minus one
*     number of nuisance parameters
-----------------------------------------------------------------------
'''
        #header += "shapes * * {0} $CHANNEL/$PROCESS $CHANNEL/$PROCESS_$SYSTEMATIC\n".format(rootFilePath.split("/")[-1])
        header += "shapes * * FAKE\n"
        header += self.sep+"\n"
        header += "\n"
        return header

    def makeStandardCardDetails(self,binList):
        self.rateParamLines = ""
        self.binName = "bin\t"
        self.processName = "process\t"
        self.processNum = "process\t"
        self.binNameObservation = "bin\t"
        for bin in binList:
            self.binNameObservation += bin.name+"\t"
            for iprocess,process in enumerate(bin.processList):
                self.binName += bin.name+"\t"
                self.processName += process.name+"\t"
                if bin.isSignal(process.name):
                    self.processNum += "0\t"
                else:
                    self.processNum += str(iprocess+1)+"\t"
        self.observation = "observation"
        self.rates = "rate\t"
        self.sep = "---------------------------------------------------------------------------------"
        self.systLines = ""
        return  

    def makeObservationLine(self,binList):
        line = ""
        line += self.observation+"\t"
        for bin in binList:
            line += str(bin.data.count)+"\t"
        line += "\n"
        return line

    def makeCard(self,outputDir,binList,appendToPath=""):
        outputStr = ""

        self.makeStandardCardDetails(binList)
        
        binName = self.getBinName()
        
        outputStr = self.makeHeader()
        outputStr += self.binNameObservation+"\n"
        outputStr += self.makeObservationLine(binList)
        outputStr += self.sep+"\n"
        outputStr += self.binName+"\n"
        outputStr += "\n"
        outputStr += "\n"

        outputStr += self.processName+"\n"
        outputStr += self.processNum+"\n"

        outputStr += self.rates+"\t"
        for bin in binList:
            for process in bin.processList:
                outputStr += "%4.4f"%process.count+"\t"
        outputStr += "\n"
        outputStr += self.sep+"\n"
        outputStr += "\n"

        systWriter = SystWriter()
        outputStr += systWriter.makeMCSystLine(binList)
        #outputStr += systWriter.writeRateParams(self.analysisBin)
        #outputStr += systWriter.writeParameters(self.analysisBin)

        outputPath = outputDir+self.makeOutFileName(".txt",appendToPath)

        outputFile = open(outputPath,"w")
        outputFile.write(outputStr)
        outputFile.close()

    def makeOutFileName(self,extension,appendToPath):
        outputPath = self.getBinName()+extension if not appendToPath else self.getBinName()+"_"+appendToPath+extension
        return outputPath
