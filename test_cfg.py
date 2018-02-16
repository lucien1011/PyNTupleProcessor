# UF Heppy Framework specifics
from Core.Sequence import Sequence
from Core.Module import Module

from RPV.Module.EventPrinter import EventPrinter

nCores = 2
inputDir = "/afs/cern.ch/work/k/klo/SUSY/RPV/TreeProduction/CMSSW_8_0_25/src/CMGTools/RPV/cfg/TEST_01/"
componentList = ["SMS_RPV_madgraphMLM_1",]
nEvents = -1
disableProgressBar = True
eventPrinter = EventPrinter("EventPrinter")
sequence = Sequence()
sequence.add(eventPrinter)
