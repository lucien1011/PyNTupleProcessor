import os
import csv
import pickle

"""
Little script to parse btag scale factors .csv 
file into a pickled dictionary with structure:
{ WorkingPoint: { MeasurementType : { Systematic: { Flavour: { eta,pT bin: { ScaleFactor } } } } } }
"""

#bsfFileName = "CSVv2SF_25ns"
#bsfFileName = "CSV_13TEV_T1bbbb_1500_100_24_11_2015"
#bsfFileName = "CSV_13TEV_T1bbbb_1000_900_24_11_2015"
#bsfFileName = "CSV_13TEV_T1tttt_1500_100_24_11_2015"
#bsfFileName = "CSV_13TEV_T1tttt_1200_800_24_11_2015"
#bsfFileName = "CSV_13TEV_Combined_20_11_2015"

#bsfFileName = "CSVv2_2016_4fb"
#bsfFileName = "CSVv2_ichep"
#bsfFileName = "CSV_13TEV_T1bbbb_1500_100_14_7_2016"
#bsfFileName = "CSV_13TEV_T1bbbb_1000_900_11_7_2016"
#bsfFileName = "CSV_13TEV_T1tttt_1500_100_11_7_2016"
#bsfFileName = "CSV_13TEV_T1tttt_1200_800_11_7_2016"
#bsfFileName = "CSV_13TEV_Combined_14_7_2016"

bsfFileName = "CSVv2_Moriond17_B_H"
era = "2016Moriond17"

# bsfFileName = "DeepCSV_Moriond17_B_H"
# era = "2016Moriond17_DeepCSV"

if not os.path.exists(os.path.abspath(os.environ['BASE_PATH']+"/DataMC/BTagging/"+era+"/")):
    os.makedirs(os.path.abspath(os.environ['BASE_PATH']+"/DataMC/BTagging/"+era+"/"))

bsfFile = open(os.environ['BASE_PATH']+"/DataMC/BTagging/"+era+"/"+bsfFileName+".csv")

bsfDict = {}

for i, row in enumerate(csv.reader(bsfFile)):

    # Ignore empty rows, skip header
    if len(row) == 0: continue
    if i == 0: continue

    # Strip stupid characters
    for item in range(len(row)):
        row[item] = row[item].strip().strip('"')
   
    opPoint, measType, sysType, jetFlav, etaMin, etaMax, ptMin, ptMax, discrMin, discrMax, formula = row

    # Watch out for inconsistent use of etaMin
    #if etaMin == "0": etaMin = "-2.4"
    # Watch out for discrMin and discrMax
    #if "iterativefit" in measType: continue
    if discrMin != "0" or discrMax != "1": continue

    ptMin  = float(ptMin)
    ptMax  = float(ptMax)
    etaMin = float(etaMin)
    etaMax = float(etaMax)

    if opPoint  not in bsfDict:                             bsfDict[opPoint] = {}
    if measType not in bsfDict[opPoint]:                    bsfDict[opPoint][measType] = {}
    if sysType  not in bsfDict[opPoint][measType]:          bsfDict[opPoint][measType][sysType] = {}
    if jetFlav  not in bsfDict[opPoint][measType][sysType]: bsfDict[opPoint][measType][sysType][jetFlav] = {}

    bsfDict[opPoint][measType][sysType][jetFlav][((etaMin,etaMax),(ptMin,ptMax))] = formula

outFileName = os.environ['BASE_PATH']+"/DataMC/BTagging/"+era+"/btagScaleFactors_"+bsfFileName+".p"
pickle.dump( bsfDict, open(outFileName,"wb") )
print "Written SF file:", outFileName
