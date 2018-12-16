from Core.Utils.UFTier2Utils import listdir_uberftp
import os

dir_path        = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Sept18_v1/"
inUFTier2       = True
treeName        = "tree"

dataComponentDict = {}
if inUFTier2:
    fileNames = [ n for n in listdir_uberftp(dir_path) if n.endswith(".root") ]
else:
    fileNames = [ n for n in os.listdir(dir_path) if n.endswith(".root") ]

for fileName in fileNames:
    if all([pd not in fileName for pd in ["MuonEG","DoubleMuon","DoubleEG",]]): continue
    if "ext" not in fileName:
        sampleName = fileName.replace(".root","")
    else:
        sampleName = fileName.split("_ext")[0]
    tmpDataset = Dataset(
            sampleName,
            ComponentList(
                [Component(sampleName,os.path.join(dir_path,fileName),treeName,inUFTier2,),]
                ),
            isMC = False,
            )
    #tmpDataset.setSumWeight(os.path.join(dir_path,fileName),"SumGenWeights",inUFTier2)
    if sampleName not in dataComponentDict:
        dataComponentDict[sampleName] = tmpDataset
    else:
        dataComponentDict[sampleName].add(tmpDataset)
