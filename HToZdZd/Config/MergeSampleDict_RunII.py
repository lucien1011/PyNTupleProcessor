import MergeSampleDict as baseMergeSampleDict

mergeSampleDict = {}
for mergeSample in baseMergeSampleDict.mergeSampleDict:
    mergeSampleDict[mergeSample] = []
    for sample in baseMergeSampleDict.mergeSampleDict[mergeSample]:
        mergeSampleDict[mergeSample].append(sample+"_Run2016")
        mergeSampleDict[mergeSample].append(sample+"_Run2017")
        mergeSampleDict[mergeSample].append(sample+"_Run2018")

mergeSigSampleDict = {}
for mergeSample in baseMergeSampleDict.mergeSigSampleDict:
    mergeSigSampleDict[mergeSample] = []
    for sample in baseMergeSampleDict.mergeSigSampleDict[mergeSample]:
        mergeSigSampleDict[mergeSample].append(sample+"_Run2016")
        mergeSigSampleDict[mergeSample].append(sample+"_Run2017")
        mergeSigSampleDict[mergeSample].append(sample+"_Run2018")
