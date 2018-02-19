
# alphatwirl
from Core.EventReader import EventLoopRunner, MPEventLoopRunner, EventLoop
from Core.ProgressBar import ProgressBar,ProgressReport,ProgressMonitor,BProgressMonitor
from Core.Concurrently import CommunicationChannel,CommunicationChannel0
from Core.HeppyResult import HeppyResult,ComponentLoop
from Core.HeppyResult.BEventBuilder import BEventBuilder
from Core.HeppyResult.EventBuilder  import EventBuilder

from Core.HeppyResult.UFEventReader import UFEventReader
from Core.HeppyResult.UFComponentReader import UFComponentReader

# Standard package
import imp,sys

cfgFileName             = sys.argv[1]
file                    = open( cfgFileName,'r')
cfg                     = imp.load_source( 'UFHeppy.__cfg_to_run__', cfgFileName, file)

rootFileDir             = "treeProducerSusyRPV"
rootFile                = "tree.root"
rootTree                = "tree"

nCores                  = cfg.nCores
inputDir                = cfg.inputDir
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

heppyResult = HeppyResult(inputDir,componentList)
eventLoopRunner = MPEventLoopRunner(communicationChannel)
eventBuilder    = BEventBuilder(rootFileDir,rootFile,rootTree,nEvents)
componentReader = UFComponentReader(eventBuilder, eventLoopRunner, sequence, outputInfo)
componentLoop   = ComponentLoop(componentReader)

print "\nBegin Running\n"
componentLoop(heppyResult.components())

print "\nEnd Running\n"
if not disableProgressBar: progressMonitor.end()
communicationChannel.end()
