from Core.ComponentList import *
from Core.Dataset import Dataset

from LJMet.Dataset.FWLJMet_weights_step1_tptp2017 import *
from LJMet.Dataset.FWLJMet_samples_step1_tptp2017 import *

import os

# ____________________________________________________________________________________________________________________________________________ ||
inputSkimTreeDir    = "/eos/uscms/store/user/escharni/FWLJMET102X_1lep2017Dnn_071519_step1hadds/"
treeName            = "ljmet"

# ____________________________________________________________________________________________________________________________________________ ||
sampleDict = {}
for d in os.listdir(inputSkimTreeDir):
    if "TprimeTprime_M-700" in d: continue

    if d.split("_")[-2].isdigit():
        sampleName = "_".join(d.split("_")[:-2])
    else:
        sampleName = "_".join(d.split("_")[:-1])

    isData = "SingleMuon" in sampleName or "SingleElectron" in sampleName
    isMC = not isData
    isSignal = "TprimeTprime" in sampleName or "BprimeBprime" in sampleName
    foundSample = False
    for sampleKey,eachSampleName in samples.iteritems():
        if eachSampleName == sampleName:
            foundSample = True
            break
    if foundSample:
        if sampleName not in sampleDict:
            sampleDict[sampleName] = Dataset(sampleKey,ComponentList([]),isMC=isMC,isSignal=isSignal,)
            if isMC and not isSignal:
                sampleDict[sampleName].xs = xsec[sampleKey]
                sampleDict[sampleName].sumw = nRun[sampleKey]
            elif isMC and isSignal:
                sampleDict[sampleName].xs = xsec[sampleKey[:-4]]
                sampleDict[sampleName].sumw = nRun[sampleKey]
        sampleDict[sampleName].componentList.list.append(Component(sampleKey,os.path.join(inputSkimTreeDir,d),treeName,False))

bkgSamples = [b for b in sampleDict.values() if b.isMC and not b.isSignal]
dataSamples = [b for b in sampleDict.values() if b.isData]
