from collections import OrderedDict

class SystWriter(object):
    def makeMCSystLine(self,binList):
        outputStr = ""
        systDict = OrderedDict()
        for analysisBin in binList:
            for syst in analysisBin.systList:
                if syst.name not in systDict:
                    systDict[syst.name] = syst
        for systName in systDict:
            for analysisBin in binList:    
                systematics = analysisBin.systList
                foundSyst = False
                for systematic in systematics:
                    if systematic.name == systName:
                        foundSyst = True
                        break
                processList = analysisBin.processList
                if systematic.skipDC: continue
                if foundSyst:
                    outputStr += self.makelnNLine(systematic,processList,analysisBin,lineExist=systName in outputStr,forceDash=False)
                else:
                    outputStr += self.makelnNLine(systDict[systName],processList,analysisBin,lineExist=systName in outputStr,forceDash=True)
            outputStr +="\n"
        return outputStr

    @staticmethod
    def makelnNLine(systematic,processList,analysisBin,lineExist=False,forceDash=False,writeNameOnly=False):
        outputStr = ""
        if not lineExist:
            systName = systematic.getSystName() if not systematic.correlation else systematic.correlation(systematic.systNamePrefix,systematic,analysisBin,"",whichType="card")
            outputStr += systName+"\tlnN\t"
        correlationStr = ""
        if not writeNameOnly:
            for eachProcess in processList:
                if eachProcess.name not in systematic.process or forceDash:
                    correlationStr += "-\t"
                else:
                    if type(systematic.magnitudeFunc) != float:
                        correlationStr += "%s\t"%systematic.magnitudeFunc(systematic,eachProcess.name,analysisBin)
                    else:
                        correlationStr += "%4.2f\t"%systematic.magnitudeFunc

            outputStr += correlationStr
        #outputStr +="\n"
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
