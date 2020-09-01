#!/bin/bash

baseDir=/Users/lucien/NTuple/lucien/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/2019-09-05_Run
baseZXDir=/Users/lucien/NTuple/lucien/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/2019-09-05_Run
outputDir=/Users/lucien/NTuple/lucien/Higgs/DarkZ/DarkPhotonSR/ShapeTemplate/2019-09-05_RunII/
tfileName=DataMCDistribution.root
shapefileName=shape.root

mkdir ${outputDir}
for s in Higgs qqZZ ggZZ HZZd_M15 HZZd_M30 ppZZd4l_M15 ppZZd4l_M30 ZPlusX;
do
    echo "=========================" ; 
    mkdir ${outputDir}/${s}/ ; 
    hadd -f ${outputDir}/${s}/${tfileName} ${baseDir}2*/${s}/${tfileName}
done

hadd -f ${outputDir}/ZPlusX/${shapefileName} ${baseZXDir}2*/ZPlusX/${shapefileName}
mkdir ${outputDir}/Data/
hadd -f ${outputDir}/Data/${tfileName} ${baseDir}2*/Data*/${tfileName}

for yr in 2016 2017 2018 ; 
do 
    for s in Higgs qqZZ ggZZ HZZd_M15 HZZd_M30 ppZZd4l_M15 ppZZd4l_M30 ZPlusX;
    do
        mkdir ${outputDir}/${s}_${yr}/ ;
        cp -r ${baseDir}${yr}/${s}/* ${outputDir}/${s}_${yr}/ ;
    done ;

    mkdir ${outputDir}/Data${yr}/ ; 
    cp -r ${baseDir}${yr}/Data${yr}/* ${outputDir}/Data${yr}/ ;
done
