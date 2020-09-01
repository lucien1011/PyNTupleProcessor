from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system
from Core.BaseObject import BaseObject
from Core.mkdir_p import mkdir_p

from HToZdZd.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import *

from HToZdZd.Config.MergeSampleDict_RunII import mergeSampleDict

import os,ROOT,shutil

User                    = os.environ['USER']
baseDir                 = system.getStoragePath()+"/"+User+"/Higgs/DarkZ/DarkPhotonSR/StatInput/"
outputBaseDir           = "2019-12-02_hadd_RunII/"
outputDir               = os.path.join(baseDir,outputBaseDir)
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + dataSamples + sigSamples
verbose                 = True

for s in sample2016.bkgSamples+sigSample2016.sigSamples : s.input = BaseObject("2016",inputDir=os.path.join(baseDir,"2019-12-02_Run2016/"),postfix="_Run2016",)
for s in sample2017.bkgSamples+sigSample2017.sigSamples : s.input = BaseObject("2017",inputDir=os.path.join(baseDir,"2019-12-02_Run2017/"),postfix="_Run2017",)
for s in sample2018.bkgSamples+sigSample2018.sigSamples : s.input = BaseObject("2018",inputDir=os.path.join(baseDir,"2019-12-02_Run2018/"),postfix="_Run2018",)
for s in sample2016.dataSamples: s.input = BaseObject("2016",inputDir=os.path.join(baseDir,"2019-12-02_Run2016/"),postfix="",)
for s in sample2017.dataSamples: s.input = BaseObject("2017",inputDir=os.path.join(baseDir,"2019-12-02_Run2017/"),postfix="",)
for s in sample2018.dataSamples: s.input = BaseObject("2018",inputDir=os.path.join(baseDir,"2019-12-02_Run2018/"),postfix="",)
for cmp in componentList:
    targetDir = os.path.join(outputDir,cmp.name)
    sourceDir = os.path.join(cmp.input.inputDir,cmp.name.replace(cmp.input.postfix,""))
    print "Copying "+targetDir+" to "+sourceDir
    shutil.copytree(sourceDir,targetDir)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=False)
