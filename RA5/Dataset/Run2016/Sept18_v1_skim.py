from Core.ComponentList import *
from Core.Utils.UFTier2Utils import listdir_uberftp
from RA5.Dataset.Run2016.Sept18_v1 import componentDict
import os

#dir_path        = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Sept18_v1/"
dir_path        = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/Sept18_v1_skim/"
inUFTier2       = False
treeName        = "tree"
rootFileName    = "SkimTree.root"
postfix         = "/"+rootFileName

if inUFTier2:
    fileNames = [ n for n in listdir_uberftp(dir_path) if "txt" not in n and "skip" not in n]
else:
    fileNames = [ n for n in os.listdir(dir_path) if "txt" not in n and "skip" not in n]

skimComponentDict = {}
for fileName in fileNames:
    if "ext" not in fileName:
        sampleName = fileName.replace(postfix,"")
    else:
        sampleName = fileName.split("/")[-1].split("_ext")[0]
    if sampleName in componentDict:
        if sampleName not in skimComponentDict:
            skimComponentDict[sampleName] = componentDict[sampleName]
            skimComponentDict[sampleName].componentList = ComponentList( [Component(sampleName,os.path.join(dir_path,fileName,rootFileName),treeName,inUFTier2,),] )
        else:
            skimComponentDict[sampleName].componentList.extend( [Component(sampleName,os.path.join(dir_path,fileName,rootFileName),treeName,inUFTier2,),] )
