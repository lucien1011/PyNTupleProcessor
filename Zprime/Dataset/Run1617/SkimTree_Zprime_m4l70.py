import Zprime.Dataset.Run2016.SkimTree_Bkg_m4l70 as sample2016
#import Zprime.Dataset.Run2016.SkimTree_Zprime_m4l70 as sampleSig2016
import Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 as sample2017
import Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 as sampleSig2017
#import Zprime.Dataset.Run2018.SkimTree_DarkPhoton_m4l70 as sample2018

for sample in sample2016.bkgSamples:
    sample.name += "_Run2016"
    sample.lumi = 35.9
for sample in sample2017.bkgSamples:
    sample.name += "_Run2017"
    sample.lumi = 41.4
'''
for sample in sample2018.bkgSamples:
    sample.name += "_Run2018"
    sample.lumi = 59.7
'''
bkgSamples = sample2016.bkgSamples + sample2017.bkgSamples# + sample2018.bkgSamples

sigSamples = sampleSig2017.sigSamples
for sample in sigSamples: sample.lumi = 77.3

#dataSamples = [sample2016.data2016,sample2017.data2017,sample2018.data2018,]
dataSamples = [sample2016.data2016,sample2017.data2017,]
