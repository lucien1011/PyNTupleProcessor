class SystWriter(object):
    def makeMCSystLine(self,analysisBin):
        systematics = analysisBin.systList
        processList = analysisBin.processList
        outputStr = ""
        for systematic in systematics:
            if systematic.skipDC: continue
            if systematic.systType == "shape":
                outputStr += self.makeShapeLine(systematic,processList,analysisBin)
            elif systematic.systType == "lnN":
                outputStr += self.makelnNLine(systematic,processList,analysisBin)
        return outputStr

    @staticmethod
    def makelnNLine(systematic,processList,analysisBin):
        outputStr = ""
        systName = systematic.getSystName() if not systematic.correlation else systematic.correlation(systematic.systNamePrefix,systematic,analysisBin,"",whichType="card")
        outputStr += systName+"\tlnN\t"
        correlationStr = ""
        for eachProcess in processList:
            if eachProcess.name not in systematic.process:
                correlationStr += "-\t"
            else:
                correlationStr += "%s\t"%systematic.magnitudeFunc(systematic,eachProcess.name,analysisBin)
        outputStr += correlationStr
        outputStr +="\n"
        return outputStr

    @staticmethod
    def makeShapeLine(systematic,processList,analysisBin):
        outputStr = ""
        systName = systematic.getSystName() if not systematic.correlation else systematic.correlation("",systematic,analysisBin,"",whichType="card")
        outputStr += systName+"\tshape\t"
        correlationStr = ""
        for eachProcess in processList:
            if eachProcess.name not in systematic.process:
                correlationStr += "-\t"
            else:
                correlationStr += "1\t"
        outputStr += correlationStr
        outputStr +="\n"
        return outputStr

    @staticmethod
    def makeRateParamLine(rateParamName,process,formulaStr,parameterStr):
        outputStr = ""
        outputStr += rateParamName+"Rate\trateParam\tSignal\t{process}\t{formulaStr}\t{parameterStr}\n".format(
                process=process,
                formulaStr=formulaStr,
                parameterStr=parameterStr,
                )
        return outputStr+"\n"

    @staticmethod
    def makeParamLine(paramName,meanStr,widthStr,paramRangeStr):
        outputStr = ""
        outputStr += "{paramName}\tparam\t{meanStr}\t{widthStr}\t{paramRangeStr}\n".format(
            paramName=paramName,
            meanStr=meanStr,
            widthStr=widthStr,
            paramRangeStr=paramRangeStr,
            )
        return outputStr+'\n'

    def writeRateParams(self,analysisBin):
        outputStr = ""
        analysisBin.parameterList = []
        for rateParam in analysisBin.rateParams:
            outputStr += self.makeRateParamLine(rateParam.name,rateParam.process,rateParam.formulaStr,rateParam.parameterStr)
            for paramStr in rateParam.parameterStr.split(","):
                if paramStr not in analysisBin.parameterList:
                    analysisBin.parameterList.append(paramStr)
        return outputStr

    def writeParameters(self,analysisBin):
        outputStr = ""
        for paramStr in analysisBin.parameterList:
            outputStr += self.makeParamLine(*analysisBin.paramDict[paramStr])
        return outputStr
