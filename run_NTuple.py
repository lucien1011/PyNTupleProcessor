
# alphatwirl
from Core.EventReader import EventLoopRunner, MPEventLoopRunner, EventLoop
from Core.ProgressBar import ProgressBar,ProgressReport,ProgressMonitor,BProgressMonitor
from Core.Concurrently import CommunicationChannel,CommunicationChannel0

from Core.BEventBuilder import BEventBuilder

from Core.ComponentLoop import ComponentLoop
from Core.UFComponentReader import UFComponentReader

from Core.Utils.git import getGitDescribe,getGitDiff
from Core.Utils.printFunc import pyPrint

# Standard package
import imp,sys,os,time

cfgFileName             = sys.argv[1]
file                    = open( cfgFileName,'r')
cfg                     = imp.load_source( 'UFNTuple.__cfg_to_run__', cfgFileName, file)

nCores                  = cfg.nCores
componentList           = cfg.componentList
nEvents                 = cfg.nEvents
disableProgressBar      = cfg.disableProgressBar
sequence                = cfg.sequence
outputInfo              = cfg.outputInfo
endSequence             = cfg.endSequence
justEndSequence         = cfg.justEndSequence if hasattr(cfg,"justEndSequence") else False
mergeSampleDict         = cfg.mergeSampleDict if hasattr(cfg,"mergeSampleDict") else {}
verbose                 = cfg.verbose if hasattr(cfg,"verbose") else False
skipGitDetail           = cfg.skipGitDetail if hasattr(cfg,"skipGitDetail") else False
eventSelection          = cfg.eventSelection if hasattr(cfg,"eventSelection") else None

if verbose:
    pyPrint("Starting")
start_time = time.time()

if not justEndSequence:
    if verbose:
        pyPrint("Initiating progress bar")
    progressBar = ProgressBar()
    
    if nCores != 1:
        progressMonitor      = BProgressMonitor(progressBar)
        communicationChannel = CommunicationChannel(nCores,progressMonitor)
    else:
        progressMonitor      = ProgressMonitor(progressBar)
        communicationChannel = CommunicationChannel0(progressMonitor)
        pass
        
    if not disableProgressBar: progressMonitor.begin()
    communicationChannel.begin()
    
    pyPrint("\nLoading samples:\n")
    for cmp in componentList:
        pyPrint(cmp.name)
    
    eventLoopRunner = MPEventLoopRunner(communicationChannel)
    eventBuilder    = BEventBuilder()
    componentReader = UFComponentReader(eventBuilder, eventLoopRunner, sequence, outputInfo,selection=eventSelection)
    componentLoop   = ComponentLoop(componentReader)
    
    pyPrint("\nBegin Running\n")
    componentLoop(componentList)
    
    pyPrint("\nEnd Running\n")
    pyPrint("\nOutput saved in "+outputInfo.outputDir+"\n")
   
    if not skipGitDetail:
        gitFile        = os.path.join(outputInfo.outputDir,"gitDetails.txt")
        gitVerboseFile = os.path.join(outputInfo.outputDir,"gitVerboseDetails.txt")
        with open(gitFile,'w') as f:
            f.write(getGitDescribe())
    
        with open(gitVerboseFile,'w') as f:
            f.write(getGitDiff())
    
    if verbose:
        pyPrint("Ending progress bar")
    if not disableProgressBar: progressMonitor.end()
    communicationChannel.end()

pyPrint("\nBegin Summarising\n")
pyPrint("\nInput used: "+outputInfo.outputDir+"\n")
endSequence.run(outputInfo,componentList,mergeSampleDict=mergeSampleDict)

elapsed_time = time.time() - start_time
pyPrint("Time used: "+str(elapsed_time)+"s")
