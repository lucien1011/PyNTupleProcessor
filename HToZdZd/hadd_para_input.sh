#!/bin/bash

baseDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_Run
baseZXDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_Run
outputDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_RunII/

for s in Data Higgs qqZZ ggZZ HToZdZd_MZD10 HToZdZd_MZD4 HToZdZd_MZD20 HToZdZd_MZD30 HToZdZd_MZD40 HToZdZd_MZD50 HToZdZd_MZD60 ZPlusX;
do
    mkdir ${outputDir}/${s}/
    hadd -f ${outputDir}/${s}/StatInput.root ${baseDir}2*/${s}/StatInput.root
done

hadd -f ${outputDir}/ZPlusX/ParaShape.root ${baseZXDir}2*/ZPlusX/ParaShape.root
