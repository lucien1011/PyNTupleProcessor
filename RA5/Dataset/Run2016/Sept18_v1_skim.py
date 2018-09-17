#from Core.ComponentList import *
#from Core.Dataset import Dataset
#from Core.Utils.UFTier2Utils import listdir_uberftp
from RA5.Dataset.Run2016.Sept18_v1 import componentDict
import os

#dir_path        = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Sept18_v1/"
dir_path        = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/Sept18_v1_skim/"
inUFTier2       = False
treeName        = "tree"
postfix         = "/SkimTree.root"

componentDict = {}
if inUFTier2:
    fileNames = [ n for n in listdir_uberftp(dir_path) if n.endswith(".root") ]
else:
    fileNames = [ n for n in os.listdir(dir_path) if n.endswith(".root") ]

skimComponentDict = {}
for fileName in fileNames:
    if "ext" not in fileName:
        sampleName = fileName.replace(postfix,"")
    else:
        sampleName = fileName.split("_")[0]
    if sampleName not in skimComponentDict:
        skimComponentDict[sampleName] = componentDict[sampleName]
        skimComponentDict[sampleName].componentList = ComponentList( [Component(sampleName,os.path.join(dir_path,fileName),treeName,inUFTier2,),] )
    else:
        skimComponentDict[sampleName].componentList.extend( [Component(sampleName,os.path.join(dir_path,fileName),treeName,inUFTier2,),] )
