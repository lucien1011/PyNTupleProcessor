
# alphatwirl
from Core.EventReader import EventLoopRunner, MPEventLoopRunner, EventLoop
from Core.ProgressBar import ProgressBar,ProgressReport,ProgressMonitor,BProgressMonitor
from Core.Concurrently import CommunicationChannel,CommunicationChannel0

from Core.BEventBuilder import BEventBuilder

from Core.ComponentLoop import ComponentLoop
from Core.UFComponentReader import UFComponentReader

from Core.Utils.git import getGitDescribe,getGitDiff

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

start_time = time.time()

if not justEndSequence:
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
    
    print "\nLoading samples:\n"
    
    eventLoopRunner = MPEventLoopRunner(communicationChannel)
    eventBuilder    = BEventBuilder()
    componentReader = UFComponentReader(eventBuilder, eventLoopRunner, sequence, outputInfo)
    componentLoop   = ComponentLoop(componentReader)
    
    print "\nBegin Running\n"
    componentLoop(componentList)
    
    print "\nEnd Running\n"
    print "\nOutput saved in "+outputInfo.outputDir+"\n"
    
    gitFile        = os.path.join(outputInfo.outputDir,"gitDetails.txt")
    gitVerboseFile = os.path.join(outputInfo.outputDir,"gitVerboseDetails.txt")
    with open(gitFile,'w') as f:
        f.write(getGitDescribe())
    
    with open(gitVerboseFile,'w') as f:
        f.write(getGitDiff())
    
    if not disableProgressBar: progressMonitor.end()
    communicationChannel.end()

print "\nBegin Summarising\n"
print "\nInput used: "+outputInfo.outputDir+"\n"
endSequence.run(outputInfo,componentList)

elapsed_time = time.time() - start_time
print "Time used: "+str(elapsed_time)+"s"
