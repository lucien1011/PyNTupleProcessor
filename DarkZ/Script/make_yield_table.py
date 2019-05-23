import os,ROOT,array

from Utils.System import system
from Core.mkdir_p import mkdir_p

from Bin import Bin
from Utils.TableMaker import TableMaker

ROOT.gROOT.SetBatch(ROOT.kTRUE)

class Setting(object):
    def __init__(self,outputFileName,caption,tab,bins):
        self.outputFileName = outputFileName
        self.caption = caption
        self.tab = tab
        self.bins = bins

# ________________________________________________________________________________________________ ||
User                    = os.environ['USER']
out_path                = "DarkPhotonSR/DataMCDistributions/2019-05-20_Run2016/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-05-20_Run2017/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2019-05-20_Run2018/"
inputDir                = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/"+out_path
TFileName               = "DataMCDistribution.root"
sampleNames = [
            "Higgs",
            "qqZZ",
            "ggZZ",
            "ZPlusX",
            ]
sampleLatexDict = { 
        "Higgs": "Higgs",
        "qqZZ": "\qqZZ",
        "ggZZ": "\ggZZ",
        "ZPlusX": "$Z+X$",
        }

setting_list = [
        Setting(
                outputFileName = "yield_low-m4l.tex",
                caption = "Summary for predictions of various backgrounds in the signal region ($100 < \massFourl < 118~\GeV$) for 2016.",
                tab = "predSR_low-m4l_2016",
                bins = [
                            Bin("mZ2_low-m4l_4e",0.05,latexName="4e"),
                            Bin("mZ2_low-m4l_2mu2e",0.05,latexName="2\mu2e"),
                            Bin("mZ2_low-m4l_4mu",0.02,latexName="4\mu"),
                            Bin("mZ2_low-m4l_2e2mu",0.02,latexName="2e2\mu"),
                        ],
                ),
        Setting(
                outputFileName = "yield_mid-m4l.tex",
                caption = "Summary for predictions of various backgrounds in the signal region ($118 < \massFourl < 130~\GeV$) for 2016.",
                tab = "predSR_mid-M4l_2016",
                bins = [
                            Bin("mZ2_mid-m4l_4e",0.05,latexName="4e"),
                            Bin("mZ2_mid-m4l_2mu2e",0.05,latexName="2\mu2e"),
                            Bin("mZ2_mid-m4l_4mu",0.02,latexName="4\mu"),
                            Bin("mZ2_mid-m4l_2e2mu",0.02,latexName="2e2\mu"),
                        ],
                ),
        Setting(
                outputFileName = "yield_high-m4l.tex",
                caption = "Summary for predictions of various backgrounds in the signal region ($130 < \massFourl < 170~\GeV$) for 2016.",
                tab = "predSR_high-m4l_2016",
                bins = [
                            Bin("mZ2_high-m4l_4e",0.05,latexName="4e"),
                            Bin("mZ2_high-m4l_2mu2e",0.05,latexName="2\mu2e"),
                            Bin("mZ2_high-m4l_4mu",0.02,latexName="4\mu"),
                            Bin("mZ2_high-m4l_2e2mu",0.02,latexName="2e2\mu"),
                        ],
                ), 
        ]
outputDir               = "/Users/lucien/public_html//Higgs/DarkZ/DarkPhotonSR/Table/2019-05-20_Run2016/"
#outputDir               = "/Users/lucien/public_html//Higgs/DarkZ/DarkPhotonSR/Table/2019-05-20_Run2017/"
#outputDir               = "/Users/lucien/public_html//Higgs/DarkZ/DarkPhotonSR/Table/2019-05-20_Run2018/"

# ________________________________________________________________________________________________ ||
print("Input directory: "+inputDir)
print("Output directory: "+outputDir)
mkdir_p(outputDir)

for setting in setting_list:
    bins = setting.bins
    tab = setting.tab
    caption = setting.caption
    outputFileName = setting.outputFileName
    tableDict = {}
    tableDict["nColumn"] = len(bins)+1
    tableDict["tab"] = tab
    tableDict["caption"] = caption
    tableDict["tableList"] = []
    headerList = ["Process",]
    for b in bins:
        headerList.append(b.latexName)
    tableDict["tableList"].append(headerList)
    for sampleName in sampleNames:
        fPath = os.path.join(inputDir,sampleName,TFileName)
        f = ROOT.TFile(fPath,"READ")
        tempList = [sampleLatexDict[sampleName],]
        for b in bins:
            h = f.Get(b.histName)
            error = ROOT.Double(0.)
            integral = h.IntegralAndError(0,h.GetNbinsX()+1,error)
            tempList.append("%4.2f"%integral+" \pm "+"%4.2f"%error)
        f.Close()
        tableDict["tableList"].append(tempList) 
    tableMaker = TableMaker()
    tableMaker.makeTexFile(os.path.join(outputDir,outputFileName),tableDict,isANInput=True,)
