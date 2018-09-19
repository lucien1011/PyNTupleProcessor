import ROOT,sys
from Utils.TableMaker import TableMaker 

samples = [
        "TT_pow",
        "WJets",
        "DYJets",
        "WZ",
        #"ttVorH",
        #"ttW",
        #"gamma+X",
        #"Minor",
        "SMS-T1qqqqL_mGluino1000",
        "SMS-T1qqqqL_mGluino1500",
        ]

header_samples = [
        "TT",
        "WJets",
        "DYJets",
        "WZ",
        #"ttVorH",
        #"ttW",
        #"gamma+X",
        #"Minor",
        "T1qqqqL 1000",
        "T1qqqqL 1500",
        ]

tableMaker = TableMaker()
tableDict = {}
tableDict["nColumn"] = len(samples)+1
tableDict["tab"] = "Yield"
tableDict["caption"] = "Yield"
tableDict["tableList"] = []
headerList = ["SR"]+header_samples
tableDict["tableList"].append(headerList)

yieldDict = {}
for sample in samples:
    inputFile = ROOT.TFile(sys.argv[1]+"/"+sample+"/Yield.root","READ")
    objNames = [k.GetName() for k in inputFile.GetListOfKeys() if "HHSR" in k.GetName()]
    objNames.sort()
    for objName in objNames:
        if objName not in yieldDict:
            yieldDict[objName] = {}
        obj = inputFile.Get(objName)
        yieldDict[objName][sample] = (obj.GetBinContent(1),obj.GetBinError(1))
        #print "%10s: %4.2f +- %4.2f"%(objName,obj.GetBinContent(1),obj.GetBinError(1))
    inputFile.Close()

srNameList = [key for key in yieldDict]
srNameList.sort(key=lambda x: int(x.split("SR")[-1]))
#for srName,sampleDict in yieldDict.iteritems():
for srName in srNameList:
    sampleDict = yieldDict[srName]
    tableDict["tableList"].append(
                [srName.replace("YieldCount",""),]+["%4.2f +- %4.2f"%sampleDict[sample] if sample in sampleDict else "NA" for sample in samples]
            )

tableMaker.makeTexFile("YieldTable.tex",tableDict,landscape=True)
