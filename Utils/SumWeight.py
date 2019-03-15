

def handleSumWeight(dataset,system,sumWeightFile,sumWeightHist,inUFTier2,saveSumWeightTxt,textFilePath):
    if system.getSystemMode() == system.remote_str:
        dataset.setSumWeight(
                sumWeightFile,
                sumWeightHist,inUFTier2)
        if saveSumWeightTxt:
            dataset.saveSumWeightToPath(textFilePath)
    elif system.getSystemMode() == system.local_str:
        dataset.setSumWeightByTxt(textFilePath)
    

