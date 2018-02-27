
# alphatwirl
from Core.EventReader import EventLoopRunner, MPEventLoopRunner, EventLoop
from Core.ProgressBar import ProgressBar,ProgressReport,ProgressMonitor,BProgressMonitor
from Core.Concurrently import CommunicationChannel,CommunicationChannel0

from Core.NanoAODResult.BEventBuilder import BEventBuilder

from Core.HeppyResult import ComponentLoop
from Core.HeppyResult.UFComponentReader import UFComponentReader

# Standard package
import imp,sys

cfgFileName             = sys.argv[1]
file                    = open( cfgFileName,'r')
cfg                     = imp.load_source( 'UFNanoAOD.__cfg_to_run__', cfgFileName, file)

rootTree                = "Events"

nCores                  = cfg.nCores
componentList           = cfg.componentList
nEvents                 = cfg.nEvents
disableProgressBar      = cfg.disableProgressBar
sequence                = cfg.sequence
outputInfo              = cfg.outputInfo

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
eventBuilder    = BEventBuilder(rootTree,nEvents)
componentReader = UFComponentReader(eventBuilder, eventLoopRunner, sequence, outputInfo)
componentLoop   = ComponentLoop(componentReader)

print "\nBegin Running\n"
componentLoop(componentList)

print "\nEnd Running\n"
if not disableProgressBar: progressMonitor.end()
communicationChannel.end()
