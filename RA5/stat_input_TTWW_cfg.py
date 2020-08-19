# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Config.MergeSampleDefinition import mergeSampleDict
#from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from RA5.Sequence.RecoSequence import ttww_sequence
from RA5.Producer.StatInputProducer import StatInputProducer

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

#from RA5.Dataset.Run2016.Sept18_v1 import *
from RA5.Dataset.Run2016.Sept18_v1_Data import *
from RA5.Dataset.Run2016.Sept18_v1_skim import *
from RA5.Dataset.Run2016.Oct18_v1_TTWW import sigComponentDict

'''if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/RPV/DataMCDistributions/2018-09-12_HLTEmulation/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    #out_path = "RPV/DataMCDistribution/2018-09-19_OnlyMET0To50/"
    #out_path = "RPV/DataMCDistribution/2018-09-19/"
    #out_path = "RPV/StatInput/rpv_binning2016_v1_120fb-1/2018-09-26/"
    out_path = "RPV/StatInput/rpv_binning2016_v4_150fb-1/2018-10-15/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path'''
out_path = "StatInput/TTWW_met_50_bjet_onebin/"
outputDir = "/raid/raid7/kshi/SUSY/RA5/" +out_path
endModuleOutputDir = "/home/kshi/public_html/SUSY/RA5/" + out_path
lepCats = ["HH","HL","LL"]

nCores = 5
nEvents = -1
disableProgressBar = False
justEndSequence = False
verbose = False
#componentList = skimComponentDict.values() + dataComponentDict.values() + sigComponentDict.values()
componentList = skimComponentDict.values() + sigComponentDict.values()
#componentList = sigComponentDict.values()
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 136.1
    for component in dataset.componentList:
        component.maxEvents = nEvents

statInputProducer = StatInputProducer("StatInputProducer",[])
sequence = ttww_sequence
sequence.add(statInputProducer)

endSequence = EndSequence(skipHadd=False,haddAllSamples=True)
#endSequence = EndSequence(skipHadd=False,haddAllSamples=False)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "StatInput.root"
