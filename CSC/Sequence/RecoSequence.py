from Core.Sequence import Sequence

from CSC.Producer.StandAloneMuonProducer import StandAloneMuonProducer
from CSC.Producer.SegmentProducer import SegmentProducer
from CSC.Weighter.EventWeighter import EventWeighter

eventWeighter = EventWeighter("EventWeighter")
standAloneMuonProducer = StandAloneMuonProducer("StandAloneMuonProducer")
segmentProducer = SegmentProducer("SegmentProducer")

MuonSequence = Sequence()
MuonSequence.add(eventWeighter)
MuonSequence.add(standAloneMuonProducer)
#MuonSequence.add(segmentProducer)
