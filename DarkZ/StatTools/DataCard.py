from DarkZ.StatTools.SystWriter import *

class DataCard(object):
    def __init__(self,window):
        self.sep = "---------------------------------------------------------------------------------"
        self.window = window
        self.makeStandardCardDetails()

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

    def makeStandardCardDetails(self):
        self.rateParamLines = ""
        self.binName = "bin\t"
        self.processName = "process\t"
        self.processNum = "process\t"
        for iprocess,process in enumerate(self.window.processList):
            self.binName += "Signal\t"
            self.processName += process.name+"\t"
            if "HZZd" not in process.name:
                self.processNum += str(iprocess+1)+"\t"
            else:
                self.processNum += "0\t"
        self.binNameObservation = "bin\tSignal\t"
        self.observation = "observation"
        self.rates = "rate\t"
        self.sep = "---------------------------------------------------------------------------------"
        self.systLines = ""
        return  

    def makeCard(self,outputDir,appendToPath=""):
        outputStr = ""
        
        binName = self.getBinName()
        
        outputStr = self.makeHeader()
        outputStr += self.binNameObservation+"\n"   
        outputStr += self.observation+"\t"+str(self.window.data.count)+"\n"
        outputStr += self.sep+"\n"
        outputStr += self.binName+"\n"
        outputStr += "\n"
        outputStr += "\n"

        outputStr += self.processName+"\n"
        outputStr += self.processNum+"\n"

        outputStr += self.rates+"\t"
        for process in self.window.processList:
            outputStr += str(process.count)+"\t"
        outputStr += "\n"
        outputStr += self.sep+"\n"
        outputStr += "\n"

        systWriter = SystWriter()
        outputStr += systWriter.makeMCSystLine(self.window)
        #outputStr += systWriter.writeRateParams(self.analysisBin)
        #outputStr += systWriter.writeParameters(self.analysisBin)

        outputPath = outputDir+self.makeOutFileName(".txt",appendToPath)

        outputFile = open(outputPath,"w")
        outputFile.write(outputStr)
        outputFile.close()

    def makeOutFileName(self,extension,appendToPath):
        outputPath = self.getBinName()+extension if not appendToPath else self.getBinName()+"_"+appendToPath+extension
        return outputPath
